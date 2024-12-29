Namespaces
==========

A namespace is a collection of currently defined symbolic names and information
about an object. You can think of a namespace as a dictionary in which the keys
are the object names and the values are the objects themselves. Each of these
key-value pairs assigns a name to the corresponding object.

    Namespaces are one honking great idea – let’s do more of those!

– `The Zen of Python <https://peps.python.org/pep-0020/>`_, by Tim Peters

Python now uses namespaces extensively. We have already learnt about some of
them in :doc:`function variables <../functions/variables>`: :ref:`local
<local_variables>`, :ref:`global <global_variables>` and :ref:`non-local
variables <nonlocal_variables>`.

If you are in the method of a class, you have direct access

#. to the **local namespace** with the parameters and variables declared in this
   method,
#. the **global namespace** with functions and variables declared at module
   level, and
#. the **built-in namespace** with the built-in functions and built-in
   exceptions.

These three namespaces are searched in this order.

To explain the different namespaces in more detail in our example, we have
extended our existing module to make it clear what can be accessed within a
method: :download:`form_ns.py`.

You can get an overview of the methods that are available in a namespace with

.. literalinclude:: form_ns.py
    :language: python
    :linenos:
    :lines: 65-71
    :lineno-start: 65

.. code-block:: pycon

    >>> import form_ns
    >>> c1 = form_ns.Circle()
    >>> c1.namespaces()
    ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
    Global namespace: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'Form', 'Square', 'Circle']
    Superclass namespace: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'move']
    Class namespace: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'circles', 'circumference', 'circumferences', 'diameter', 'instance_variables', 'move', 'namespaces', 'pi']
    Instance namespace: ['_Circle__diameter', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'circles', 'circumference', 'circumferences', 'diameter', 'instance_variables', 'move', 'namespaces', 'pi', 'x', 'y']
    Local namespace: ['self']

Via the ``self`` variable you also have access to

#. the **namespace of the instance** with

   * instance variables
   * private instance variables and
   * instance variables of the superclass,


#. the **namespace of the class** with

   * methods,
   * class variables,
   * private methods and
   * private class variables and

#. the **namespace of the superclass** with

   * methods of the superclass and
   * class variables of the superclass.

These three namespaces are also searched in this order.

You can now analyse the namespace of the instance with the method
``instance_variables``, for example:

.. literalinclude:: form_ns.py
    :language: python
    :linenos:
    :lines: 73-
    :lineno-start: 73

.. code-block:: pycon

    >>> import form_ns
    >>> c1 = form_ns.Circle()
    >>> c1.instance_variables()
    Instance variables self.__diameter, self.x, self.y: 1 0 0

.. note::

    While you can access the ``move`` method of the superclass ``form`` with
    ``self``, private instance variables, private methods and private class
    variables of the superclass are not accessible in this way.

If you only want to change instances of a certain class, you can do this with
the :mod:`garbage collector <gc>`, for example:

.. code-block:: pycon

    >>> import forms
    >>> c1 = forms.Circle()
    >>> c2 = forms.Circle(2, 3, 4)
    >>> s1 = forms.Square(5, 6, 7)
    >>> import gc
    >>> for obj in gc.get_objects():
    ...     if isinstance(obj, forms.Circle):
    ...         obj.move(3, 0)
    ...
    >>> c1.x, c1.y
    (3, 0)
    >>> c2.x, c2.y
    (6, 4)
    >>> s1.x, s1.y
    (6, 7)
