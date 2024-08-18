from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        print("Call decorated function")
        return f(*args, **kwargs)

    return wrapper


@my_decorator
def example():
    """Example docstring"""
    print("Call example function")
