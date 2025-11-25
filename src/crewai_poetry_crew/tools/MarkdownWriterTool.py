import os
import sys
from crewai.tools import BaseTool
import re
import logging
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Type, Optional

logger = logging.getLogger("crewai")

# Regex to strip a trailing datetime stamp like -2025-11-24-02-40-00
TIMESTAMP_RE = re.compile(r"-\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}$")


class MarkdownWriterToolInput(BaseModel):
    """Input schema for MarkdownWriterTool."""

    poem_title: str = Field(
        ...,
        description=(
            "The exact poem title to use as the base for the filename, "
            "e.g. 'Hinge of Tender Light'. Do NOT include any timestamps "
            "or file extensions."
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
    """
    Tool that writes the final combined poem-and-critique markdown file.

    In this workflow, the tool ONLY needs to be called successfully once per
    crew run. To guard against framework bugs or repeated tool calls, this
    implementation is idempotent: after the first successful write in a run,
    subsequent calls will NOT write a new file and will simply return the
    existing file path.
    """

    name: str = "Markdown Writer Tool"
    description: str = (
        "Writes the final combined poem-and-critique content to a markdown (.md) file. "
        "The tool handles adding a datetime stamp to the filename and the .md extension. "
        "You MUST pass the poem_title (not a full path) and the complete markdown content. "
        "Use this tool exactly once per poem. If it is called multiple times in the same "
        "run, it will reuse the already written file instead of creating new ones."
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

    def _normalise_base_title(self, poem_title: str) -> str:
        """
        Normalise the poem title before turning it into a base filename:
        - Strip any trailing datetime stamp (if the LLM accidentally includes one).
        - Remove dangerous filesystem characters.
        - Trim and compress whitespace.
        """
        # Strip one trailing datetime stamp if present
        base = TIMESTAMP_RE.sub("", poem_title).strip()

        # Remove characters that are problematic on most filesystems
        # (keep letters, digits, spaces, underscores, hyphens)
        base = re.sub(r'[\\/:*?"<>|]', "", base)

        # Compress whitespace to single spaces, then we'll convert spaces to underscores
        base = re.sub(r"\s+", " ", base).strip()

        return base

    def _make_final_filename(self, poem_title: str) -> str:
        """
        Create a safe, timestamped markdown filename from the poem title.
        Ensures we only ever end up with a single datetime stamp.
        """
        base = self._normalise_base_title(poem_title)
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # Convert spaces to underscores and keep alphanumerics, underscores, hyphens
        safe_base_name = re.sub(r"[^\w\-]+", "_", base).strip("_")

        final_filename = f"{safe_base_name}-{timestamp}.md"
        logger.debug(f"Final filename after normalisation and timestamp: {final_filename}")
        return final_filename

    def _run(self, poem_title: str, content: str) -> str:
        """
        Writes the given content to a markdown file derived from the poem title.

        Idempotent behaviour:
        - On the first successful call in a crew run, it writes the file and
          stores the path.
        - On subsequent calls in the same run, it does NOT write again; it
          simply returns the existing file path.
        """
        # If we've already written the file in this run, do not write again
        if self.has_already_written_file and self.last_file_path is not None:
            logger.info(
                "MarkdownWriterTool called again, but file has already been written "
                f"for this run. Reusing existing file: {self.last_file_path}"
            )
            return (
                "File already written in this run. "
                f"Reusing existing publication at '{self.last_file_path}'."
            )

        logger.info(
            f"Starting to write markdown file for poem_title '{poem_title}' "
            f"with content length {len(content)}"
        )

        final_filename = self._make_final_filename(poem_title)

        try:
            # Create a 'publications' directory if it doesn't exist
            if not os.path.exists("publications"):
                logger.info("Creating 'publications' directory")
                os.makedirs("publications")

            file_path = os.path.join("publications", final_filename)
            logger.debug(f"Directory/filename: {file_path}")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            logger.info(f"File written successfully: {file_path}")

            # Mark as written for this run and remember the path
            self.has_already_written_file = True
            self.last_file_path = file_path

            # Return a message that clearly distinguishes poem_title from file_path
            return (
                "Publication successful. "
                f"poem_title: '{poem_title}'. "
                f"file_path: '{file_path}'."
            )
        except Exception as e:
            logger.error(f"Error writing file: {e}")
            return f"Error writing file: {e}"
