from pathlib import Path

from core.doc import get_default_docx_path


def is_default_template_path(path: Path) -> bool:
    return Path(get_default_docx_path()) == Path(path)
