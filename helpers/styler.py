from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_COLOR_INDEX


class Styler:
    """
    Класс, реализующий стиль текста в документе.
    Основной метод - style_text, использующийся в качестве декоратора.
    Все методы вызываются из экземпляра класса - styler.
    """
    align = WD_PARAGRAPH_ALIGNMENT

    def style_text(self):
        """Декоратор, который стилизует текст, по заданным параметрам."""
        def take_attrs(add_text: callable):
            def init_styler(*args, **kwargs):
                p, kwargs = add_text(*args, **kwargs)
                for key, value in kwargs.items():
                    self.apply_text_styles(p, key, value)
            return init_styler
        return take_attrs

    @staticmethod
    def apply_cell_style(cell, style_name: str = 'ЕИПП_стиль_авто'):
        for paragraph in cell.paragraphs:
            paragraph.style = style_name

    def apply_text_styles(self, p, key, value) -> None:
        """Применение соответствующих стилей к тексту."""
        if key == "align":
            if value == "left":
                p.alignment = self.align.LEFT
            if value == "right":
                p.alignment = self.align.RIGHT
            if value == "center":
                p.alignment = self.align.CENTER
            if value == "justify":
                p.runs[-1].add_tab()
                p.alignment = self.align.JUSTIFY

        if key == "font_name":
            p.runs[-1].font.name = value
        if key == "font_size":
            p.runs[-1].font.size = Pt(value)
        if key == "bold":
            p.runs[-1].font.bold = value
        if key == "underline":
            p.runs[-1].font.underline = value
        if key == "italic":
            p.runs[-1].font.italic = value
        if key == "style":
            p.style = value
        if key == "font_color":
            if value == "red":
                p.runs[-1].font.color.rgb = RGBColor(255, 0, 0)
            if value == "green":
                p.runs[-1].font.color.rgb = RGBColor(0, 204, 0)
            if value == "yellow":
                p.runs[-1].font.color.rgb = RGBColor(255, 255, 0)
            if value == "orange":
                p.runs[-1].font.color.rgb = RGBColor(255, 128, 0)
        if key == "font_back_color":
            if value == "red":
                p.runs[-1].font.highlight_color = WD_COLOR_INDEX.RED
            if value == "green":
                p.runs[-1].font.highlight_color = WD_COLOR_INDEX.GREEN
            if value == "yellow":
                p.runs[-1].font.highlight_color = WD_COLOR_INDEX.YELLOW

    @staticmethod
    def reset_global_font_style(doc, name: str, size: int):
        """Метод устанавливает глобально стиль шрифта и его размер."""
        default_style = doc.styles["Normal"]
        default_style.font.name = name
        default_style.font.size = Pt(size)


styler = Styler()
