from core.ui_objects import BaseContentTag

class BookmarkStart(BaseContentTag):

    @property
    def tag(self) -> str:
        return "w:bookmarkStart"


class BookmarkEnd(BaseContentTag):

    @property
    def tag(self) -> str:
        return "w:bookmarkEnd"