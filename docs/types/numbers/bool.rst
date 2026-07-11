Boolean values
==============

Boolean values are integers in Python:

.. code-block:: pycon

   >>> issubclass(bool, int)
   True

.. include:: ../../oop/types.rst
   :start-after: start-issubclass
   :end-before: end-issubclass

``True`` behaves like a ``1`` and ``False`` like a ``0``. There are, in fact,
certain situations in which this is very useful.

The functions :py:func:`any` and :py:func:`all` check whether at least one or
all elements in an iterable satisfy the respective condition:

.. code-block:: pycon

   >>> numbers = [0, 1, -1, 2, 3]
   >>> any(n > 0 for n in numbers)
   True
   >>> any(n < 0 for n in numbers)
   True
   >>> all(n > 0 for n in numbers)
   False
   >>> all(n < 0 for n in numbers)
   False

However, neither ``any`` nor ``all`` can tell you how many elements match. To
count the number of matches, you can use :py:func:`sum` instead:

.. code-block:: pycon

   >>> sum(n > 0 for n in numbers)
   3

This involves counting the number of ``True`` values by adding together ``True``
and ``False``.

Checks
------

* Decide whether the following statements are true or false:

  * ``1``
  * ``0``
  * ``-1``
  * ``[0]``
  * ``[]``
  * ``1 and 0``
  * ``1 > 0 or []``
