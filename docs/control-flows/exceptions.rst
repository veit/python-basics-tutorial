Exception handling
==================

Exceptions or errors can be caught and handled using the compound statement
``try``-``except``-``else``-``finally``. This statement can also catch and
handle exceptions that you can define and raise yourself. Any exception that is
not caught will cause the programme to terminate. The following examples show
the basic handling of exceptions.

.. literalinclude:: exceptions.py
   :linenos:

Line 1
    Here you define your own exception type, which inherits from the basic type
    ``Exception``.
Line 5
    If an ``IOError`` or ``EmptyFileError`` occurs during the execution of the
    instructions in the ``try`` block, the corresponding ``except`` block is
    executed.
Line 7
    An ``IOError`` could be triggered here.
Line 10
    Here you trigger the ``EmptyFileError``.
Line 15
    The ``else`` clause is optional; it is executed if no exception occurs in
    the ``try`` block.

    .. note::
       In this example, ``continue`` statements could have been used in the
       ``except`` blocks instead.

Line 17
    The ``finally`` clause is optional; it is executed at the end of the block,
    regardless of whether an exception was thrown or not.
