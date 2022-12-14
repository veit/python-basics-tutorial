Variables and expressions
=========================

Variables
---------

The most commonly used command in Python is assignment. The Python code to
create a Vairiable called ``x`` that is to be given the value ``π`` is:

.. code-block:: python

    >>> x = 3.14159

In Python, unlike many other programming languages, neither a variable
declaration nor an end-of-line delimiter is necessary. The line is terminated by
the end of the line. Variables are created automatically when they are assigned
for the first time.

.. note::
   In Python, variables are labels that refer to objects. Any number of labels
   can refer to the same object, and if that object changes, so does the value
   to which all those variables refer. To better understand what this means, see
   the following example:

   .. code-block:: python

      >>> x = [1, 2, 3]
      >>> y = x
      >>> y[0] = 4
      >>> print(x)
      [4, 2, 3]

   However, variables can also refer to constants:

   .. code-block:: python

      >>> x = 1
      >>> y = x
      >>> z = y
      >>> y = 4
      >>> print(x,y,z)
      1 4 1

   In this case, after the third line, ``x``, ``y`` and ``z`` all refer to the
   same immutable integer object with the value ``1``. The next line, ``y = 4``,
   causes ``y`` to refer to the integer object ``4``, but this does not change
   the references of ``x`` or ``z``.

Python variables can be set to any object, whereas in many other languages
variables can only be stored in the declared type.

Variable names are case-sensitive and can contain any alphanumeric character as
well as underscores, but must begin with a letter or underscore.

Expressions
-----------

Python supports arithmetic and similar expressions. The following code
calculates the average of ``x`` and ``y`` and stores the result in the variable
``z``:

.. code-block:: python

    >>> x = 1
    >>> y = 2
    >>> z = (x + y) / 2

.. note::
   Arithmetic operators that use only integers do not always return an integer.
   As of Python 3, division returns a floating point number. If you want the
   traditional integer division to return an integer, you can use ``//``
   instead.
