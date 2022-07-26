Loops
=====

``while`` loop
--------------

The ``while`` loop is executed as long as the condition (here: ``x > y``) is
true:

.. code-block:: python
    :linenos:

    >>> x, y = 6, 3
    >>> while x > y:
    ...     x -= 1
    ...     if x == 4:
    ...         break
    ...     print(x)
    ... 
    5

Line 1
    This is a shorthand notation where ``x`` is given the value ``6`` and ``y``
    is given the value ``3``.
Lines 2–10
    This is the ``while`` loop with the statement ``x > y``, which is true as
    long as ``x`` is greater than ``y``.
Line 3
    ``x`` is reduced by ``1``.
Line 4
    ``if`` condition where ``x`` is to be exactly ``4``.
Line 5
    ``break`` ends the loop.
Lines 8 and 9
    outputs the results of the ``while`` loop before execution was interrupted
    with ``break``.

.. code-block:: python
    :linenos:

    >>> x, y = 6, 3
    >>> while x > y:
    ...     x -= 1
    ...     if x == 4:
    ...         continue
    ...     print(x)
    ... 
    5
    3

Line 5
    ``continue`` terminates the current iteration of the loop.

.. _for-loop:

``for`` loop
------------

The ``for`` loop is simple but powerful because it can iterate over any iterable
type, such as a list or a tuple. Unlike many other languages, the ``for`` loop
in Python iterates over every element in a sequence for example a :doc:`list
<../types/lists>` or a :doc:`tuple <../types/tuples>`), which makes it more like
a foreach loop. The following loop finds the first occurrence of an integer that
is divisible by ``5``:

.. code-block:: python
    :linenos:

    >>> items = [1, "fünf", 5.0, 10, 11, 15]
    >>> d = 5
    >>> for i in items:
    ...     if not isinstance(i, int):
    ...         continue
    ...     if not i % d:
    ...         print(f"First integer found that is divisible by {d}: {i}")
    ...         break
    ... 
    First integer found that is divisible by 5: 10

``x`` is assigned each value in the list in turn. If ``x`` is not an integer,
the remainder of this iteration is aborted by the ``continue`` statement. The
flow control is continued with ``x`` being set to the next entry in the list.
After the first matching integer is found, the loop is terminated with the
``break`` statement.
