import logging
from pydantic import BaseModel
from crewai.tools import BaseTool

# -----------------------------
# Python logger setup
# -----------------------------
logger = logging.getLogger("crewai")
logger.setLevel(logging.INFO)

# handler = logging.StreamHandler()
# formatter = logging.Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )
# handler.setFormatter(formatter)
# logger.addHandler(handler)


# -----------------------------
# Minimal BaseModel tool
# prefix is now a call-time argument
# -----------------------------
class LogInfoTool(BaseTool, BaseModel):
    """
    A CrewAI tool that writes a message to the Python logger.
    The prefix is supplied on each tool call.
    """

    name: str = "LogInfoTool"
    description: str = (
        "Write an INFO-level log line. "
        "Arguments: message (str), prefix (str)."
    )

    def _run(self, message: str, prefix: str = "LLM") -> str:
        logger.info(
            f"[DEBUG] LogInfoTool invoked with message={message!r}, prefix={prefix!r}"
        )
        print(f"LOGGING: {prefix}: {message}")
        logger.info(f"{prefix}: {message}")
        return f"Logged with prefix '{prefix}'."

    async def _arun(self, message: str, prefix: str = "LLM") -> str:
        logger.info(f"{prefix}: {message}")
        return f"Logged with prefix '{prefix}'."
