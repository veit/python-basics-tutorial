Variables
=========

Local, non-local and global variables
-------------------------------------

Here you return to the definition of ``fact`` from the beginning of this
chapter:

.. code-block:: python

    >>> def fact(n):
    ...     """Return the factorial of the given number."""
    ...     f = 1
    ...     while n > 0:
    ...         f = f * n
    ...         n = n - 1
    ...     return f

Both the variables ``f`` and ``n`` are local to a particular call to the
function ``fact``; changes made to them during the execution of the function
have no effect on variables outside the function. All variables in the parameter
list of a function and all variables created within a function by an assignment,
such as ``f = 1``, are local to the function.

You can explicitly make a variable a global variable by declaring it with the
``global`` statement before it is used. Global variables can be accessed and
changed by the function. They exist outside the function and can also be
accessed and changed by other functions that declare them as global, or by code
that is not inside a function. Here is an example that illustrates the
difference between local and global variables:

.. code-block:: python

    >>> def my_func():
    ...     global x
    ...     x = 1
    ...     y = 2

.. code-block:: python

    >>> x = 3
    >>> y = 4
    >>> my_func()
    >>> x
    1
    >>> y
    4

In this example, a function is defined that treats ``x`` as a global variable
and ``y`` as a local variable, and attempts to change both ``x`` and ``y``. The
assignment to ``x`` within ``my_func`` is an assignment to the global variable
``x``, which also exists outside ``my_func``. Since ``x`` is designated as
global in ``my_func``, the assignment changes this global variable so that it
retains the value ``1`` instead of the value ``3``. However, the same is not
true for ``y``; the local variable ``y`` inside ``my_func`` initially refers to
the same value as the variable ``y`` outside ``my_func``, but the assignment
causes ``y`` to refer to a new value that is local to the ``my_func`` function.

.. seealso::

    * :ref:`python3:global`

While ``global`` is used for a top-level variable, ``nonlocal`` refers to any
variable in an enclosing area.

.. seealso::

    * :ref:`python3:nonlocal`
    * `PEP 3104 – Access to Names in Outer Scopes
      <https://peps.python.org/pep-3104/>`_
