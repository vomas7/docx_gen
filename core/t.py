import copy

from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from core.doc import DOC
from core.doc_objects.Section import DOCSection
from core.styles.section import SectionStyle


# d = DOC(r'C:\Users\Balabanov.DA\PycharmProjects\docx_gen\core\е.docx')
# p2 = [p for p in d.paragraphs][-1]
# p1 = [p for p in d.paragraphs][0]
# p1_copy = copy.deepcopy(p1)
# d.writer.write(element=p1_copy, before=p2)
# d.save(r'C:\Users\Balabanov.DA\PycharmProjects\docx_gen\core\eе.docx')
sect = DOCSection()
print(sect.elem)
if sect:
    print(1)
print(sect is not None)

