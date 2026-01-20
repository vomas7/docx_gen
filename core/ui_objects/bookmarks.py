from core.ui_objects.base.base_content_tag import BaseContentTag


class BookmarkStart(BaseContentTag):
    @property
    def tag(self) -> str:
        return "w:bookmarkStart"


class BookmarkEnd(BaseContentTag):
    @property
    def tag(self) -> str:
        return "w:bookmarkEnd"
