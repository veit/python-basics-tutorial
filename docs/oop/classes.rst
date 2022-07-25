Classes
=======

A :doc:`class in Python <python3:tutorial/classes>` is actually a data type. All
of Python’s built-in data types are classes, and Python provides you with
powerful tools to manipulate every aspect of a class’s behaviour. You can define
a class with the ``class`` statement:

.. code-block:: python

    >>> class MyClass:
    ...     STATEMENTS

``MyClass``
    Class identifiers are usually written in capital letters, that mean the
    first letter of each word is capitalised to emphasise the identifiers.
``STATEMENTS``
    is a list of Python statements – usually variable assignments and function
    definitions. However, no assignments or function definitions are required;
    it can just be a single ``pass`` statement.

After you have defined the class, you can create a new object of the class type
(an instance of the class) by calling the class name as a function:

.. code-block:: python

    >>> instance = MyClass()

Class instances can be used as structures or data sets. However, unlike C
structures or Java classes, the data fields of an instance do not have to be
declared in advance. The following short example defines a class called
``Square``, creates a ``Square`` instance, assigns a value to the edge length
and then uses this value to calculate the total edge length:

.. code-block:: python

    >>> my_square = Square()
    >>> my_square.length = 3
    >>> print(4 * my_square.length)
    12

As in Java and many other languages, the fields of an instance are addressed
using dot notation.

You can initialise fields of an instance automatically by including an
``__init__`` initialisation method in the class. This function is executed each
time an instance of the class is created with this new instance as the first
argument ``self``. Unlike in Java and C++, Python classes can also have only one
``__init__`` method. In the following example, squares with an edge length of
``1`` are created by default:

.. code-block:: python
    :linenos:

    >>> class Square:
    ...     def __init__(self):
    ...         self.length = 1
    ...
    >>> my_square = Square()
    >>> print(4 * my_square.length)
    4

Line 2
    By convention, ``self`` is always the name of the first argument of
    ``__init__``. ``self`` is set to the newly created ``Square`` instance when
    ``__init__`` is executed.
Line 5
    Next, the code uses the class definition. You first create a ``Square``
    instance object.
Line 6
    This line takes advantage of the fact that the ``length`` field is already
    initialised.

    You can also overwrite the ``length`` field so that the last line gives a
    different result than the previous ``print`` statement:

    .. code-block:: python

        >>> my_square.length = 3
        >>> print(4 * my_square.length)
        12
