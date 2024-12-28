Conditional statements
======================

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
   >>> x, y
   (6, 7)

Python uses indentations to delimit blocks. No explicit delimiters such as
brackets or curly braces are required. Each block consists of one or more
statements separated by line breaks. All these statements must be at the same
indentation level.

Line 5
    The ``elif`` statement looks like the ``if`` statement and works in the same
    way, but with two important differences:

    * ``elif`` is only allowed after an ``if`` statement or another ``elif``
      statement
    * you can use as many ``elif`` statements as you need

Line 8
    The optional ``else`` clause denotes a code block that is only executed if
    the other conditional blocks, ``if`` and ``elif``, are all false.
