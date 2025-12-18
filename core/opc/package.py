"""Objects that implement reading and writing OPC packages."""

from __future__ import annotations

from typing import IO, TYPE_CHECKING, Iterator, cast

from core.opc.constants import RELATIONSHIP_TYPE as RT
from core.opc.part import PartFactory
from core.opc.pkgreader import PackageReader
from core.opc.utils import lazyproperty

from core.opc.rel import Relationships
from core.opc.pkgurl import PACKAGE_URI

from core.parts.image import ImageParts

if TYPE_CHECKING:
    from core.opc.part import Part
    from core.opc.rel import _Relationship
    from core.parts.image import ImagePart


class OpcPackage:

    def __init__(self):
        super(OpcPackage, self).__init__()

    def after_unmarshal(self):
        pass

    @lazyproperty
    def rels(self):
        """Return a reference to the |Relationships| instance holding the collection of
        relationships for this package."""
        return Relationships(PACKAGE_URI.baseURI)

    def load_rel(self, reltype: str, target: Part | str, rId: str,
                 is_external: bool = False):
        """Return newly added |_Relationship| instance of `reltype` between this part
        and `target` with key `rId`.

        Target mode is set to ``RTM.EXTERNAL`` if `is_external` is |True|. Intended for
        use during load from a serialized package, where the rId is well known. Other
        methods exist for adding a new relationship to the package during processing.
        """
        return self.rels.add_relationship(reltype, target, rId, is_external)

    def part_related_by(self, reltype: str) -> Part:
        """Return part to which this package has a relationship of `reltype`.

        Raises |KeyError| if no such relationship is found and |ValueError| if more than
        one such relationship is found.
        """
        return self.rels.part_with_reltype(reltype)

    def iter_rels(self) -> Iterator[_Relationship]:
        """Generate exactly one reference to each relationship in the package by
        performing a depth-first traversal of the rels graph."""

        def walk_rels(
                source: OpcPackage | Part, visited: list[Part] | None = None
        ) -> Iterator[_Relationship]:
            visited = [] if visited is None else visited
            for rel in source.rels.values():
                yield rel
                if rel.is_external:
                    continue
                part = rel.target_part
                if part in visited:
                    continue
                visited.append(part)
                new_source = part
                for rel in walk_rels(new_source, visited):
                    yield rel

        for rel in walk_rels(self):
            yield rel

    @property
    def main_document_part(self):
        """Return a reference to the main document part for this package.

        Examples include a document part for a WordprocessingML package, a presentation
        part for a PresentationML package, or a workbook part for a SpreadsheetML
        package.
        """

        return self.part_related_by(RT.OFFICE_DOCUMENT)

    @classmethod
    def open(cls, pkg_file: str | IO[bytes]) -> OpcPackage:
        """Return an |OpcPackage| instance loaded with the contents of `pkg_file`."""
        pkg_reader = PackageReader.from_file(pkg_file)

        package = cls()
        Unmarshaller.unmarshal(pkg_reader, package, PartFactory)
        return package

    # def save(self, pkg_file: str | IO[bytes]):
    #     """Save this package to `pkg_file`.
    #
    #     `pkg_file` can be either a file-path or a file-like object.
    #     """
    #     for part in self.parts:
    #         part.before_marshal()
    #     PackageWriter.write(pkg_file, self.rels, self.parts)


class Package(OpcPackage):
    """Customizations specific to a WordprocessingML package."""

    def after_unmarshal(self):
        """Called by loading code after all parts and relationships have been loaded.

        This method affords the opportunity for any required post-processing.
        """
        self._gather_image_parts()

    def get_or_add_image_part(self,
                              image_descriptor: str | IO[bytes]) -> ImagePart:
        """Return |ImagePart| containing image specified by `image_descriptor`.

        The image-part is newly created if a matching one is not already present in the
        collection.
        """
        return self.image_parts.get_or_add_image_part(image_descriptor)

    @lazyproperty
    def image_parts(self) -> ImageParts:
        """|ImageParts| collection object for this package."""
        return ImageParts()

    def _gather_image_parts(self):
        """Load the image part collection with all the image parts in package."""
        for rel in self.iter_rels():
            if rel.is_external:
                continue
            if rel.reltype != RT.IMAGE:
                continue
            if rel.target_part in self.image_parts:
                continue
            self.image_parts.append(cast("ImagePart", rel.target_part))


class Unmarshaller:
    """Hosts static methods for unmarshalling a package from a |PackageReader|."""

    @staticmethod
    def unmarshal(pkg_reader, package, part_factory):
        """Construct graph of parts and realized relationships based on the contents of
        `pkg_reader`, delegating construction of each part to `part_factory`.

        Package relationships are added to `pkg`.
        """
        parts = (Unmarshaller._unmarshal_parts(
            pkg_reader,
            package,
            part_factory
        ))
        Unmarshaller._unmarshal_relationships(pkg_reader, package, parts)
        for part in parts.values():
            part.after_unmarshal()
        package.after_unmarshal()

    @staticmethod
    def _unmarshal_parts(pkg_reader, package, part_factory):
        """Return a dictionary of |Part| instances unmarshalled from `pkg_reader`, keyed
        by partname.

        Side-effect is that each part in `pkg_reader` is constructed using
        `part_factory`.
        """
        parts = {}
        for partname, content_type, reltype, blob in pkg_reader.iter_sparts():
            parts[partname] = part_factory(
                partname,
                content_type,
                reltype,
                blob,
                package
            )
        return parts

    @staticmethod
    def _unmarshal_relationships(pkg_reader, package, parts):
        """Add a relationship to the source object corresponding to each of the
        relationships in `pkg_reader` with its target_part set to the actual target part
        in `parts`."""
        for source_uri, srel in pkg_reader.iter_srels():
            source = package if source_uri == "/" else parts[source_uri]
            target = srel.target_ref if srel.is_external else parts[
                srel.target_partname]
            source.load_rel(srel.reltype, target, srel.rId, srel.is_external)
