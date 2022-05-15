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
namespace. If you use it without parameters, you can find out which methods and
data are available locally. Alternatively, it can also list objects for a module
or type.
