import pytest

from docx import Document

d = Document()

d.add_paragraph("Здесь некий текст с пробелами")

d.save(r"C:\Users\Balabanov.DA\PycharmProjects\docx_gen\tests\t.docx")

