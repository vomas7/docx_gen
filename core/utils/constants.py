from pathlib import Path
from core.utils.metrics import Twips

DOC_DEFAULT_PATH = str(Path(__file__).parent.parent / "writer" / "default.docx")

# A4 page margins in twips
A4_MARGIN_TOP = Twips(1440)
A4_MARGIN_RIGHT = Twips(1440)
A4_MARGIN_BOTTOM = Twips(1440)
A4_MARGIN_LEFT = Twips(1800)
A4_MARGIN_HEADER = Twips(720)
A4_MARGIN_FOOTER = Twips(720)
A4_MARGIN_GUTTER = Twips(0)

# Letter page margins in twips
LETTER_TOP = Twips(1440)
LETTER_RIGHT = Twips(1440)
LETTER_LEFT = Twips(1440)
LETTER_BOTTOM = Twips(1440)
LETTER_HEADER = Twips(720)
LETTER_FOOTER = Twips(720)
LETTER_GUTTER = Twips(0)

# A4 page size in twips
A4_WIDTH = Twips(12240)
A4_HEIGHT = Twips(15840)

# A3 page size in twips
A3_WIDTH = Twips(16838)
A3_HEIGHT = Twips(23811)

# Letter page size in twips
LETTER_WIDTH = Twips(12240)
LETTER_HEIGHT = Twips(15840)

COLUMN_GAP = Twips(720)
