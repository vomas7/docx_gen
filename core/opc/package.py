"""Objects that implement reading and writing OPC packages."""

from __future__ import annotations

from typing import IO, TYPE_CHECKING, Iterator

# from docx.opc.constants import RELATIONSHIP_TYPE as RT
# from docx.opc.packuri import PACKAGE_URI
# from docx.opc.part import PartFactory
from core.opc.pkgreader import PackageReader

# from docx.opc.pkgwriter import PackageWriter
# from docx.opc.rel import Relationships
# from docx.shared import lazyproperty

if TYPE_CHECKING:
    # from docx.opc.part import Part
    pass


class OpcPackage:

    def __init__(self):
        super(OpcPackage, self).__init__()

    @classmethod
    def open(cls, pkg_file: str | IO[bytes]) -> OpcPackage:
        """Return an |OpcPackage| instance loaded with the contents of `pkg_file`."""
        pkg_reader = PackageReader.from_file(pkg_file)
        print(pkg_reader._pkg_srels)
        print(pkg_reader._sparts)

        # package = cls()
        # Unmarshaller.unmarshal(pkg_reader, package, PartFactory)

        # return package

    # def save(self, pkg_file: str | IO[bytes]):
    #     """Save this package to `pkg_file`.
    #
    #     `pkg_file` can be either a file-path or a file-like object.
    #     """
    #     for part in self.parts:
    #         part.before_marshal()
    #     PackageWriter.write(pkg_file, self.rels, self.parts)

#
# class Unmarshaller:
#     """Hosts static methods for unmarshalling a package from a |PackageReader|."""
#
#     @staticmethod
#     def unmarshal(pkg_reader, package, part_factory):
#         """Construct graph of parts and realized relationships based on the contents of
#         `pkg_reader`, delegating construction of each part to `part_factory`.
#
#         Package relationships are added to `pkg`.
#         """
#         parts = Unmarshaller._unmarshal_parts(pkg_reader, package,
#                                               part_factory)
#         Unmarshaller._unmarshal_relationships(pkg_reader, package, parts)
#         for part in parts.values():
#             part.after_unmarshal()
#         package.after_unmarshal()
#
#     @staticmethod
#     def _unmarshal_parts(pkg_reader, package, part_factory):
#         """Return a dictionary of |Part| instances unmarshalled from `pkg_reader`, keyed
#         by partname.
#
#         Side-effect is that each part in `pkg_reader` is constructed using
#         `part_factory`.
#         """
#         parts = {}
#         for partname, content_type, reltype, blob in pkg_reader.iter_sparts():
#             parts[partname] = part_factory(partname, content_type, reltype,
#                                            blob, package)
#         return parts
#
#     @staticmethod
#     def _unmarshal_relationships(pkg_reader, package, parts):
#         """Add a relationship to the source object corresponding to each of the
#         relationships in `pkg_reader` with its target_part set to the actual target part
#         in `parts`."""
#         for source_uri, srel in pkg_reader.iter_srels():
#             source = package if source_uri == "/" else parts[source_uri]
#             target = srel.target_ref if srel.is_external else parts[
#                 srel.target_partname]
#             source.load_rel(srel.reltype, target, srel.rId, srel.is_external)
