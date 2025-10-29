from oxml.xmlchemy import BaseAttributeElement
from docx.oxml.simpletypes import BaseSimpleType, ST_TwipsMeasure
from docx.enum.base import BaseXmlEnum

class AttrMeta():
    pass



class Right():
    default_value = None
    tag_attr = "w:right" #todo заменить строки на енумы




class Left(BaseAttributeElement):
    def __init__(self):
        attr_name = "w:left"
        value = 6500

        super().__init__(attr_name, value, ST_TwipsMeasure)