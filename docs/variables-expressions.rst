Variables and expressions
=========================

Variables
---------

The most commonly used command in Python is assignment. The Python code to
create a Vairiable called ``x`` that is to be given the value ``π`` is:

.. code-block:: python

    >>> x = 3.14159

In Python, unlike many other programming languages, neither a variable
declaration nor an end-of-line delimiter is necessary. The line is terminated by
the end of the line. Variables are created automatically when they are assigned
for the first time.

.. note::
   In Python, variables are labels that refer to objects. Any number of labels
   can refer to the same object, and if that object changes, so does the value
   to which all those variables refer. To better understand what this means, see
   the following example:

   .. code-block:: python

      >>> x = [1, 2, 3]
      >>> y = x
      >>> y[0] = 4
      >>> print(x)
      [4, 2, 3]

   However, variables can also refer to constants:

   .. code-block:: python

      >>> x = 1
      >>> y = x
      >>> z = y
      >>> y = 4
      >>> print(x,y,z)
      1 4 1

   In this case, after the third line, ``x``, ``y`` and ``z`` all refer to the
   same immutable integer object with the value ``1``. The next line, ``y = 4``,
   causes ``y`` to refer to the integer object ``4``, but this does not change
   the references of ``x`` or ``z``.

Python variables can be set to any object, whereas in many other languages
variables can only be stored in the declared type.

Variable names are case-sensitive and can contain any alphanumeric character as
well as underscores, but must begin with a letter or underscore.

.. note::
   You can use a variable name to overwrite built-in functions, types and other
   objects so that they can then only be accessed via the :doc:`builtins
   <python3:library/builtins>` module. These variable names should therefore
   never be used. You can obtain a list of the :mod:`__builtins__` objects
   with :

   .. code-block:: python

      >>> dir(__builtins__)
      ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

Expressions
-----------

Python supports arithmetic and similar expressions. The following code
calculates the average of ``x`` and ``y`` and stores the result in the variable
``z``:

.. code-block:: python

    >>> x = 1
    >>> y = 2
    >>> z = (x + y) / 2

.. note::
   Arithmetic operators that use only integers do not always return an integer.
   As of Python 3, division returns a floating point number. If you want the
   traditional integer division to return an integer, you can use ``//``
   instead.
