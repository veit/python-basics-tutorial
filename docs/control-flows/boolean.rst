Boolean values and expressions
==============================

In Python, there are several ways to express Boolean values; the Boolean
constant ``False``, ``0``, the Python value ``None``, and empty values (for
example, the empty list ``[]`` or the empty string ``""``) are all considered
``False``. The Boolean constant ``True`` and everything else is considered
``True``.

You can create comparison expressions by using the comparison operators (``<``,
``<=``, ``==``, ``>``, ``>=``, ``!=``, ``is``, ``is not``, ``in``, ``not in``)
and the logical operators (``and``, ``not``, ``or``) , which all return ``True``
or ``False``:

.. code-block:: python

    >>> x = 5
    >>> y = 3
    >>> z = [3, 4, 5]
    >>> x is y
    False
    >>> x is not y
    True
    >>> x in z
    True
