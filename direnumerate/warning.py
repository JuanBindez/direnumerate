import functools
import warnings

def deprecated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn("The function '{}' is deprecated and will be removed in future versions.".format(func.__name__), category=DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)
    return wrapper