# in future would add global exception for this project

class ValidationError(Exception):
    def __init__(self, message=None, invalid_elem=None):
        self.element = invalid_elem

        if message is None:
            element_info = f" | {self.element} |" if self.element else ""
            message = f"Element{element_info} wasn't passed validation"

        super().__init__(message)

#todo допилить эксепшены/ мб сделать их проще

class ValidationAccessError(ValidationError):
    def __init__(self, message=None, invalid_elem=None, allowed_access=None):
        if not message:
            message = "Access denied for this elements"
            if allowed_access and invalid_elem:
                message = (f"{message}. Element(s): {invalid_elem} "
                           f"not in allowed: {allowed_access} ")
        super().__init__(message, invalid_elem)


class ValidationRequireError(ValidationError):
    def __init__(self, message=None, invalid_elem=None, missing=None):
        if not message:
            message = "The required element is missing"
            if invalid_elem is not None and missing is not None:
                message = (f"{message}: {missing} to the {invalid_elem}")
        super().__init__(message, invalid_elem)
