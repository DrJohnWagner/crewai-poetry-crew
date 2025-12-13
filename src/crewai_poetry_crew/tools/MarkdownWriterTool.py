import os
import json
from crewai.tools import BaseTool
import re
import logging
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Type, Optional

logger = logging.getLogger("crewai")

# Regex to strip a trailing datetime stamp like -2025-11-24-02-40-00 from a base filename
TIMESTAMP_RE = re.compile(r"-\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}$")


def normalise_base_filename(filename: str) -> str:
    """
    Normalise a caller-provided *base filename* (no extension) before use:

    - Strip a single trailing datetime stamp, if the LLM accidentally included one.
    - Remove characters that are problematic on most filesystems.
    - Trim and compress whitespace.

    This function works purely at the "logical filename" level; it does not
    add extensions or timestamps.
    """
    # Strip one trailing datetime stamp if present
    base = TIMESTAMP_RE.sub("", filename).strip()

    # Remove characters that are problematic on most filesystems
    # (keep letters, digits, spaces, underscores, hyphens)
    base = re.sub(r'[\\/:*?"<>|]', "", base)

    # Compress whitespace to single spaces
    base = re.sub(r"\s+", " ", base).strip()

    return base


def create_filename(base_filename: str, extension: str = "md") -> str:
    """
    Create a safe, timestamped markdown filename from a *base filename*.

    The caller supplies a base filename with no extension, e.g.
    "case-study-a-constraint-driven-mutation". We normalise it, convert
    spaces to underscores, and append a datetime stamp and the extension.

    Ensures we only ever end up with a single datetime stamp.
    """
    base = normalise_base_filename(base_filename)
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Convert spaces to underscores and keep alphanumerics, underscores, hyphens
    safe_base_name = re.sub(r"[^\w\-]+", "_", base).strip("_")

    filename = f"{safe_base_name}-{timestamp}.{extension}"
    logger.debug(f"Final filename after normalisation and timestamp: {filename}")
    return filename


class MarkdownWriterToolInput(BaseModel):
    """Input schema for MarkdownWriterTool."""  # noqa: D401

    filename: str = Field(
        ...,
        description=(
            "The base filename (without extension) to use for the markdown file, "
            "e.g. 'Case Study a Constraint-Driven Mutation'. "
            "Do NOT include any timestamps or file extensions."
        ),
    )
    content: str = Field(
        ...,
        description=(
            "The complete markdown content to write to the publication file. "
            "This should already contain the combined poet and critic blocks, "
            "with all formatting preserved exactly."
        ),
    )


class MarkdownWriterTool(BaseTool):
    """Tool that writes a final markdown file for publication.

    This tool takes a logical *filename* (without extension) and the full markdown
    content, writes a .md file under the configured output directory, and returns
    the final file path.

    In this workflow, the tool ONLY needs to be called successfully once per
    crew run. To guard against framework bugs or repeated tool calls, this
    implementation is idempotent: after the first successful write in a run,
    subsequent calls will NOT write a new file and will simply return the
    path to the already-written file.
    """  # noqa: D401

    name: str = "MarkdownWriterTool"
    description: str = (
        "Writes the final combined markdown content to a single .md file on disk. "
        "Takes two arguments: 'filename' (base filename without extension) and "
        "'content' (the complete markdown to write). "
        "Returns a JSON string with status and file_path."
    )
    args_schema: Type[BaseModel] = MarkdownWriterToolInput

    # Per-instance state to enforce idempotency for a single crew run
    has_already_written_file: bool = False
    last_file_path: Optional[str] = None

    def __init__(self, **data):
        # Important: call BaseTool's __init__ so Pydantic / CrewAI wiring works
        super().__init__(**data)
        # Explicit per-instance flags
        self.has_already_written_file = False
        self.last_file_path = None

    def _run(self, filename: str, content: str) -> str:
        """Write the given content to a markdown file derived from the filename.

        Idempotent behaviour:

        - On the first successful call in a crew run, it writes the file and
          stores the path.
        - On subsequent calls in the same run, it does NOT write again; it
          simply returns the existing file path.
        """  # noqa: D401
        logger.info(f"MarkdownWriterTool called with: {filename}")
        # If we've already written the file in this run, do not write again
        if self.has_already_written_file and self.last_file_path is not None:
            logger.info(
                "MarkdownWriterTool called again, but file has already been written "
                f"for this run. Reusing existing file: {self.last_file_path}"
            )
            return json.dumps(
                {
                    "status": "ok",
                    "filename": os.path.basename(self.last_file_path),
                    "file_path": self.last_file_path,
                    "note": "Reused existing file for this crew run.",
                }
            )

        try:
            directory = os.environ.get("PUBLISH_OUTPUT_DIR", "publications")
            os.makedirs(directory, exist_ok=True)

            final_filename = create_filename(filename)
            file_path = os.path.join(directory, final_filename)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            logger.info(f"MarkdownWriterTool wrote file: {file_path}")

            # Update idempotent state
            self.has_already_written_file = True
            self.last_file_path = file_path

            # Return a JSON-serialised summary
            return json.dumps(
                {
                    "status": "ok",
                    "filename": final_filename,
                    "file_path": file_path,
                }
            )
        except Exception as e:
            logger.error(f"Error writing file: {e}")
            return json.dumps({"status": "error", "message": str(e)})
