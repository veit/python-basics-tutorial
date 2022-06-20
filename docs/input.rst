Input
=====

You can use the :func:`python3:input` function to get data input. Use the prompt
string you want to display as a parameter for ``input``:

.. code-block:: python

    >>> first_name = input("First name? ")
    First name? Veit
    >>> surname = input("Surname? ")
    Surname? Schiele
    >>> print(first_name, surname)
    Veit Schiele

This is a fairly simple way to get data input. The only catch is that the input
comes in as a string. So if you want to use a number, you have to convert it
with the :class:`python3:int` or :class:`python3:float` function.
