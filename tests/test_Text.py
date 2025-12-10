from core.ui_objects.Text import Text


def test_text():
    t_object = Text("Ave Maria!")
    assert isinstance(t_object, Text)
    assert t_object.tag == 'w:t'
    assert t_object.__repr__() == t_object.__str__() == "Text(Ave Maria!)"
