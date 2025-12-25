"""|DocumentPart| and closely related objects."""

from __future__ import annotations

from typing import IO

from core.io.constants import RELATIONSHIP_TYPE as RT
from core.parts.hdrftr import FooterPart, HeaderPart
from core.parts.numbering import NumberingPart
from core.parts.story import StoryPart
from core.io.utils import lazyproperty



class DocumentPart(StoryPart):
    """Main document part of a WordprocessingML (WML) package, aka a .ui_objects file.

    Acts as broker to other parts such as image, core properties, and style parts. It
    also acts as a convenient delegate when a mid-document object needs a service
    involving a remote ancestor. The `Parented.part` property inherited by many content
    objects provides access to this part object for that purpose.
    """

    def add_footer_part(self):
        """Return (footer_part, rId) pair for newly-created footer part."""
        footer_part = FooterPart.new(self.package)
        rId = self.relate_to(footer_part, RT.FOOTER)
        return footer_part, rId

    def add_header_part(self):
        """Return (header_part, rId) pair for newly-created header part."""
        header_part = HeaderPart.new(self.package)
        rId = self.relate_to(header_part, RT.HEADER)
        return header_part, rId



    @property
    def document(self):
        """A |Document| object providing access to the content of this document."""
        return self.package._elemet

    def drop_header_part(self, rId: str) -> None:
        """Remove related header part identified by `rId`."""
        self.drop_rel(rId)

    def footer_part(self, rId: str):
        """Return |FooterPart| related by `rId`."""
        return self.related_parts[rId]


    def header_part(self, rId: str):
        """Return |HeaderPart| related by `rId`."""
        return self.related_parts[rId]

    @lazyproperty
    def numbering_part(self):
        """A |NumberingPart| object providing access to the numbering definitions for
        this document.

        Creates an empty numbering part if one is not present.
        """
        try:
            return self.part_related_by(RT.NUMBERING)
        except KeyError:
            numbering_part = NumberingPart.new()
            self.relate_to(numbering_part, RT.NUMBERING)
            return numbering_part

    def save(self, path_or_stream: str | IO[bytes]):
        """Save this document to `path_or_stream`, which can be either a path to a
        filesystem location (a string) or a file-like object."""
        self.package.save(path_or_stream)

