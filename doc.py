import os
from io import BytesIO
from docx import Document
from docx.shared import Cm
from docx.table import Table
from docx.section import Section


class DOC:
    _left_margin: int = 3
    _right_margin: int = 1.5

    def __init__(self, template: str):
        """
        При создании документа - применяются отступы по умолчанию
        Это поведение можно поменять, если переопределить отступы (margins)
        и вызвать функцию setup_margins еще раз, в дочернем классе.
        """
        self.doc = DOC.create_document(template)
        self.setup_margins()

    def get_table(self, table_index: int) -> Table:
        """Возвращает таблицу, по индексу."""
        return self.doc.tables[table_index]

    def get_section(self, section_index: int) -> Section:
        """
        Возвращает секцию, по индексу.
        Пригождается при изменении ориентации страницы.
        """
        return self.doc.sections[section_index]

    @property
    def iter_sections(self) -> iter:
        """Итератор по секциям."""
        yield from self.doc.sections

    def setup_margins(self) -> None:
        """Устанавливает отступы документа слева и справа."""
        for section in self.iter_sections:
            section.left_margin = Cm(self._left_margin)
            section.right_margin = Cm(self._right_margin)

    @staticmethod
    def create_document(template_path: str) -> Document: ############
        """
        Создает документ из шаблона. В шаблоне нужно определить стили.
        """
        return Document(template_path)

    def delete_empty_page_if_exist(self) -> None:
        """
        Вызывается перед созданием байтового представления документа
        Метод проверяет наличие пустой страницы в конце,
        которая могла появиться из-за разрывов страниц, и удаляет ее.
        """
        paragraphs = self.doc.paragraphs
        if paragraphs:
            last_paragraph = paragraphs[-1]
            if not last_paragraph.text.strip():
                p = last_paragraph._element
                p.getparent().remove(p)

    @property
    def doc_bytes(self) -> bytes:
        """
        Метод возвращает байтовое представление документа,
        которое далее используется либо для передачи документа
        по HTTP, либо для записи в файл.
        """
        buffer = BytesIO()
        self.doc.save(buffer)
        content = buffer.getvalue()
        return content

    def save_docx(self, file_name: str, path: str = None) -> None:
        """
        Метод сохраняет документ в директорию проекта в формате docx.
        Если не задан параметр path, то файл создастся в текущей директории
        """
        if path:
            full_path = os.path.join(path, f"{file_name}.docx")
        else:
            full_path = f"{file_name}.docx"
        with open(full_path, "wb") as file:
            file.write(self.doc_bytes)

    def save_pdf(self, file: str) -> None:
        """
        Метод сохраняет документ в директорию проекта в формате pdf.
        """
        pass

    @staticmethod
    def load_docx_as_bytes() -> bytes:
        doc = Document("error_doc.docx")
        buffer = BytesIO()
        doc.save(buffer)
        doc_bytes = buffer.getvalue()
        return doc_bytes
