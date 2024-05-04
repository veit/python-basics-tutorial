Private variables and methods
=============================

A private variable or private method is a variable that is not visible outside
the methods of the class in which it is defined. Private variables and methods
are useful for two reasons:

#. they increase security and reliability by selectively denying access to
   important parts of an object’s implementation
#. they prevent naming conflicts that can arise from the use of inheritance.

A class can define a private variable and inherit it from a class that defines a
private variable with the same name. Private variables make code easier to read
because they explicitly state what is only used internally in a class.
Everything else is the interface of the class.

Most languages that define private variables do so by using the keyword
*private* or similar. The convention in Python is simpler and also makes it
easier to see immediately what is private and what is not. Any method or
instance variable whose name begins with a double underscore (``__``) but does
not end is private; anything else is not.

As an example, consider the following class definition:

.. code-block:: pycon

    >>> class MyClass:
    ...     def __init__(self):
    ...         self.x = 1
    ...         self.__y = 2
    ...     def print_y(self):
    ...         print(self.__y)
    ...
    >>> m = MyClass()
    >>> print(m.x)
    1
    >>> print(m.__y)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'MyClass' object has no attribute '__y'

The ``print_y`` method is not private, and since it is in the ``MyClass`` class,
it can access and output ``__y``:

.. code-block:: pycon

    >>> m.print_y()
    2

.. note::

   The mechanism used to ensure privacy falsifies the name of private variables
   and private methods when the code is compiled into bytecode. Specifically,
   this means that ``_classname`` is prefixed to the variable name:

   .. code-block:: pycon

      >>> dir(m)
      ['_MyClass__y', '__class__', …]

   So this is only to prevent accidental access.
