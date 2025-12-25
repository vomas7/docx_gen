from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from core.io.constants import CONTENT_TYPE as CT
from core.io.pkgurl import PackURI
from core.io.part import XmlPart
from core.oxml_magic.ns import nsdecls
from core.io.oxml import parse_xml

if TYPE_CHECKING:
    from core.io.package import IOPackage


class CorePropertiesPart(XmlPart):
    """Corresponds to part named ``/docProps/core.xml``.

    The "core" is short for "Dublin Core" and contains document metadata relatively common across
    documents of all types, not just DOCX.
    """

    @classmethod
    def default(cls, package: IOPackage):
        """Return a new |CorePropertiesPart| object initialized with default values for
        its base properties."""
        core_properties_part = cls.new(package)
        core_properties = core_properties_part.core_properties
        core_properties.title = "Word Document"
        core_properties.last_modified_by = "python-ui_objects"
        core_properties.revision = 1
        core_properties.modified = dt.datetime.now(dt.timezone.utc)
        _coreProperties_tmpl = ("<cp:coreProperties %s/>\n" %
                                nsdecls("cp", "dc", "dcterms"))

        return core_properties_part

    @property
    def core_properties(self):
        """A |CoreProperties| object providing read/write access to the core properties
        contained in this core properties part."""
        return self.element

    @classmethod
    def _new(cls):
        """Return a new `<cp:coreProperties>` element."""
        xml = cls._coreProperties_tmpl
        coreProperties = parse_xml(xml)
        return coreProperties

    @classmethod
    def new(cls, package: IOPackage) -> CorePropertiesPart:
        partname = PackURI("/docProps/core.xml")
        content_type = CT.OPC_CORE_PROPERTIES
        coreProperties = cls._new()
        return CorePropertiesPart(partname, content_type, coreProperties, package)
