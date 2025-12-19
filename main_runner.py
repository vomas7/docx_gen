# from docx import Document
#
# # from core.oxml_magic.parser import make_xml_tree, to_xml_str
# # from core.ui_objects import Run, Text
#
#
# doc = Document()
# doc.add_paragraph('1111')
#
# doc.add_section()
# doc.add_paragraph('1111')
# doc.add_page_break()
#
# doc.save("aaaaaaaaaa.docx")
#
#
# #
# # r = Run()
# # r.add_page_break()
# #
# # r.add(Text("AAAAAAAAAAAAAAAAAAAAA"))
# # r.add_column_break()
# #
# # run_element = make_xml_tree(r)
# #
# #
# # run_xml_str = to_xml_str(run_element)
# # print(run_xml_str)
# #
# # s = """
# #   <w:body xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
# #     <w:p>
# #       {run}
# #     </w:p>
# #     <w:sectPr w:rsidR="00FC693F" w:rsidRPr="0006063C" w:rsidSect="00034616">
# #       <w:pgSz w:w="12240" w:h="15840"/>
# #       <w:pgMar w:top="1440" w:right="1800" w:bottom="1440" w:left="1800" w:header="720"
# #       w:footer="720" w:gutter="0"/>
# #       <w:cols w:space="720"/>
# #       <w:docGrid w:linePitch="360"/>
# #     </w:sectPr>
# #   </w:body>
# # """
# # s = s.format(run=run_xml_str)
# # from lxml import etree
# # namespaces = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
# # root = etree.fromstring(s.encode("utf-8"))
# # d = Document()
# #
# # d._element.clear()
# # d._element.insert(0, root)
# #
# # d.save("test.docx")


from core.io.package import PackageReader
from core.io.package import IOPackage
from core.oxml_magic.parser import convert_xml_to_cls, make_xml_tree, to_xml_str

# ppkg = IOPackage.open("aaaaaaaaaa.docx")
#
# ppkg.save("sosi.docx")

from core.ui_objects import Section, Body, Document, CLASS_REGISTRY
from core.oxml_magic.parser import convert_xml_to_cls, make_xml_tree, to_xml_str
from core.io.package import Package
ppkg = Package.open(r"C:\Users\AkentevDV\Desktop\localProjects\docx_gen\.venv\Lib\site-packages\docx\templates\default.docx")
xml_doc = ppkg.main_document_part._element
c = convert_xml_to_cls(xml_doc)
m = make_xml_tree(c)

print(to_xml_str(m))


# ppkg.save("sosi.docx")








from core.ui_objects import Section, Body, Document, CLASS_REGISTRY
# document = Document(linked_objects=[])
# body = Body()
# document.add(body)
# section = Section()
# body.add(section)
# c = make_xml_tree(document)

# print(to_xml_str(c))










"""
<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:mo="http://schemas.microsoft.com/office/mac/office/2008/main" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:mv="urn:schemas-microsoft-com:mac:vml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 wp14">
  <w:body>
    <w:sectPr w:rsidR="00FC693F" w:rsidRPr="0006063C" w:rsidSect="00034616">
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1800" w:bottom="1440" w:left="1800" w:header="720" w:footer="720" w:gutter="0"/>
      <w:cols w:space="720"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
</w:document>


"""
