Exceptions
==========

This section is about exceptions, that is, language functions that specifically
handle unusual circumstances during the execution of a programme. The most
common exception is to handle errors, but they can also be used effectively for
many other purposes. Python provides a comprehensive set of exceptions, and you can define new exceptions for your own purposes.

The entire exception mechanism in Python is object-oriented: An exception is an
object that is automatically created by Python functions with a ``raise``
statement. This ``raise`` statement causes the Python programme to be executed
in a different way than usually intended: The current call chain is searched for
a handler that can handle the generated exception. If such a handler is found,
it is called and can access the exception object to obtain further information.
If no suitable exception handler is found, the programme terminates with an
error message.

.. note::
   The way Python handles error situations in general differs from some other
   languages, for example Java. These languages check possible errors as far as
   possible before they occur, as handling exceptions after they occur is
   costly. This is sometimes referred to as the :abbr:`LBYL (Look before you
   leap)` approach.

   Python, on the other hand, relies more on exceptions to handle errors after
   they occur. Although this reliance may seem risky, when exceptions are used
   correctly, the code is less cumbersome and easier to read, and errors are
   only handled when they occur. This Pythonic approach to error handling is
   often described as `EAFP (Easier to ask forgiveness than permission)`.

It is possible to create different types of exceptions to reflect the actual
cause of the reported error or unusual circumstance. For an overview of the
class hierarchy of built-in exceptions, see `Exception hierarchy
<https://docs.python.org/3/library/exceptions.html#exception-hierarchy>`_ in the
Python documentation. Each exception type is a Python class that inherits from
its parent exception type. For example, a ``ZeroDivisionError`` is also an
``ArithmeticError``, an ``Exception`` and also a ``BaseException`` by
inheritance. This hierarchy is intentional: most exceptions inherit from
``Exception``, and it is strongly recommended that all user-defined exceptions
also subclass ``Exception``, and not ``BaseException``:

.. literalinclude:: exceptions.py
   :language: python
   :lines: 1-2

This defines your own exception type, which inherits from the ``Exception`` base
type.

.. literalinclude:: exceptions.py
   :language: python
   :lines: 5

A list of different file types is defined.

Finally, exceptions or errors are caught and handled using the compound
statement ``try``-``except``-``else``-``finally``. Any exception that is not
caught will cause the programme to terminate.

.. literalinclude:: exceptions.py
   :language: python
   :linenos:
   :lines: 7-
   :lineno-start: 7

Line 7
    If an ``IOError`` or ``EmptyFileError`` occurs during the execution of the
    instructions in the ``try`` block, the corresponding ``except`` block is
    executed.
Line 9
    An ``IOError`` could be triggered here.
Line 12
    Here you trigger the ``EmptyFileError``.
Line 17
    The ``else`` clause is optional; it is executed if no exception occurs in
    the ``try`` block.

    .. note::
       In this example, ``continue`` statements could have been used in the
       ``except`` blocks instead.

Line 19
    The ``finally`` clause is optional; it is executed at the end of the block,
    regardless of whether an exception was thrown or not.

Checks
------

* Write code that receives two numbers and divides the first number by the
  second. Check if the :class:`python3:ZeroDivisionError` occurs when the second
  number is ``0`` and catch it.

* If :class:`MyError` inherits from :class:`Exception`, what is the difference
  between ``except Exception as e`` and ``except MyError as e``?

  The first catches every exception that inherits from :class:`Exception`, while
  the second only catches :class:`MyError` exceptions.

* Write a simple program that receives a number and then uses the :func:`assert`
  statement to throw an :class:`python3:Exception` if the number is ``0``.

* Schreibt eine benutzerdefinierte Ausnahme :class:`Outliers`, die eine
  :class:`Exception` auslöst, wenn die Variable ``x`` größer oder kleiner als
  ``3`` ist?

* Is checking whether an object is a list (:ref:`Check: Listen <check-list>`)
  programming in the style of :abbr:`LBYL (look before you leap)` or
  :abbr:`EAFP (easier to ask forgiveness than permission)`?
