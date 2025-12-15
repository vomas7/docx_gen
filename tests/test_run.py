from core.ui_objects import LinkedObjects
from core.ui_objects.run import Break, Run, Text


def test_run_tag():
    linked_objects = []
    run = Run(linked_objects)
    assert run.tag == "w:r"


def test_run_access_children():
    linked_objects = []
    run = Run(linked_objects)
    assert run.access_children == {Break, Text}


def test_run_init_with_linked_objects():
    linked_objects = []
    run = Run(linked_objects)
    assert run.linked_objects == linked_objects


def test_run_init_with_list():
    test_list = [Text("style1"), Text("style2")]
    run = Run(test_list)
    assert run._linked_objects == test_list


def test_add_page_break():
    linked_objects = []
    run = Run(linked_objects)

    run.add_page_break()

    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], Break)
    assert run.linked_objects[0].type == "page"


def test_add_column_break():
    linked_objects = []
    run = Run(linked_objects)

    run.add_column_break()

    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], Break)
    assert run.linked_objects[0].type == "column"


def test_add_text_with_string():
    linked_objects = []
    run = Run(linked_objects)

    run.add_text("test string")

    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], Text)
    assert run.linked_objects[0].text == "test string"


def test_add_text_with_text_object():
    linked_objects = []
    run = Run(linked_objects)

    text_obj = Text("test content")
    run.add_text(text_obj)

    assert len(run.linked_objects) == 1
    assert isinstance(run._linked_objects[0], Text)
    assert run._linked_objects[0].text == text_obj.text


def test_add_text_with_empty_string():
    linked_objects = []
    run = Run(linked_objects)

    run.add_text("")

    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], Text)
    assert run.linked_objects[0].text == ""


def test_run_inherits_from_base_container():
    linked_objects = []
    run = Run(linked_objects)

    assert hasattr(run, "add")


def test_run_with_multiple_children():
    linked_objects = []
    run = Run(linked_objects)

    run.add_text("First part ")
    run.add_page_break()
    run.add_text("After page break")

    assert len(run.linked_objects) == 3
    assert isinstance(run.linked_objects[0], Text)
    assert isinstance(run.linked_objects[1], Break)
    assert isinstance(run.linked_objects[2], Text)
    assert run.linked_objects[0].text == "First part "
    assert run.linked_objects[1].type == "page"
    assert run.linked_objects[2].text == "After page break"


def test_add_text_directly():
    linked_objects = []
    run = Run(linked_objects)

    text_obj = Text("direct text")
    run.add(text_obj)

    assert text_obj in run._linked_objects


def test_run_empty():
    linked_objects = []
    run = Run(linked_objects)
    assert run.linked_objects == []


def test_run_with_only_breaks():
    linked_objects = []
    run = Run(linked_objects)

    run.add_page_break()
    run.add_column_break()
    run.add_page_break()

    assert len(run.linked_objects) == 3
    assert all(isinstance(child, Break) for child in run.linked_objects)
    assert run.linked_objects[0].type == "page"
    assert run.linked_objects[1].type == "column"
    assert run.linked_objects[2].type == "page"


def test_add_text_with_special_characters():
    run = Run()
    special_text = "Text with <>&\"' symbols"
    run.add_text(special_text)

    assert len(run.linked_objects) == 1
    text_child = run.linked_objects[0]
    assert text_child.text == special_text


def test_run_with_real_linked_objects():
    linked_objects = LinkedObjects(Run())
    run = Run(linked_objects)
    assert run._linked_objects is linked_objects


def test_add_method_works():
    linked_objects = []
    run = Run(linked_objects)
    run.linked_objects = []
    text = Text("test")
    run.add(text)

    assert text in run._linked_objects
    assert len(run.linked_objects) == 1
