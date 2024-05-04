``if``-``elif``-``else`` statement
==================================

The code block after the first true condition of an ``if`` or ``elif`` statement
is executed. If none of the conditions are true, the code block after the
``else`` is executed:

.. code-block:: pycon
    :linenos:

    >>> x = 1
    >>> if x < 1:
    ...     x = 2
    ...     y = 3
    ... elif x > 1:
    ...     x = 4
    ...     y = 5
    ... else:
    ...     x = 6
    ...     y = 7
    ...
    >>> print(x, y)
    6 7

Lines 5 and 8
    The ``elif`` and ``else`` clauses are optional, and there can be any number
    of ``elif`` clauses.
Lines 3, 4, 6, 7, 9 and 10
    Python uses indentations to delimit blocks. No explicit delimiters such as
    brackets or curly braces are required. Each block consists of one or more
    statements separated by line breaks. All these statements must be on the
    same indentation level.
