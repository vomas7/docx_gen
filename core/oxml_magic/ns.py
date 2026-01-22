"""Namespace-related objects."""

from __future__ import annotations

import re

from typing import Any

nsmap = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcmitype": "http://purl.org/dc/dcmitype/",
    "dcterms": "http://purl.org/dc/terms/",
    "dgm": "http://schemas.openxmlformats.org/drawingml/2006/diagram",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "sl": "http://schemas.openxmlformats.org/schemaLibrary/2006/main",
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "w14": "http://schemas.microsoft.com/office/word/2010/wordml",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "xml": "http://www.w3.org/XML/1998/namespace",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
}

pfxmap = {value: key for key, value in nsmap.items()}

qn_pattern = re.compile(r"</?[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z_][a-zA-Z0-9_-]*[^>]*>")


class NamespacePrefixedTag(str):
    """Value object that knows the semantics of an XML tag having a namespace prefix."""

    def __new__(cls, nstag: str, *args: Any):
        return super().__new__(cls, nstag)

    def __init__(self, nstag: str):
        self._pfx, self._local_part = nstag.split(":")
        self._ns_uri = nsmap[self._pfx]

    @property
    def clark_name(self) -> str:
        return f"{{{self._ns_uri}}}{self._local_part}"

    @classmethod
    def from_clark_name(cls, clark_name: str) -> NamespacePrefixedTag:
        nsuri, local_name = clark_name[1:].split("}")
        nstag = f"{pfxmap[nsuri]}:{local_name}"
        return cls(nstag)

    @property
    def local_part(self) -> str:
        """The local part of this tag.

        E.g. "foobar" is returned for tag "f:foobar".
        """
        return self._local_part

    @property
    def nsmap(self) -> dict[str, str]:
        """Single-member dict mapping prefix of this tag to it's namespace name.

        Example: `{"f": "http://foo/bar"}`. This is handy for passing to xpath calls
        and other uses.
        """
        return {self._pfx: self._ns_uri}

    @property
    def nspfx(self) -> str:
        """The namespace-prefix for this tag.

        For example, "f" is returned for tag "f:foobar".
        """
        return self._pfx

    @property
    def nsuri(self) -> str:
        """The namespace URI for this tag.

        For example, "http://foo/bar" would be returned for tag "f:foobar" if the "f"
        prefix maps to "http://foo/bar" in nsmap.
        """
        return self._ns_uri


def nsdecls(*prefixes: str) -> str:
    """Namespace declaration including each namespace-prefix in `prefixes`.

    Handy for adding required namespace declarations to a tree root element.
    """
    return " ".join(f'xmlns:{pfx}="{nsmap[pfx]}"' for pfx in prefixes)


def nspfxmap(*nspfxs: str) -> dict[str, str]:
    """Subset namespace-prefix mappings specified by *nspfxs*.

    Any number of namespace prefixes can be supplied, e.g. namespaces("a", "r", "p").
    """
    return {pfx: nsmap[pfx] for pfx in nspfxs}


def qn(tag: str) -> str:
    """Stands for "qualified name".

    This utility function converts a familiar namespace-prefixed tag name like "w:p"
    into a Clark-notation qualified tag name for lxml. For example, `qn("w:p")` returns
    "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p".
    """
    prefix, tagroot = tag.split(":")
    uri = nsmap[prefix]
    return f"{{{uri}}}{tagroot}"


def find_qn(collection: dict[str, str]):
    print(collection)
    items = list(filter(lambda x: qn_pattern.match(x.keys()), collection))
    print(items)
    # return re.findall(qn_pattern, collection)


class XmlString(str):
    """Provides string comparison override suitable for serialized XML that is useful
    for tests."""

    # '    <w:xyz xmlns:a="http://ns/decl/a" attr_name="val">text</w:xyz>'
    # |          |                                          ||           |
    # +----------+------------------------------------------++-----------+
    #  front      attrs                                     | text
    #                                                     close

    _xml_elm_line_patt = re.compile(r"( *</?[\w:]+)(.*?)(/?>)([^<]*</[\w:]+>)?$")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, str):
            return False
        lines = self.splitlines()
        lines_other = other.splitlines()
        if len(lines) != len(lines_other):
            return False
        for line, line_other in zip(lines, lines_other):
            if not self._eq_elm_strs(line, line_other):
                return False
        return True

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def _attr_seq(self, attrs: str) -> tuple[str]:
        """Return a sequence of attribute strings parsed from `attrs`.

        Each attribute string is stripped of whitespace on both ends.
        """
        attrs = attrs.strip()
        attr_lst = attrs.split()
        return sorted(attr_lst)

    def _eq_elm_strs(self, line: str, line_2: str):
        """Return True if the element in `line_2` is XML equivalent to the element in
        `line`."""
        front, attrs, close, text = self._parse_line(line)
        front_2, attrs_2, close_2, text_2 = self._parse_line(line_2)
        if front != front_2:
            return False
        if self._attr_seq(attrs) != self._attr_seq(attrs_2):
            return False
        if close != close_2:
            return False
        if text != text_2:
            return False
        return True

    @classmethod
    def _parse_line(cls, line: str) -> tuple[str, str, str, str]:
        """(front, attrs, close, text) 4-tuple result of parsing XML element `line`."""
        match = cls._xml_elm_line_patt.match(line)
        if match is None:
            return "", "", "", ""
        front, attrs, close, text = [match.group(n) for n in range(1, 5)]
        return front, attrs, close, text
