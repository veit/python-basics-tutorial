``@property`` decorator
=======================

In Python, you can access instance variables directly, without additional getter
and setter methods that are often used in Java and other object-oriented
languages. This makes writing Python classes cleaner and easier, but in some
situations using getter and setter methods can also be useful. Let’s say you
need a value before setting it in an instance variable, or you just want to find
out the value of an attribute. In both cases, getter and setter methods would do
the job, but at the cost of losing easy access to instance variables in Python.

The answer is to use a *property*. This combines the ability to pass access to
an instance variable via methods such as getters and setters with simple access
to instance variables via dot notation. To create a *property*, the
:class:`python3:property` decorator is used with a method that has the name of
the property:

.. literalinclude:: form_pr.py
    :language: python
    :linenos:
    :lines: 23-25
    :lineno-start: 23

Without a setter, however, the *property* ``length`` is read-only:

.. code-block:: python

    >>> s1 = form.Square()
    >>> s1.length = 2
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute

To change this, you need to add a setter:

.. literalinclude:: form_pr.py
    :language: python
    :linenos:
    :lines: 27-29
    :lineno-start: 27

Now you can use the dot notation to both get and set the property ``length``.
Note that the name of the method remains the same, but the decorator changes to
the *property* name, in our case to ``length.setter``:

.. code-block:: python

    >>> s1 = form.Square()
    >>> s1.length = 2
    >>> s1.circumference()
    8

A big advantage of Python’s ability to add properties is that you can work with
plain old instance variables at the beginning of development and then seamlessly
switch to *property* variables whenever and wherever you need to, without
changing the client code. The access is still the same, using dot notation.
