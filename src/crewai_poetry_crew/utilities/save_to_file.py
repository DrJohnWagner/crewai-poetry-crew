from pathlib import Path


def save_to_file(s: str, filename: Path | str) -> None:
    """
    Save a string to a file, creating directories if necessary.

    Args:
        s (str): The string content to save
        filename (Path | str): The file path where to save the content.
                              Can include directories that will be created if they don't exist.
    """
    path = Path(filename)

    # Create parent directories if they don't exist
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write the string to the file
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)