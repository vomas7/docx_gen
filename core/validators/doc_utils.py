import os
from pathlib import Path
import warnings

#todo пригодится для эспортера, мб будет изменяться

def validate_filepath(path: Path) -> Path:
    """
    Validate a filepath for writing operations.
    Raises:
        ValueError: If the path is a directory (implies missing filename).
        FileNotFoundError: If the parent directory does not exist.
        PermissionError: If there are no write permissions for the target location.
    Warns:
        UserWarning: If the file already exists and will be overwritten.
    """
    path = path if isinstance(path, Path) else Path(path)
    if path.is_dir():
        raise ValueError(f"Path must be a file, not a directory: {path.resolve()}")
    parent = path.parent
    if not parent.exists():
        raise FileNotFoundError(f"Parent directory does not exists: {parent}")
    if not os.access(parent, os.W_OK):
        raise PermissionError(f"No write permissions for directory: {parent}")
    if path.exists():
        warnings.warn(
            message=f"File already exists and will be overwritten: {path.resolve()}",
            category=UserWarning,
            stacklevel=1
        )
    return path
