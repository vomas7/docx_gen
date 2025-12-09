from core.oxml_magic.ns import qn

registered_tag = {}


def register_tag(tag, cls):
    registered_tag[qn(tag)] = cls

def get_cls_by_tag(tag):
    cls = registered_tag.get(qn(tag), None)
    return cls










