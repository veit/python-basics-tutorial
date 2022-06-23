Functions
=========

Basic function definitions
--------------------------

The basic syntax for a Python function definition is

.. code-block:: python

    def function_name(param1, param2, ...):
        body

As with :doc:`control streams </control-flows/index>`, Python uses indentation
to separate the function from the function definition. The following simple
example inserts the code into a function so that you can call it to get the
`factorial <https://en.wikipedia.org/wiki/Factorial>`_ of a number:

.. code-block:: python
   :linenos:

    >>> def fact(n):
    ...     """Return the factorial of the given number."""
    ...     f = 1
    ...     while n > 0:
    ...         f = f * n
    ...         n = n - 1
    ...     return f

Line 2
    This is an optional documentation string, or ``docstring``. You can get its
    value by calling ``fact.__doc__``. The purpose of docstrings is to describe
    the behaviour of a function and the parameters it takes, while comments are
    to document internal information about how the code works. Docstrings are
    :doc:`/types/strings` that immediately follow the first line of a function
    definition and are usually enclosed in triple quotes to allow for multi-line
    descriptions. For multi-line documentation strings, it is common to give a
    summary of the function on the first line, follow this summary with an empty
    line and end with the rest of the information.

    .. seealso::
        * :ref:`napoleon`

Line 7
    The value is returned after the function is called. You can also write
    functions that have no return statement and return :doc:`/types/none`, and
    when ``return arg`` is executed, the value ``arg`` is returned.

Although all Python functions return values, it is up to you how the return
value of a function is used:

.. code-block:: python
   :linenos:

    >>> fact(3)
    6
    >>> x = fact(3)
    >>> x
    6

Line 1
    The return value is not linked to a variable.
Line 2
    The value of the ``fact`` function is only output in the interpreter.
Line 3
    The return value is linked to the variable ``x``.

.. toctree::
   :titlesonly:
   :hidden:

   params
   variables
   decorators
