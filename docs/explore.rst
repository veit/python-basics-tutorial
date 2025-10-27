Exploring Python
================

Whether you use :ref:`idle` or the :ref:`interactive_shell`, there are some
useful functions to explore Python.

.. code-block:: pycon

   >>> x = 4.2

``type()``
----------

With :py:func:`type`, you can display the object type, for example:

.. code-block:: pycon

   >>> type(x)
   <class 'float'>

.. _help:

``help()``
----------

:py:func:`help` has two different modes. When you type :func:`help`, you call
the help system, which you can use to get information about modules, keywords,
and other topics. When you are in the help system, you will see a prompt with
``help>``. You can now enter a module name, for example ``float``, to search the
`Python documentation <https://docs.python.org/>`_ for that type.

:func:`help` is part of the :doc:`pydoc <python3:library/pydoc>` library, which
provides access to the documentation built into Python libraries. Since every
Python installation comes with full documentation, you have all the
documentation at your fingertips even offline.

Alternatively, you can use :func:`help` more specifically by passing a type or
variable name as a parameter, for example:

.. code-block:: pycon

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
    |  is_integer(self, /)
    |      Return True if the float is an integer.
    ...

For example, you will learn that ``x`` is of type ``float`` and has a function
 :func:`is_integer` that you can use with dot notation:

.. code-block:: pycon

   >>> x.is_integer()
   False

``id()``
--------

:py:func:`id` specifies the identification number of an object, for example:

.. code-block:: pycon

   >>> id(x)
   4304262800

``dir()``
---------

:py:func:`dir` is another useful function to find out which methods and data are
available locally or for a specific object:

.. code-block:: pycon

   >>> dir()
   ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'x']

For example, we can use ``dir(__builtins__)`` to display a list of what is
already available in the Python standard library:

.. code-block:: pycon

   >>> dir(__builtins__)
   ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
