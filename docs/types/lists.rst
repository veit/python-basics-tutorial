Lists
=====

Python has a powerful built-in list type:

.. code-block:: python

    []
    [1]
    [1, "2.", 3.0, ["4a", "4b"], (5.1,5.2)]

A list can contain a mixture of other types as elements, including strings,
tuples, lists, dictionaries, functions, file objects and any kind of number.

A list can be indexed from the front or the back. You can also refer to a
sub-segment of a list using slice notation:

.. code-block:: python
   :linenos:

    >>> x = [1, "2.", 3.0, ["4a", "4b"], (5.1,5.2)]
    >>> x[0]
    '1'
    >>> x[1]
    '2.'
    >>> x[-1]
    (5.1, 5.2)
    >>> x[-2]
    ['4a', '4b']
    >>> x[1:-1]
    ['2.', 3.0, ['4a', '4b']]
    >>> x[0:3]
    [1, '2.', 3.0]
    >>> x[:3]
    [1, '2.', 3.0]
    >>> x[-4:-1]
    ['2.', 3.0, ['4a', '4b']]
    >>> x[-4:]
    ['2.', 3.0, ['4a', '4b'], (5.1, 5.2)]

Lines 2 and 4
    Index from the beginning using positive indices starting with ``0`` as the
    first element.
Lines 6 and 8
    Index from the back using negative indices starting with ``-1`` as the last
    element.
Lines 10 and 12
    Slice with ``[m:n]``, where ``m`` is the inclusive start point and ``n`` is
    the exclusive end point.
Lines 14, 16 and 18
    A ``[:n]`` slice starts at the beginning and an ``[m:]`` slice goes to the
    end of a list.

You can use this notation to add, remove and replace elements in a list or to
get an element or a new list that is a slice of it, for example:

.. code-block:: python
   :linenos:

    >>> x = [1, "2.", 3.0, ["4a", "4b"], (5.1,5.2)]
    >>> x[1] = "zweitens"
    >>> x[2:3] = []
    >>> x
    [1, 'zweitens', (5.1, 5.2)]
    >>> x[2] = [3.1, 3.2, 3.3]
    >>> x
    [1, 'zweitens', [3.1, 3.2, 3.3]]
    >>> x[2:]
    [[3.1, 3.2, 3.3]]

Line 3
    The size of the list increases or decreases if the new slice is larger or
    smaller than the slice it replaces.

Some built-in functions (``len``, ``max`` and ``min``), some operators (``in``,
``+`` and ``*``), the ``del`` statement and the list methods (``append``,
``count``, ``extend``, ``index``, ``insert``, ``pop``, ``remove``, ``reverse``
and ``sort``) work with lists:

.. code-block:: python
   :linenos:

    >>> x = [1, "2.", 3.0, ["4a", "4b"], (5.1,5.2)]
    >>> len(x)
    5
    >>> [-1, 0] + x
    [-1, 0, 1, '2.', 3.0, ['4a', '4b'], (5.1, 5.2)]
    >>> x.reverse()
    >>> x
    [(5.1, 5.2), ['4a', '4b'], 3.0, '2.', 1]

Line 4
    The operators ``+`` and ``*`` each create a new list, leaving the original
    list unchanged.
Line 6
    The methods of a list are called using the attribute notation for the list
    itself: ``x.METHOD(ARGUMENTS)``.

Some of these operations repeat functions that can be performed using slice
notation, but they improve the readability of the code.

Summary
-------

+---------------+---------------+---------------+---------------+---------------+
| data type     | mutable       | ordered       | indexed       | duplicates    |
+===============+===============+===============+===============+===============+
| list          | ✅            | ✅            | ✅            | ✅            |
+---------------+---------------+---------------+---------------+---------------+
