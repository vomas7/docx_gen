from core.exceptions.validation import ValidationError
from core.utils.annotaions import annotation_catcher


@annotation_catcher('val', 'access_val')
def validate_access_elem(args):
    if not isinstance(args.val, tuple(args.access_val)):
        raise ValidationError(
            f"Element '{args.val}' not allowed! Valid are: {args.access_val}"
        )
