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


if __name__ == "__main__":
    print(example.__name__)
    print(example.__doc__)
