from core.ui_objects.document import Document

# from core.ui_objects.paragraph import Paragraph
from core.ui_objects.table.table import Table
from core.writer.recording_tools import create_docx2
# from core.ui_objects import Section
# from core.writer.recording_tools import create_docx2, create_docx

d = Document()
b = d.body

sect = b.objects[0]
t = Table(2, 2, sect)
b.objects.insert(0, t)
d.save("table.docx")
xml = """<w:document xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dgm="http://schemas.openxmlformats.org/drawingml/2006/diagram" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:sl="http://schemas.openxmlformats.org/schemaLibrary/2006/main" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="w14 wp14">
  <w:body>
    <w:tbl>
      <w:tr>
        <w:tc>
          <w:tcPr>
            <w:tcW w:w="2000"/>
          </w:tcPr>
          <w:p>
            <w:r>
              <w:t>Моча коня ударила в голову Василию</w:t>
            </w:r>
          </w:p>
        </w:tc>
        <w:tc>
          <w:p>Еда</w:p>
        </w:tc>
      </w:tr>
      <w:tr>
        <w:tc>
          <w:p>Как же ворду похуй на мои попытки что либо сделать с таблицей</w:p>
        </w:tc>
        <w:tc>
          <w:p>Ну и иди нахуй</w:p>
        </w:tc>
      </w:tr>
    </w:tbl>
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1800" w:header="720" w:footer="720" w:gutter="0"/>
      <w:cols w:space="720"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
</w:document>"""


create_docx2(xml, "jepa.docx")
#
# from core.ui_objects import CLASS_REGISTRY
# print(CLASS_REGISTRY)
#
#
# from core.oxml_magic.parser import make_xml_tree, to_xml_str
#
# doc = Document("image_word.docx")
#
# tree = make_xml_tree(doc)
# print(to_xml_str(tree))
