from core.exceptions.validation import ValidationError
from core.utils.annotaions import annotation_catcher


@annotation_catcher('val', 'access_vals')
def validate_access_type(args):
    if not isinstance(args.val, tuple(args.access_vals)):
        raise ValidationError(
            f"Element '{args.val}' not allowed! Valid are: {args.access_vals}"
        )


@annotation_catcher('markup_obj', 'access_vals')
def validate_access_markup(args):
    # if object doesn't have at least one constraint
    if len(args.access_vals) == 0:
        return

    if set([args.markup_obj.tag]) - set(args.access_vals):
        raise ValidationError(
            f"tag '{args.markup_obj.tag}' not"
            f" allowed! Valid are: {args.access_vals}"
        )
