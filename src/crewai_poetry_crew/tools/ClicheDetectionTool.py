from crewai.tools import BaseTool
import re
import logging
from .cliches import CLICHES
from pydantic import BaseModel, Field
from typing import Type

logger = logging.getLogger("crewai")

class ClicheDetectionToolInput(BaseModel):
    """Input schema for ClicheDetectionTool."""
    poem_text: str = Field(..., description="The poem text to analyze for cliches.")

class ClicheDetectionTool(BaseTool):
    name: str = "Cliche Detection Tool"
    description: str = "Identifies a comprehensive list of common cliches and overused phrases in a given text. Useful for helping a poet refine their language."
    args_schema: Type[BaseModel] = ClicheDetectionToolInput

    def _run(self, poem_text: str) -> str:
        logger.info(f"Starting cliche detection on poem text of length {len(poem_text)}")
        # The list is now managed in cliche_list.py
        found_cliches = []
        
        # Use regex to find whole-word matches, case-insensitively
        # This is more robust than simple 'in' checks
        for cliche in CLICHES:
            # We escape the cliche in case it contains special regex characters
            # and use \b for word boundaries to avoid matching parts of words.
            if re.search(r'\b' + re.escape(cliche) + r'\b', poem_text, re.IGNORECASE):
                found_cliches.append(cliche)
        
        if not found_cliches:
            logger.info("No common cliches were found in the text.")
            return "No common cliches were found in the text."
        
        # Format the output nicely
        result = f"The following potential cliches were found: {'; '.join(found_cliches)}."
        logger.info(f"Found cliches: {found_cliches}")
        return result