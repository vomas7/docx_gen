"""The proxy class for an image part, and related objects."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

from core.image.image import Image
from core.io.part import Part
from core.utils.metrics import Emu, Inches

from typing import IO
from core.io.pkgurl import PackURI

if TYPE_CHECKING:
    from core.io.package import IOPackage


class ImagePart(Part):
    """An image part.

    Corresponds to the target part of a relationship with type RELATIONSHIP_TYPE.IMAGE.
    """

    def __init__(
            self, partname: PackURI, content_type: str, blob: bytes,
            image: Image | None = None
    ):
        super(ImagePart, self).__init__(partname, content_type, blob)
        self._image = image

    @property
    def default_cx(self):
        """Native width of this image, calculated from its width in pixels and
        horizontal dots per inch (dpi)."""
        px_width = self.image.px_width
        horz_dpi = self.image.horz_dpi
        width_in_inches = px_width / horz_dpi
        return Inches(width_in_inches)

    @property
    def default_cy(self):
        """Native height of this image, calculated from its height in pixels and
        vertical dots per inch (dpi)."""
        px_height = self.image.px_height
        horz_dpi = self.image.horz_dpi
        height_in_emu = int(round(914400 * px_height / horz_dpi))
        return Emu(height_in_emu)

    @property
    def filename(self):
        """Filename from which this image part was originally created.

        A generic name, e.g. 'image.png', is substituted if no name is available, for
        example when the image was loaded from an unnamed stream. In that case a default
        extension is applied based on the detected MIME type of the image.
        """
        if self._image is not None:
            return self._image.filename
        return "image.%s" % self.partname.ext

    @classmethod
    def from_image(cls, image: Image, partname: PackURI):
        """Return an |ImagePart| instance newly created from `image` and assigned
        `partname`."""
        return ImagePart(partname, image.content_type, image.blob, image)

    @property
    def image(self) -> Image:
        if self._image is None:
            self._image = Image.from_blob(self.blob)
        return self._image

    @classmethod
    def load(cls, partname: PackURI, content_type: str, blob: bytes,
             package: IOPackage):
        """Called by ``ui_objects.io.package.PartFactory`` to load an image part from a
        package being opened by ``Document(...)`` call."""
        return cls(partname, content_type, blob)

    @property
    def sha1(self):
        """SHA1 hash digest of the blob of this image part."""
        return hashlib.sha1(self.blob).hexdigest()


"""WordprocessingML Package class and related objects."""


class ImageParts:
    """Collection of |ImagePart| objects corresponding to images in the package."""

    def __init__(self):
        self._image_parts: list[ImagePart] = []

    def __contains__(self, item: object):
        return self._image_parts.__contains__(item)

    def __iter__(self):
        return self._image_parts.__iter__()

    def __len__(self):
        return self._image_parts.__len__()

    def append(self, item: ImagePart):
        self._image_parts.append(item)

    def get_or_add_image_part(self,
                              image_descriptor: str | IO[bytes]) -> ImagePart:
        """Return |ImagePart| object containing image identified by `image_descriptor`.

        The image-part is newly created if a matching one is not present in the
        collection.
        """
        image = Image.from_file(image_descriptor)
        matching_image_part = self._get_by_sha1(image.sha1)
        if matching_image_part is not None:
            return matching_image_part
        return self._add_image_part(image)

    def _add_image_part(self, image: Image):
        """Return |ImagePart| instance newly created from `image` and appended to the collection."""
        partname = self._next_image_partname(image.ext)
        image_part = ImagePart.from_image(image, partname)
        self.append(image_part)
        return image_part

    def _get_by_sha1(self, sha1: str) -> ImagePart | None:
        """Return the image part in this collection having a SHA1 hash matching `sha1`,
        or |None| if not found."""
        for image_part in self._image_parts:
            if image_part.sha1 == sha1:
                return image_part
        return None

    def _next_image_partname(self, ext: str) -> PackURI:
        """The next available image partname, starting from ``/word/media/image1.{ext}``
        where unused numbers are reused.

        The partname is unique by number, without regard to the extension. `ext` does
        not include the leading period.
        """

        def image_partname(n: int) -> PackURI:
            return PackURI("/word/media/image%d.%s" % (n, ext))

        used_numbers = [image_part.partname.idx for image_part in self]
        for n in range(1, len(self) + 1):
            if n not in used_numbers:
                return image_partname(n)
        return image_partname(len(self) + 1)
