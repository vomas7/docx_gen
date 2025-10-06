class BaseDOC:

    def __init__(self):
        self.parent = None
        self._linked_objects = []

    @staticmethod
    def validate_annotation(obj, **kwargs):
        """
            args:
                obj: class instance
                **kwargs: key-value pairs for checking received arguments
        """
        # todo не обрабатываает генерики

        if not kwargs:
            raise ValueError("arguments are required")
        annotation = obj.__init__.__annotations__

        for key, value in kwargs.items():
            if key not in annotation:
                continue

            if not isinstance(value, annotation[key]):
                raise AttributeError(
                    f"Creating {obj} object failed: "
                    f"Unknown source {type(value)}!"
                )


#todo добавить разделение на объекты, которые хранят элементы и не хранят