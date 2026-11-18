Lambda functions
================

In Python, a lambda function is an anonymous function, that is, a function that
is declared without a name. It is a small and restricted function that is no
longer than one line. Like a normal function, a lambda function can have several
arguments, but only one expression that is evaluated and returned.

The syntax of a lambda function is :samp:`lambda {ARGUMENTS}: {EXPRESSION}`

.. note::
   There is no ``return`` statement in the lambda function. The single
   expression after the colon is the return value.

.. tip::
   However, always use a ``def`` statement instead of an assignment that binds a
   lambda expression directly to an identifier – in other words, use

   .. code-block:: pycon
      :class: good

      >>> def add(x, y):
      ...     return x + y
      ...
      >>> add(2, 3)
      5

   rather than

   .. code-block:: pycon
      :class: bad

      >>> add = lambda x, y: x + y
      >>> add(2, 3)
      5

This is generally more useful for tracebacks and string representations. The
only advantage of lambda functions is that they can be embedded within a larger
expression. In the next example, we’ll see how a lambda function is created
within a function call. In this case, there is no global variable to store the
values of the lambda function:

.. code-block:: pycon
   :linenos:

   >>> count = ["1", "123", "1000"]
   >>> max(count)
   '123'
   >>> max(count, key=lambda val: int(val))
   '1000'

In this case, the :py:func:`max` function accepts the ``key`` argument, which
defines how the size of each entry is to be determined. Using a lambda function
that converts each string into an integer, ``max`` can compare the numerical
values to determine the expected result.

.. tip::
   `cusy seminar: Advanced Python
   <https://cusy.io/en/our-training-courses/advanced-python.html>`_
