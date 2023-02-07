Functions
=========

Python offers flexible mechanisms for passing arguments to functions:

.. code-block:: python
    :linenos:

    >>> x, y = 2, 3
    >>> def func1(u, v, w):
    ...     value = u + 2*v + w**2
    ...     if value > 0:
    ...         return u + 2*v + w**2
    ...     else:
    ...         return 0
    ...
    >>> func1(x, y, 2)
    12
    >>> func1(x, w=y, v=2)
    15
    >>> def func2(u, v=1, w=1):
    ...     return u + 4 * v + w ** 2
    ...
    >>> func2(5, w=6)
    45
    >>> def func3(u, v=1, w=1, *tup):
    ...     print((u, v, w) + tup)
    ...
    >>> func3(7)
    (7, 1, 1)
    >>> func3(7, 8, 9)
    (7, 8, 9)
    >>> def func4(u, v=1, w=1, **kwargs):
    ...     print(u, v, w, kwargs)
    ...
    >>> func4(1, 2, s=4, t=5, w=3)
    1 2 3 {'s': 4, 't': 5}

Line 2
    Functions are defined with the ``def`` statement.
Line 5
    The ``return`` statement is used by a function to return a value. This value
    can be of any type. If no ``return`` statement is found, the value ``None``
    is returned by Python.
Line 11
    Function arguments can be entered either by position or by name (keyword).
    ``z`` and ``y`` are specified by name in our example.
Line 13
    Function parameters can be defined with default values that will be used if
    a function call omits them.
Line 18
    A special parameter can be defined that combines all additional positional
    arguments in a function call into one tuple.
Zeile 25
    Similarly, a special parameter can be defined that summarises all additional
    keyword arguments in a function call in a dictionary.
