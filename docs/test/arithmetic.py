def add(x, y):
    """
    >>> add(7,6)
    13
    """
    return x + y


def divide(x, y):
    """Divides the first parameter by the second
    >>> x, y, z = 7, -6.0, 0
    >>> divide(x, y)
    -1.1666666666666667
    >>> divide(x, z)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero
    """
    return x / y


def multiply(x, y):
    """
    >>> multiply(7,6)
    42
    """
    return x * y


def subtract(x, y):
    """
    >>> subtract(7,6)
    1
    """
    return x - y


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
