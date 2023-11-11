Exploring Python
================

Whether you use IDLE or the interactive shell, there are some useful functions
to explore Python.

``help()``
----------

``help()`` has two different modes. When you type ``help()``, you call the help
system, which you can use to get information about modules, keywords, and other
topics. When you are in the help system, you will see a prompt with ``help>``.
You can now enter a module name, for example ``float``, to search the `Python
documentation <https://docs.python.org/>`_ for that type.

``help()`` is part of the :doc:`pydoc <python3:library/pydoc>` library, which
provides access to the documentation built into Python libraries. Since every
Python installation comes with full documentation, you have all the
documentation at your fingertips even offline.

Alternatively, you can use ``help()`` more specifically by passing a type or
variable name as a parameter, for example:

.. code-block:: python

    >>> x = 4.2
    >>> help(x)
    Help on float object:

    class float(object)
     |  float(x=0, /)
     |
     |  Convert a string or number to a floating point number, if possible.
     |
     |  Methods defined here:
     |
     |  __abs__(self, /)
     |      abs(self)
    ...

``dir()``, ``globals()`` and ``locals()``
-----------------------------------------

:py:func:`dir` is another useful function that lists objects in a specific
:doc:`namespace <oop/namespaces>`. If you use it without parameters, you can
find out which methods and data are available locally. Alternatively, it can
also list objects for a module or type.

.. code-block:: python

   >>> dir()
   ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'x']
   >>> dir(x)
   ['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

In contrast to :py:func:`dir`, both :py:func:`globals` and :py:func:`locals`
display the values associated with the objects. Currently, both functions return
the same thing:

.. code-block:: python

   >>> globals()
   {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 4.2}
