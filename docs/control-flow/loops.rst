Loops
=====

``while`` loop
--------------

The ``while`` loop is executed as long as the condition (here: ``x > y``) is
true:

.. code-block:: pycon
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

.. code-block:: pycon
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
<../types/sequences-sets/lists>` or a :doc:`tuple
<../types/sequences-sets/tuples>`), which makes it more like a foreach loop. The
following loop uses the `Modulo
<https://en.wikipedia.org/wiki/Modulo_operation>`_ operator ``%`` as a condition
for the first occurrence of an integer divisible by ``5``:

.. code-block:: pycon
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

Loops with an index
-------------------

You can also output the index in a ``for`` loop, for example with
:py:func:`enumerate()`:

.. code-block:: pycon

   >>> data_types = ["Data types", "Numbers", "Lists"]
   >>> for index, title in enumerate(data_types):
   ...     print(index, title)
   ...
   0 Data types
   1 Numbers
   2 Lists

List Comprehensions
-------------------

A list is usually generated as follows:

.. code-block:: pycon

   >>> squares = []
   >>> for i in range(8):
   ...     squares.append(i**2)
   ...
   >>> squares
   [0, 1, 4, 9, 16, 25, 36, 49]

Instead of creating an empty list and inserting each element at the end, with
list comprehensions you simply define the list and its content at the same time
with just a single line of code:

.. code-block:: pycon

   >>> squares = [i**2 for i in range(8)]
   >>> squares
   [0, 1, 4, 9, 16, 25, 36, 49]

The general format for this is:

:samp:`{NEW_LIST} = [{EXPRESSION} for {MEMBER} in {ITERABLE}]`

Each list comprehension in Python contains three elements:

:samp:`{EXPRESSION}`
    is a call to a method or another valid expression that returns a value. In
    the example above, the expression ``i ** 2`` is the square of the
    respective member value.
:samp:`{MEMBER}`
    is the object or the value in an :samp:`{ITERABLE}`. In the example above,
    the value is ``i``.
:samp:`{ITERABLE}`
    is a :doc:`list <../types/sequences-sets/lists>`, a :doc:`set
    <../types/sequences-sets/sets>`, a generator or another object that can
    return its elements individually. In the example above, the iterable is
    ``range(8)``.

You can also use optional conditions with list comprehensions, which are usually
appended to the end of the expression:

.. code-block:: pycon

   >>> squares = [i**2 for i in range(8) if i >= 4]
   >>> squares
   [16, 25, 36, 49]

Checks
------

* Removes all negative numbers from the list ``x = [ -2, -1, 0, 1, 2, 3]``.

* Which list comprehension would you use to achieve the same result?

* How would you count the total number of negative numbers in the list ``[[-1,
  0, 1], [-1, 1, 3], [-2, 0, 2]]``?

* Creates a generator that only returns odd numbers from 1 to 10.

  .. tip::
     A number is odd if there is a remainder when it is divided by 2, in other
     words if ``% 2`` is true.

* Write a :doc:`dict </types/dicts>` with the edge lengths and volumes of cubes.
