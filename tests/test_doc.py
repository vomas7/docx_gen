import tempfile
from pathlib import Path

import pytest
import os.path
from engine.doc import DOC
from docx.opc.exceptions import PackageNotFoundError


class TestDOC:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.doc = DOC()

    def test_init(self):
        assert self.doc
        assert "<DOC object: not saved>" == str(self.doc)

    def test_wrong_template_content_type(self):
        with pytest.raises(PackageNotFoundError):
            test_template = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         "test.zip")
            DOC(template=test_template)

    def test_export_to_docx(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file = Path(tmpdir) / 'test.doc'
            self.doc.export(file)
            assert file.is_file()
            assert file.exists()

    def test_export_pdf(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file = Path(tmpdir) / 'test.pdf'
            self.doc.export(file)
            assert file.is_file()
            assert file.exists()

    def test_doc_bytes(self):
        assert isinstance(self.doc.doc_bytes, bytes)
        assert len(self.doc.doc_bytes) > 0

    def test_file_path_setter_validator(self):
        assert self.doc.file is None
        self.doc.file = "test.docx"
        assert str(self.doc.file) == "test.docx"
