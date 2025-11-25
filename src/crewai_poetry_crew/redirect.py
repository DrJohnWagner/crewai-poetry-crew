import sys
import re
from contextlib import contextmanager

# Regular expression to match ANSI escape sequences
ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

class FilteredStream:
    """A custom file-like object that filters escape codes."""
    def __init__(self, stream):
        self.stream = stream

    def write(self, s):
        # Remove ANSI escape codes from the string
        clean = ANSI_ESCAPE.sub('', s)
        # Write the filtered string to the original stream
        self.stream.write(clean)

    def flush(self):
        # Call the flush method on the original stream
        self.stream.flush()

@contextmanager
def redirect_stdout(stream=None):
    """Context manager to redirect stdout. If stream is provided, redirect to it; otherwise, filter ANSI codes from original stdout."""
    old_stdout = sys.stdout
    if stream is not None:
        sys.stdout = FilteredStream(stream)
    else:
        sys.stdout = FilteredStream(old_stdout)
    try:
        yield
    finally:
        sys.stdout = old_stdout

@contextmanager
def redirect_stderr(stream=None):
    """Context manager to redirect stderr. If stream is provided, redirect to it; otherwise, filter ANSI codes from original stderr."""
    old_stderr = sys.stderr
    if stream is not None:
        sys.stderr = FilteredStream(stream)
    else:
        sys.stderr = FilteredStream(old_stderr)
    try:
        yield
    finally:
        sys.stderr = old_stderr

