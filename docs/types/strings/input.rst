``input()``
===========

You can use the :func:`python3:input` function to get data input. Use the prompt
string you want to display as a parameter for ``input``:

.. code-block:: pycon

    >>> first_name = input("First name? ")
    First name? Veit
    >>> surname = input("Surname? ")
    Surname? Schiele
    >>> print(first_name, surname)
    Veit Schiele

This is a fairly simple way to get data input. The only catch is that the input
comes in as a string. So if you want to use a number, you have to convert it
with the :class:`python3:int` or :class:`python3:float` function, for example, for calculating the age from the year of birth:

.. code-block:: pycon

    >>> import datetime
    >>>
    >>> currentDateTime = datetime.datetime.now()
    >>> year = currentDateTime.year
    >>> year_birth = input("Year of birth? ")
    Year of birth? 1964
    >>> age = year - int(year_birth)
    >>> print("Age:", age, "years")
    Age: 58 years

Checks
------

* How can you get string and integer values with the :func:`input` function?

* What is the effect if you do not use :func:`int` to call :func:`input` for
  integer inputs?

* Can you change the code so that it accepts a floating point number?

* What happens if you enter an incorrect value type?

* Write the code to ask for the names and ages of three users. After the values
  have been entered, ask for one of the names and output the corresponding age.
