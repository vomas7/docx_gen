from enum import Enum

ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}
SECTION_STANDARD = ('<w:sectPr xmlns:w="http://schemas.openxmlformats.org'
                    '/wordprocessingml/2006/main">'
                    '  <w:pgSz w:w="12240" w:h="15840"/>'  # A4 размер в twips (8.5×11 дюймов)
                    '  <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
                    '           w:header="720" w:footer="720" w:gutter="0"/>'
                    '  <w:cols w:space="720"/>'
                    '  <w:docGrid w:linePitch="360"/>'
                    '</w:sectPr>')

PARAGRAPH_STANDARD = ("""
            <w:p 
                xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
                xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
                w14:paraId="{random_paragraph_id}" 
                w14:textId="{random_paragraph_id}" 
                w:rsidR="{random_paragraph_id}" 
                w:rsidRPr="{random_paragraph_id}" 
                w:rsidRDefault="{random_paragraph_id}" 
                w:rsidP="{random_paragraph_id}"
            >
                <w:pPr>
                    <w:rPr/>
                </w:pPr>
            </w:p>
            """)


class LangTag(str, Enum):
    en = 'en-US'
    ru = 'ru-RU'
    de = 'de-DE'
