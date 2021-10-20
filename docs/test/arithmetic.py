def add(x, y):
    """
    >>> add(7,6)
    13
    """
    return x + y

def divide(x, y):
    """
    >>> divide(42,7)
    6.0
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
