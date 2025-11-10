from docx.shared import Cm, Length, Mm


class CM:
    def __new__(cls, cm: float):
        return Length(Cm(cm))


class MM:
    def __new__(cls, mm: float):
        return Length(Mm(mm))