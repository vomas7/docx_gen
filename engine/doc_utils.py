import os
import warnings
from pathlib import Path
from typing import Union
from importlib import resources


def get_default_docx_path() -> Union[str, Path]:
    """Gets path to libs template."""
    try:
        with resources.path("docx.templates", "default.docx") as path:
            return str(path)
    except AttributeError:
        return resources.path("docx.templates", "default.docx").__enter__()


def validate_filepath(path: Path):
    """
    Validate a filepath for writing operations.
    Raises:
        ValueError: If the path is a directory (implies missing filename).
        FileNotFoundError: If the parent directory does not exist.
        PermissionError: If there are no write permissions for the target location.
    Warns:
        UserWarning: If the file already exists and will be overwritten.
    """
    if path.is_dir():
        raise ValueError(f"Path must be a file, not a directory: {path.resolve()}")
    parent = path.parent
    if not parent.exists():
        raise FileNotFoundError(f"Parent directory does not exists: {parent}")
    if not os.access(parent, os.W_OK):
        raise PermissionError(f"No write permissions for directory: {parent}")
    if path.exists():
        warnings.warn(
            f"File already exists and will be overwritten: {path.resolve()}",
            UserWarning
        )
