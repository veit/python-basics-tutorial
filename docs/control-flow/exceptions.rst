Exceptions
==========

This section deals with :term:`exceptions <exception>`, which are language
functions that specifically handle unusual circumstances during the execution of
a programme. The most common exception is error handling, but they can also be
used effectively for many other purposes. Python provides a comprehensive set of
exceptions, and you can define new exceptions for your own purposes.

An exception is an object that is automatically created by Python functions with
a :ref:`raise <python3:raise>` statement, for example with:

.. literalinclude:: exceptions.py
   :language: python
   :linenos:
   :lines: 11-12
   :lineno-start: 11

The :ref:`raise <python3:raise>` statement causes the Python programme to be
executed in a different way than is usually intended: The current call chain is
searched for a handler that can handle the generated exception. If such a
handler is found, it is called and can access the exception object to obtain
further information, as in our :class:`EmptyFileError` example:

.. literalinclude:: exceptions.py
   :language: python
   :linenos:
   :lines: 1-2

This defines your own exception type, which inherits from the ``Exception`` base
type.

You can find an overview of the class hierarchy of built-in exceptions at
`Exception hierarchy
<https://docs.python.org/3/library/exceptions.html#exception-hierarchy>`_ in the
Python documentation. Each exception type is a Python class that inherits from
its parent exception type. For example, a ``ZeroDivisionError`` is also an
``ArithmeticError``, an ``Exception`` and also a ``BaseException`` by
inheritance. This hierarchy is intentional: most exceptions inherit from
``Exception``, and it is strongly recommended that all user-defined exceptions
also subclass ``Exception`` and not ``BaseException``:

It is possible to create different types of exceptions to reflect the actual
cause of the reported error or exceptional circumstance.

.. literalinclude:: exceptions.py
   :language: python
   :linenos:
   :lines: 8-16
   :lineno-start: 8

If an ``OSError`` or an ``EmptyFileError`` occurs in the ``try`` block during
the execution of :func:`open`, the corresponding ``except`` block is executed.

If no suitable exception handler is found, the programme terminates with an
error message. We therefore add ``else`` and ``finally`` to our
``try``-``except`` statements:

.. literalinclude:: exceptions.py
   :language: python
   :linenos:
   :lines: 17-21
   :lineno-start: 17

Now we can define a list of different file types so that our complete code looks
like this:

.. literalinclude:: exceptions.py
   :language: python
   :linenos:
   :lines: 1-
   :lineno-start: 1

Line 7
    If an ``OSError`` or ``EmptyFileError`` occurs during the execution of the
    statements in the ``try`` block, the corresponding ``except`` block is
    executed.
Line 9
    An ``OSError`` could be triggered here.
Line 12
    Here you trigger the ``EmptyFileError``.
Line 17
    The ``else`` clause is optional; it is executed if no exception occurs in
    the ``try`` block.
Line 19
    The ``finally`` clause is also optional and is executed at the end of the
    block, regardless of whether an exception was triggered or not.

.. note::
   The way Python handles error situations in general differs from some other
   languages, such as Java. These languages check possible errors as far as
   possible before they occur, as handling exceptions after they occur is
   costly. This is sometimes referred to as the :term:`LBYL` approach.

   Python, on the other hand, relies more on exceptions to handle errors after
   they occur. Although this reliance may seem risky, when exceptions are used
   correctly, the code is less cumbersome and easier to read, and errors are
   only handled when they occur. This Pythonic approach to error handling is
   often described as :term:`EAFP`.

Checks
------

* Write code that receives two numbers and divides the first number by the
  second. Check if the :class:`python3:ZeroDivisionError` occurs when the second
  number is ``0`` and catch it.

* If :class:`MyError` inherits from :class:`Exception`, what is the difference
  between ``except Exception as e`` and ``except MyError as e``?

* Write a simple program that receives a number and then uses the :func:`assert`
  statement to throw an :class:`exception <python3:Exception>` if the number is
  ``0``.

* Writes a user-defined exception :class:`Outliers` that throws an exception if
  the variable ``x`` is greater or less than ``3``?

* Is the check whether an object is a list (:ref:`Check: list <check-list>`)
  programming in the style of :term:`LBYL` or :term:`EAFP`?
