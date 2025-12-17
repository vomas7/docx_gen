from typing import Dict, Any


class CaseInsensitiveDict(Dict[str, Any]):
    """Mapping type that behaves like dict except that it matches without respect to the
    case of the key.

    E.g. cid['A'] == cid['a']. Note this is not general-purpose, just complete enough to
    satisfy opc package needs. It assumes str keys, and that it is created empty; keys
    passed in constructor are not accounted for
    """

    def __contains__(self, key):
        return super(CaseInsensitiveDict, self).__contains__(key.lower())

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())

    def __setitem__(self, key, value):
        return super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)
