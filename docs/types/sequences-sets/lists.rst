Lists
=====

A list in Python is similar to an array in Java or C: an ordered collection of
objects. However, unlike lists in many other languages, Python lists can contain
different types of elements; a list element can be any Python object, including
:doc:`../strings/index`, :doc:`tuples`, :doc:`lists`, :doc:`../dicts`,
:doc:`../../functions/index`, :doc:`../../save-data/files` and any kind of
:doc:`../numbers/index`. You create a list by enclosing no elements or elements
separated by commas in square brackets, like this:

.. code-block:: python
   :linenos:

    []
    [1]
    [1, "2.", 3.0, ["4a", "4b"], (5.1, 5.2)]

.. tip::
   I recommend that you do **not** use the :class:`python3:ctypes.Array` type
   available in Python, but if numerical calculations require it, consider
   :doc:`Python4DataScience:workspace/numpy/index`, which is described in our
   :doc:`Python4DataScience:index` tutorial.

Indices
-------

Elements can be extracted from a Python list using a notation similar to array
indexing in C, starting with ``0``; asking for element ``0`` will return the
first element of the list, asking for element ``1`` will return the second
element, and so on. Here are a few examples:

.. code-block:: pycon
   :linenos:

   >>> x = [1, "2.", 3.0, ["4a", "4b"], (5.1, 5.2)]
   >>> x[0]
   '1'
   >>> x[1]
   '2.'

A list can be indexed from the front or the back. You can also refer to a
sub-segment of a list by using the slice notation:

.. code-block:: pycon
   :lineno-start: 6

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

Slices also allow a step-by-step selection between the start and end indices.
The default value for an unspecified stride is ``1``, which takes every element
from a sequence between the indices. With a stride of ``2``, every second
element is taken and so on:

.. code-block:: pycon
   :linenos:

   >>> x[0:3:2]
   [1, [3.1, 3.2, 3.3]]
   >>> x[::2]
   [1, [3.1, 3.2, 3.3]]
   >>> x[1::2]
   ['secondly', (5.1, 5.2)]

The stride value can also be negative. A ``-1`` stride means counting from right
to left:

.. code-block:: pycon
   :linenos:

   >>> x[3:0:-2]
   [(5.1, 5.2), 'secondly']
   >>> x[::-2]
   [(5.1, 5.2), 'secondly']
   >>> x[::-1]
   [(5.1, 5.2), [3.1, 3.2, 3.3], 'secondly', 1]

Line 1
    To use a negative increment, the start slice should be larger than the end
    slice.
Line 3
    The exception is if you omit the start and end indices.
Line 5
    A stride of ``-1`` reverses the order.

    .. tip::
       To reverse the order, however, :func:`list.reverse` should be easier to
       read than a stride of  ``-1``, see also :ref:`list.reverse() <reverse>`.

.. seealso::
   * :doc:`Select and filter data with pandas
     <Python4DataScience:workspace/pandas/select-filter>`

Changing lists
--------------

You can use this notation to add, remove and replace elements in a list or to
get an element or a new list that is a slice of it, for example:

.. code-block:: pycon
   :linenos:

   >>> x = [1, "2.", 3.0, ["4a", "4b"], (5.1, 5.2)]
   >>> x[1] = "secondly"
   >>> x
   [1, 'secondly', 3.0, ['4a', '4b'], (5.1, 5.2)]
   >>> x[5:] = [6, 7]
   >>> x
   [1, 'secondly', 3.0, ['4a', '4b'], (5.1, 5.2), 6, 7]
   >>> x[:0] = [-1, 0]
   >>> x
   [-1, 0, 1, 'secondly', 3.0, ['4a', '4b'], (5.1, 5.2), 6, 7]
   >>> x[2:3] = []
   >>> x
   [-1, 0, 'secondly', 3.0, ['4a', '4b'], (5.1, 5.2), 6, 7]

Line 2
    replaces the second element of the list.
Line 5
    adds elements at the end of the list.
Line 8
    adds elements at the beginning of the list.
Line 11
    removes elements from the list.

Some functions of the slice notation can also be executed with special
operations, which improves the readability of the code:

.. _reverse:

.. code-block:: pycon
   :linenos:

   >>> x.reverse()
   >>> x
   [(5.1, 5.2), [3.1, 3.2, 3.3], 'secondly', 1]

You can also use the built-in functions (:func:`python3:len`, :func:`max` and
:func:`min`), some operators (:ref:`in, not in <python3:in>`, ``+`` and ``*``),
the ``del`` statement and the list methods (``append``, ``count``, ``extend``,
``index``, ``insert``, ``pop``, ``remove``, ``reverse``, :meth:`sort
<python3:list.sort>` and ``sum``) for lists:

.. code-block:: pycon
   :linenos:

   >>> len(x)
   4
   >>> x[len(x) :] = [0, -1]
   >>> x
   [(5.1, 5.2), [3.1, 3.2, 3.3], 'secondly', 1, 0, -1]
   >>> x.append(-2)
   >>> x
   [(5.1, 5.2), [3.1, 3.2, 3.3], 'secondly', 1, 0, -1, -2]
   >>> y = [-3, -4, -5]
   >>> x.append(y)
   >>> x
   [(5.1, 5.2), [3.1, 3.2, 3.3], 'secondly', 1, 0, -1, -2, [-3, -4, -5]]
   >>> x[7:8] = []
   >>> x
   [(5.1, 5.2), [3.1, 3.2, 3.3], 'secondly', 1, 0, -1, -2]
   >>> x.extend(y)
   >>> x
   [(5.1, 5.2), [3.1, 3.2, 3.3], 'secondly', 1, 0, -1, -2, -3, -4, -5]
   >>> x + [-6, -7]
   [(5.1, 5.2), [3.1, 3.2, 3.3], 'secondly', 1, 0, -1, -2, -3, -4, -5, -6, -7]
   >>> x.reverse()
   >>> x
   [-5, -4, -3, -2, -1, 0, 1, 'secondly', [3.1, 3.2, 3.3], (5.1, 5.2)]

Line 1
    shows the number of list elements.
Line 3
    appends a new list to the end of the list.
Line 6
    appends a new element to the end of the list with ``append``.
Line 10
    appends **not** the elements of the ``y`` list to the end of the list with
    ``append``, but the element ``y`` list.
Line 16
    appends the elements of the ``y`` list with ``extend``.
Line 19
    The operators ``+`` and ``*`` each create a new list, whereby the original
    list remains unchanged.
Line 21
    The methods of a list are called using the attribute notation for the list
    itself: :samp:`{LIST}.{METHOD}({ARGUMENTS})`.

List operations
---------------

Sorting lists
~~~~~~~~~~~~~

Lists can be sorted using the built-in Python sort method
:meth:`python3:list.sort`:

.. code-block:: pycon

   >>> x = [5, 3, -3, 3.1, 0, 1]
   >>> x.sort()
   >>> x
   [-3, 0, 1, 3, 3.1, 5]

With this method, sorting is performed on the spot, meaning that the list to be
sorted is changed. If you want the original list to remain unchanged, you have
two options:

#. You can use the built-in function :func:`python3:sorted`, which is described
   in more detail later.
#. You can create a copy of the list and sort the copy:

   .. code-block:: pycon

      >>> x = [5, 3, -3, 3.1, 0, 1]
      >>> y = x[:]
      >>> y.sort()
      >>> y
      [-3, 0, 1, 3, 3.1, 5]
      >>> x
      [5, 3, -3, 3.1, 0, 1]

Strings and lists of lists can also be sorted:

.. code-block:: pycon

   >>> hipy_list = ["Say", "hi", "to", "all", "Pythonistas", "!"]
   >>> hipy_list.sort()
   >>> hipy_list
   ['!', 'Pythonistas', 'Say', 'all', 'hi', 'to']
   >>> ll = [[5.1, 5.2], [4.0, 5.0], [4.0, 3.0], [3.3, 3.2, 3.1]]
   >>> ll.sort()
   >>> ll
   [[3.3, 3.2, 3.1], [4.0, 3.0], [4.0, 5.0], [5.1, 5.2]]

When comparing complex objects, the sub-lists are first sorted by the first
element and then by the second element in ascending order.

:meth:`python3:list.sort` can also sort in reverse order with ``reverse=True``.
A separate ``key`` function can also be used to determine how the elements of a
list are to be sorted.

However, the standard key method used by :meth:`python3:list.sort` requires that
all elements in the list are of comparable type. In a list that contains both
numbers and strings, an :term:`Exception` is therefore thrown:

.. code-block:: pycon

   >>> x
   [-5, -4, -3, -2, -1, 0, 1, 'secondly', [3.1, 3.2, 3.3], (5.1, 5.2)]
   >>> x.sort()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: '<' not supported between instances of 'str' and 'int'

User-defined sorting
::::::::::::::::::::

.. note::
   You must be able to define :doc:`../../functions/index` for user-defined
   sorting. The processing of :doc:`../strings/index` will also be covered in
   more detail later.

Python usually sorts words lexicographically – upper case before lower case.
However, we want to sort a list of words by the number of characters in each
word in ascending order instead:

.. code-block:: pycon

   >>> def ascending_number_chars(string):
   ...     return len(string)
   ...
   >>> hipy_list = ["Say", "hi", "to", "all", "Pythonistas", "!"]
   >>> new_list = hipy_list[:]
   >>> hipy_list.sort()
   >>> hipy_list
   ['!', 'Pythonistas', 'Say', 'all', 'hi', 'to']
   >>> new_list.sort(key=ascending_number_chars)
   >>> new_list
   ['!', 'hi', 'to', 'Say', 'all', 'Pythonistas']

The ``sorted`` function
:::::::::::::::::::::::

Lists have an inbuilt method for sorting themselves :meth:`python3:list.sort`.
However, other iterables in Python, such as the keys of :doc:`../dicts`, do not
have a sorting method. However, Python offers the built-in
:func:`python3:sorted` function for this purpose, which returns a sorted list
from any iterable. :func:`python3:sorted` uses the same
:doc:`../../functions/params` ``key`` and ``reverse`` as the
:meth:`python3:list.sort` method:

.. code-block:: pycon

   >>> x
   [5, 3, -3, 3.1, 0, 1]
   >>> y = sorted(x)
   >>> y
   [-3, 0, 1, 3, 3.1, 5]
   >>> z = sorted(x, reverse=True)
   >>> z
   [5, 3.1, 3, 1, 0, -3]

.. _list-in:

List membership
~~~~~~~~~~~~~~~

The :ref:`in and not in <python3:in>`, which return a Boolean value, make it
easy to check whether a value is contained in a list.

List concatenation
~~~~~~~~~~~~~~~~~~

The ``+`` operator can be used to create a list from two existing lists, whereby
the initial lists remain unchanged:

.. code-block:: pycon

   >>> x = [3, -3, 0, 1]
   >>> y = [3.1]
   >>> z = x + y
   >>> z
   [3, -3, 0, 1, 3.1]

List initialisation
~~~~~~~~~~~~~~~~~~~

You can use the ``*`` operator to create a list of a certain size and certain
values. This is a common method for working with lists whose size is known in
advance and which do not cause any memory reallocation overhead. You should
therefore prefer ``append`` in such cases in order to enlarge the list at the
start of the programme:

.. code-block:: pycon

   >>> x = [None] * 4
   >>> x
   [None, None, None, None]

The operator for ``list`` multiplications ``*`` repeats the copying of the
elements of a list the specified number and merges all copies into a new list. A
list with a single instance of :doc:`/types/none` is usually used for list
multiplication, but the list can be anything:

.. code-block:: pycon

   >>> initial_list = [[1, 2, 3, 4]]
   >>> arr = initial_list * 4
   >>> arr
   [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

Minimum or maximum of a list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use :func:`max` and :func:`min` to find the largest and smallest
element of a list. You will probably use :func:`max` and :func:`min` mainly for
:doc:`numeric </types/numbers/index>` lists, but you can also use them for lists
with arbitrary elements; however, if the comparison of these types does not make
sense, this will result in an error:

.. code-block:: pycon

   >>> x = [5, 3, -3, 3.1, 0, 1]
   >>> max(x)
   5
   >>> hipy_list = ["Say", "hi", "to", "all", "Pythonistas", "!"]
   >>> max(hipy_list)
   'to'
   >>> max(x + hipy_list)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: '>' not supported between instances of 'str' and 'int'

When comparing complex objects, the sub-lists are first analysed according to
the first element and then according to the second element (and so on).

.. code-block:: pycon

   >>> ll = [[1.0, 1.1], [1.0, 1.1, 1.2], [0.9, 1.3]]
   >>> max(ll)
   [1.0, 1.1, 1.2]

Search in a list
~~~~~~~~~~~~~~~~

If you want to know **where** a value can be found in a list, you can use the
``index`` method. It searches a list for a list element with a specific value
and returns the position of this list element:

.. code-block:: pycon
   :linenos:

   >>> x = [5, 3, 3.0, -3, 3.1, 0, 1]
   >>> x.index(3)
   1
   >>> x.index(3.0)
   1
   >>> x.index(5.0)
   0
   >>> x.index(6)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: 6 is not in list

Line 8–11
    Attempting to find the position of an element that is not in the list
    results in an error. This can be avoided by testing the list with the
    :ref:`in or not-in <list-in>` list operators before using ``index``.

Matches in lists
~~~~~~~~~~~~~~~~

``count`` also searches a list for a specific value, but returns the number of
occurrences in the list and not the position:

.. code-block:: pycon

   >>> x = [5, 3, 3.0, -3, 3.1, 0, 1]
   >>> x.count(3)
   2
   >>> x.count(5)
   1
   >>> x.count(6)
   0

Nested lists and ``deepcopy``
-----------------------------

Lists can be nested, for example to display two-dimensional matrices. The
elements of these matrices can be referenced using two-dimensional indices:

.. code-block:: pycon

   >>> ll = [[5.1, 5.2], [4.0, 5.0], [4.0, 3.0], [3.3, 3.2]]
   >>> ll[0]
   [5.1, 5.2]
   >>> ll[0][1]
   5.2

As expected, this mechanism can be transferred to more dimensions:

.. code-block:: pycon

   >>> sub = [0]
   >>> sup = [sub, 1]
   >>> sup
   [[0], 1]
   >>> sub[0] = 1
   >>> sup
   [[1], 1]
   >>> sup[0][0] = 2
   >>> sub
   [2]
   >>> sup
   [[2], 1]

However, if ``sub`` is set to a different list, the connection between ``sub``
and ``sup`` is interrupted:

.. code-block:: pycon

   >>> sub = [3]
   >>> sup
   [[2], 1]

You can get a copy of a list by creating a full slice (``x[:]``) or by using
``+`` or ``*`` (for example,  ``x + []`` or ``x * 1``). All three create a
so-called flat copy of the list, which is probably what you want in most cases.
However, if your list contains other lists that are nested within it, you may
want to create a deep copy. You can do this with the :func:`copy.deepcopy`
function of the :mod:`python3:copy` module:

.. code-block:: pycon

   >>> shallow = sup[:]
   >>> shallow
   [[2], 1]

The ``shallow`` copy does not copy the elements of the list but only refers to
the original elements. Changing one of these elements affects both ``shallow`` and ``sup``:

.. code-block:: pycon

   >>> shallow[1] = 2
   >>> shallow
   [[2], 2]
   >>> sup
   [[2], 1]
   >>> shallow[0][0] = 0
   >>> sup
   [[0], 1]

However, ``deepcopy`` is independent of the original list and no change to it
has any effect on the original list:

.. code-block:: pycon

   >>> import copy
   >>> deep = copy.deepcopy(sup)
   >>> deep
   [[0], 1]
   >>> deep[0][0] = 1
   >>> deep
   [[1], 1]
   >>> sup
   [[0], 1]

.. _check-list:

Checks
------

* What does :func:`len` return for each of the following cases:

  * ``[3]``
  * ``[]``
  * ``[[1, [2, 3], 4], "5 6"]``

* How would you use :func:`len` and slices to determine the second half of a
  list if you don’t know how long it is?

* How could you move the last two entries of a list to the beginning without
  changing the order of the two?

* Which of the following cases triggers an exception?

  * ``min(["1", "2", "3"])``
  * ``max([1, 2, "3"])``
  * ``[1,2,3].count("1")``

* If you have a list ``l``, how can you remove a certain value ``i`` from it?

* If you have a nested list ``ll``, how can you get a copy ``nll`` of this list
  in which you can change the elements without changing the contents of ``ll``?

* Make sure that the ``my_collection`` object is a list before you try to append
  data to it.
