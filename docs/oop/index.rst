Object-oriented programming
===========================

Python offers full support for OOP. The following listing is an example that
could be the beginning of a simple shapes module for a drawing program. It is
mainly intended as a reference if you are already familiar with OOP. In the
notes, the syntax and semantics of Python are compared with the standard
functions of other languages.

.. literalinclude:: form.py
    :linenos:

Line 2
    Classes are defined with the keyword ``class``.
Line 4
    Methods, like functions, are defined with the keyword ``def``.

    The instance initialisation method (constructor) for a class is always
    called ``__init__``.

Lines 5—6
    The first argument of a method is called ``self`` by convention. When the
    method is called, ``self`` is set to the instance that called the method.

    Here, the instance variables ``x`` and ``y`` are created and initialised.

Line 15
    The class ``Circle`` inherits from the class ``Shape``.
Line 19
    A class must explicitly call the initialiser of its base class in its
    initialiser.
Line 24
    The method ``__str__`` is used by the function ``print``.

Other special method attributes allow operators to be overloaded or are used by
built-in methods such as the length (``len``) function.

.. code-block:: python

    >>> import form
    >>> c1 = form.Circle()
    >>> c2 = form.Circle(3, 5, 8)
    >>> print(c1)
    Circle of radius 1 at coordinates (0, 0)
    >>> print(c2)
    Circle of radius 3 at coordinates (5, 8)
    >>> c2.area()
    28.27431
    >>> c2.move(6, 10)
    >>> print(c2)
    Circle of radius 3 at coordinates (11, 18)
