# -----------------------------------------------------------------------------
# Adapted from python-docx (MIT License)
# Copyright (c) 2013 Steve Canny, https://github.com/python-openxml/python-docx
# -----------------------------------------------------------------------------


class Length(int):
    """
    Base class for length constructor classes Inches, Cm, Mm, Px, and Emu.

    Behaves as an int count of English Metric Units, 914,400 to the inch, 36,000 to the
    mm. Provides convenience unit conversion methods in the form of read-only
    properties. Immutable.
    """

    _EMUS_PER_INCH = 914400
    _EMUS_PER_CM = 360000
    _EMUS_PER_MM = 36000
    _EMUS_PER_PT = 12700
    _EMUS_PER_TWIP = 635

    def __new__(cls, emu: int):
        return int.__new__(cls, emu)

    @property
    def cm(self) -> float:
        """The equivalent length expressed in centimeters (float)."""
        return float(self) / float(self._EMUS_PER_CM)

    @property
    def emu(self):
        """The equivalent length expressed in English Metric Units (int)."""
        return self

    @property
    def inches(self):
        """The equivalent length expressed in inches (float)."""
        return float(self) / float(self._EMUS_PER_INCH)

    @property
    def mm(self):
        """The equivalent length expressed in millimeters (float)."""
        return float(self) / float(self._EMUS_PER_MM)

    @property
    def pt(self):
        """Floating point length in points."""
        return float(self) / float(self._EMUS_PER_PT)

    @property
    def twips(self):
        """The equivalent length expressed in twips (int)."""
        return int(round(float(self) / float(self._EMUS_PER_TWIP)))


class Inches(Length):
    """Convenience constructor for length in inches, e.g. ``width = Inches(0.5)``."""

    def __new__(cls, inches: float):
        emu = int(inches * Length._EMUS_PER_INCH)
        return Length.__new__(cls, emu)


class Cm(Length):
    """Convenience constructor for length in centimeters, e.g. ``height = Cm(12)``."""

    def __new__(cls, cm: float):
        emu = int(cm * Length._EMUS_PER_CM)
        return Length.__new__(cls, emu)


class Emu(Length):
    """
    Convenience constructor for length in English Metric Units, e.g. ``width =
        Emu(457200)``.
    """

    def __new__(cls, emu: int):
        return Length.__new__(cls, int(emu))


class Mm(Length):
    """Convenience constructor for length in millimeters, e.g. ``width = Mm(240.5)``."""

    def __new__(cls, mm: float):
        emu = int(mm * Length._EMUS_PER_MM)
        return Length.__new__(cls, emu)


class Pt(Length):
    """Convenience value class for specifying a length in points."""

    def __new__(cls, points: float):
        emu = int(points * Length._EMUS_PER_PT)
        return Length.__new__(cls, emu)


class Twips(Length):
    """Convenience constructor for length in twips, e.g. ``width = Twips(42)``.

    A twip is a twentieth of a point, 635 EMU.
    """

    def __new__(cls, twips: float):
        emu = int(twips * Length._EMUS_PER_TWIP)
        return Length.__new__(cls, emu)


class RGBColor(tuple[int, int, int]):
    """Immutable value object defining a particular RGB color."""

    def __new__(cls, r: int, g: int, b: int):
        msg = "RGBColor() takes three integer values 0-255"
        for val in (r, g, b):
            if not isinstance(val, int) or val < 0 or val > 255:
                raise ValueError(msg)
        return super().__new__(cls, (r, g, b))

    def __repr__(self):
        return "RGBColor(0x%02x, 0x%02x, 0x%02x)" % self

    def __str__(self):
        """Return a hex string rgb value, like '3C2F80'."""
        return "%02X%02X%02X" % self

    @classmethod
    def from_string(cls, rgb_hex_str: str):
        """Return a new instance from an RGB color hex string like ``'3C2F80'``."""
        r = int(rgb_hex_str[:2], 16)
        g = int(rgb_hex_str[2:4], 16)
        b = int(rgb_hex_str[4:], 16)
        return cls(r, g, b)
