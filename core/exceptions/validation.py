# in future would add global exception for this project

class ValidationError(Exception):
    """Validation Error"""


class ValidationAccessError(ValidationError):
    """Validation Access Error"""
    def __init__(self,
                 value,
                 container_type=list,
                 additional_info=None):

        message = (f"Elements '{value}' not allowed into {container_type}")
        if additional_info:
            message += f" ({additional_info})"

        super().__init__(message)



class ValidationRequireError(ValidationError):
    """Validation Require Error"""

    def __init__(self,
                 value=None,
                 operation=None,
                 container_type=list,
                 additional_info=None):
        if operation is None:
            message = (f"Elements '{value}' is requred for {container_type}")
        else:
            message = (f"Operation '{operation}' not allowed for "
                       f"element '{value}' into {container_type}")
        if additional_info:
            message += f" ({additional_info})"

        super().__init__(message)
