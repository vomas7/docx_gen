from docx import Document
from core.oxml_magic.parser import make_xml_tree, to_xml_str
from core.ui_objects import Run, Text
from lxml import etree


r = Run()

r.add_text("text1")
r.font = "Times New Roman"
print(r.font)
run_xml_str_tab = to_xml_str(make_xml_tree(r))
s = """
  <w:body xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:p>
      {run}
    </w:p>
    <w:sectPr w:rsidR="00FC693F" w:rsidRPr="0006063C" w:rsidSect="00034616">
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1800" w:bottom="1440" w:left="1800" w:header="720"
      w:footer="720" w:gutter="0"/>
      <w:cols w:space="720"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
"""
s = s.format(run=run_xml_str_tab)


namespaces = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
root = etree.fromstring(s.encode("utf-8"))
d = Document()

d._element.clear()
d._element.insert(0, root)

d.save("test.docx")
