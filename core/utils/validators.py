from typing import Sequence

def validate_for_none(seq: Sequence):
    if None in seq:
        raise TypeError("`None` is not available for sequence")
