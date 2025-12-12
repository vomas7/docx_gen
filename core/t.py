from docx import Document

from oxml_magic.parser import make_xml_tree, to_xml_str
from core.ui_objects import Run, Text


# r = Run()
# t = Text("Я ПИДОРАС")


r = Run()
r.add_page_break()

r.add(Text("AAAAAAAAAAAAAAAAAAAAA"))
r.add_column_break()

run_element = make_xml_tree(r)


run_xml_str = to_xml_str(run_element)
print(run_xml_str)

s = """
  <w:body xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:p>
      {run}
    </w:p>
    <w:sectPr w:rsidR="00FC693F" w:rsidRPr="0006063C" w:rsidSect="00034616">
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1800" w:bottom="1440" w:left="1800" w:header="720" w:footer="720" w:gutter="0"/>
      <w:cols w:space="720"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
"""
s = s.format(run=run_xml_str)
from lxml import etree
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
root = etree.fromstring(s.encode('utf-8'))
d = Document()

d._element.clear()
d._element.insert(0, root)

d.save("test.docx")
