Variables
=========

.. _local_variables:

Local variables
---------------

Here you return to the definition of ``fact`` from the beginning of this
:doc:`index` chapter:

.. code-block:: python

   def fact(n):
       """Return the factorial of the given number."""
       f = 1
       while n > 0:
           f = f * n
           n = n - 1
       return f

Both the variables ``f`` and ``n`` are local to a particular call to the
function ``fact``; changes made to them during the execution of the function
have no effect on variables outside the function. All variables in the
:term:`parameter` list of a function and all variables created within a function
by an assignment, such as ``f = 1``, are local to the function:

.. code-block:: pycon

   >>> fact(3)
   6
   >>> f
   Traceback (most recent call last):
     File "<python-input-27>", line 1, in <module>
       f
   NameError: name 'f' is not defined
   >>> n
   Traceback (most recent call last):
     File "<python-input-28>", line 1, in <module>
       n
   NameError: name 'n' is not defined

.. _global_variables:

Global variables
----------------

You can explicitly make a variable a global variable by declaring it with the
:ref:`global <python3:global>` statement before it is used. Global variables can
be accessed and changed by the function. They exist outside the function and can
also be accessed and changed by other functions that declare them as global, or
by code that is not inside a function. Here is an example that illustrates the
difference between local and global variables:

.. code-block:: python

   def my_func():
       global x
       x = 1
       y = 2

.. code-block:: pycon

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

.. _nonlocal_variables:

Non-local variables
-------------------

While :ref:`global <python3:global>` is used for a top-level variable,
:ref:`nonlocal <python3:nonlocal>` refers to any variable in an enclosing area:

.. code-block:: python

   def enclosing():
       x = "Enclosing function variable"

       def enclosed():
           nonlocal x
           x = "Enclosed function variable"

       enclosed()
       print(x)

.. code-block:: pycon

   >>> enclosing()
   Enclosed function variable

.. seealso::

   * :pep:`3104`

Checks
------

* Assuming ``x = 1``, :func:`func` sets the local variable ``x`` to ``2`` and
  :func:`gfunc` sets the global variable ``x`` to ``3``, what value does ``x``
  assume after :func:`func` and :func:`gfunc` have been run through?
