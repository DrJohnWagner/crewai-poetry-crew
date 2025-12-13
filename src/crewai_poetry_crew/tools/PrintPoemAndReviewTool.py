import os
import re
import json
import logging
from datetime import datetime
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


logger = logging.getLogger("crewai")

# Regex to strip a trailing datetime stamp like -2025-11-24-02-40-00 from a base filename
TIMESTAMP_RE = re.compile(r"-\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}$")


def normalise_filename(filename: str) -> str:
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
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    normalised = normalise_filename(base_filename)
    normalised = re.sub(r"[^\w\-]+", "-", normalised).strip("-")
    filename = f"{normalised}-{timestamp}.{extension}"
    logger.debug(f"Final filename after normalisation and timestamp: {filename}")
    return filename

def unescape_newlines(text):
    """Unescape newline sequences like \\n, \\\\n, etc., to actual newlines."""
    if isinstance(text, str):
        return text.encode().decode('unicode_escape')
    return text

class PrintPoemAndReviewInput(BaseModel):
    """Input schema for PrintPoemAndReviewTool."""

    poem_title: str = Field(..., description="The title of the poem to be published.")
    poem_text: str = Field(
        ...,
        description="The complete text content of the poem, including all line breaks and formatting.",
    )
    review_title: str = Field(
        ..., description="The title of the critical review accompanying the poem."
    )
    review_body: str = Field(
        ..., description="The complete body content of the critical review."
    )


class PrintPoemAndReviewTool(BaseTool):
    name: str = "Print Poem and Review"
    description: str = (
        "Tool for printing a poem and review. Returns metadata indicating where the works are stored."
    )
    args_schema: Type[BaseModel] = PrintPoemAndReviewInput

    def _run(
        self, poem_title: str, poem_text: str, review_title: str, review_body: str
    ) -> str:
        """
        Prints a poem and review.

        This tool simulates the publication process for a poem and its accompanying review
        in the CrewAI poetry generation workflow. It takes the finalized poem content and
        review content, and returns metadata indicating where the published work would be
        stored.

        The tool is designed to be used by the Publisher agent in the CrewAI crew, serving
        as the final step in the poetry creation pipeline after the poem has been written,
        architected, edited, and reviewed.

        Parameters
        ----------
        poem_title : str
            The title of the poem to be published. This will be used as the base filename
            for the published work (e.g., "Ember on the Collarbone").
        poem_text : str
            The complete text content of the poem, including all line breaks and formatting.
            This should be the final edited version ready for publication.
        review_title : str
            The title of the critical review accompanying the poem. This provides context
            and analysis for the published work.
        review_body : str
            The complete body content of the critical review, containing analysis,
            interpretation, and commentary on the poem.

        Returns
        -------
        str
            A JSON-formatted string containing publication metadata with the following structure:
            {
                "status": "ok",
                "filename": "publications/<poem_title>.md"
            }

        Notes
        -----
        This tool does not actually write files to disk or perform I/O operations. It serves
        as a placeholder/metadata generator for the publication step in the CrewAI workflow.
        The actual file writing is handled by the MarkdownWriterTool used by the Publisher agent.

        The returned file_path follows the convention of storing published works in a
        "publications/" directory with .md extension, making them ready for further
        processing or distribution.
        """
        logger.info(
            f"PrintPoemAndReviewTool called with: {poem_title} and {review_title}."
        )

        try:
            base_dir = os.environ.get("PUBLISH_OUTPUT_DIRECTORY", "publications")
            os.makedirs(base_dir, exist_ok=True)

            filename = create_filename(poem_title)
            file_path = os.path.join(base_dir, filename)

            logger.info(
                f"PrintPoemAndReviewTool printing to {file_path}."
            )
            content = "\n".join([
                "### " + poem_title,
                "By The CrewAI Poetry Crew",
                "",
                "```markdown",
                unescape_newlines(poem_text),
                "```",
                "---",
                "### " + review_title,
                "By The CrewAI Poetry Crew Critic",
                "",
                unescape_newlines(review_body)
            ])
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            logger.info(f"PrintPoemAndReviewTool wrote file: {file_path}")
            return json.dumps({ "status": "OK", "filename": file_path })
        except Exception as e:
            logger.error(f"PrintPoemAndReviewTool: Error writing file: {e}")
            return json.dumps({"status": "ERROR", "message": str(e)})
