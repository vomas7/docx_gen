def annotation_catcher(*expected_args, **expected_kwargs):
    """
    Decorator that wraps function arguments into a unified object for attribute-style access.

    Transforms all function arguments (positional and keyword) into attributes of a single
    object, providing consistent access regardless of how arguments were passed.

    Args:
        *expected_args: Names for expected positional arguments
        **expected_kwargs: Optional parameters with default values (name=default_value)

    Returns:
        Decorated function that receives an arguments object as its first parameter.

    The decorated function should accept one parameter - the arguments object.
    All original arguments become accessible as attributes of this object.

    Examples:
        >>> @annotation_catcher('name', 'age', city='Unknown')
        ... def greet_user(args):
        ...     print(f"Hello {args.name}, age {args.age} from {args.city}")
        ...     # Access additional kwargs if provided
        ...     if hasattr(args, 'country'):
        ...         print(f"Country: {args.country}")

        >>> # Different calling styles work:
        >>> greet_user('John', 25)
        >>> greet_user('John', 25, city='London', country='UK')
        >>> greet_user(name='Alice', age=30, city='Paris')

    Note:
        No argument validation is performed - all arguments are accepted and wrapped.
        Use additional validation decorators if argument checking is needed.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):

            class FuncArguments:
                def __init__(self):
                    self._args = args
                    self._kwargs = kwargs

                    for key, default_val in expected_kwargs.items():
                        setattr(self, key, default_val)

                    for i, arg_name in enumerate(expected_args):
                        if i < len(args):
                            setattr(self, arg_name, args[i])
                        elif arg_name in kwargs:
                            setattr(self, arg_name, kwargs[arg_name])
                        else:
                            setattr(self, arg_name, None)

                    for key, value in kwargs.items():
                        setattr(self, key, value)

                def __getattr__(self, name):
                    if name in self._kwargs:
                        return self._kwargs[name]
                    raise AttributeError(f"Argument '{name}' not found")

            arguments = FuncArguments()
            return func(arguments)

        return wrapper

    return decorator
