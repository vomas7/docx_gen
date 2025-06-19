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
