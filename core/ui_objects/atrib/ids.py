from core.ui_objects.base.base_attribute import SimpleAttribute



class AnchorId(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp14:anchorId")

class EditId(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp14:editId")