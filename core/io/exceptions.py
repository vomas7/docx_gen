"""Exceptions specific to python-io.

The base exception class is OpcError.
"""


class OpcError(Exception):
    """Base error class for python-io."""


class PackageNotFoundError(OpcError):
    """Raised when a package cannot be found at the specified path."""
