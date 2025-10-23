#todo реализовать валидации

def validate_optional_attr(attribute) -> bool:
    """ hz """
    return True

def validate_required_attr(attribute) -> bool:
    """ hz """
    return True

def validate_optional_tag(tag) -> bool:
    """ hz """
    return True

def validate_required_tag(tag) -> bool:
    """ hz """
    return True
import os
import sys

from core.doc_objects.paragraph import Paragraph
from core.doc_objects.text import Text

def check_on_p(x):
    if x is Paragraph:
        return True
    return False

def check_not_text(x):
    if x is Text:
        return False
    return True