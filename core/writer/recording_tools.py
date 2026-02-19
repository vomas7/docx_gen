import os
import shutil
import tempfile
from zipfile import ZipFile
from typing import TYPE_CHECKING
from core.oxml_magic.parser import make_xml_tree, to_xml_str

PARENT_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(PARENT_DIR, "template")

if TYPE_CHECKING:
    from core.ui_objects import Document


def folder_to_docx(output_file: str, template_dir: str = TEMPLATE_DIR):
    """zips template for docx."""
    folder_path = os.path.abspath(template_dir)

    with ZipFile(output_file, "w") as docx_zip:
        for root, _dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                archive_path = os.path.relpath(file_path, folder_path)
                docx_zip.write(file_path, archive_path)


def create_tmp_dir(source_dir=TEMPLATE_DIR, parent_dir=PARENT_DIR) -> str:
    """creates temp dir for zip.docx"""
    if parent_dir is None:
        parent_dir = tempfile.gettempdir()
    temp_dir_path = os.path.join(str(parent_dir), "tmp_dir")
    if os.path.exists(temp_dir_path):
        shutil.rmtree(temp_dir_path, ignore_errors=True)
    shutil.copytree(source_dir, temp_dir_path)
    return temp_dir_path


def put_document_xml(temp_dir, document_xml: str):
    document = os.path.join(temp_dir, "word", "document.xml")
    with open(document, "w", encoding="utf-8") as doc:
        doc.write(document_xml)


def clean_temp_dir(temp_dir):
    shutil.rmtree(temp_dir, ignore_errors=True)


def docx_to_xml(doc_obj: "Document"):
    return to_xml_str(make_xml_tree(doc_obj))


def create_docx(doc_obj: "Document", file_path: str):
    document_folder_template = create_tmp_dir()
    put_document_xml(document_folder_template, docx_to_xml(doc_obj))
    folder_to_docx(file_path, document_folder_template)
    clean_temp_dir(document_folder_template)


def create_docx2(xml, file_path: str):
    document_folder_template = create_tmp_dir()
    put_document_xml(document_folder_template, xml)
    folder_to_docx(file_path, document_folder_template)
    clean_temp_dir(document_folder_template)
