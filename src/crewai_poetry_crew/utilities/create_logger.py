import os
import sys
import logging
from datetime import datetime


def create_log_file(name: str, suffix: str = ".log", directory: str = "logs") -> str:

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = name + '-' + timestamp + suffix
    if not os.path.exists(directory):
        print(f"Creating '{directory}' directory", file=sys.stderr)
        os.makedirs(directory)
        print(f"Created '{directory}' directory", file=sys.stderr)        
    return os.path.join(directory, filename)


def create_logger(name: str, directory: str = "logs") -> logging.Logger:
    try:
        filename = create_log_file(name=name, directory=directory)
        print(f"Creating log file: {filename}", file=sys.stderr)
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(filename),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(name)
    except Exception as e:
        print(f"Error creating logger: {e}", file=sys.stderr)
    return None
