``print()``
===========

The function :func:`print` outputs character strings, whereby other Python data
types can easily be converted into strings and formatted, for example:

.. code-block:: pycon

   >>> import math
   >>> pi = math.pi
   >>> d = 28
   >>> u = pi * d
   >>> print(
   ...     "Pi is",
   ...     pi,
   ...     "and the circumference with a diameter of",
   ...     d,
   ...     "inches is",
   ...     u,
   ...     "inches.",
   ... )
   Pi is 3.141592653589793 and the circumference with a diameter of 28 inches is 87.96459430051421 inches.

.. _f-strings:

F-Strings
---------

F-strings can be used to shorten numbers that are too detailed for a text:

.. code-block:: pycon

    >>> print(f"The value of Pi is {pi:.3f}.")
    The value of Pi is 3.142.

In ``{pi:.3f}``, the format specification ``f`` is used to truncate the number
Pi to three decimal places.

In A/B test scenarios, you often want to display the percentage change in a key
figure. F strings can be used to formulate them in an understandable way:

.. code-block:: pycon

   >>> metrics = 0.814172
   >>> print(f"The AUC has increased to {metrics:=+7.2%}")
   The AUC has increased to +81.42%

In this example, the variable ``metrics`` is formatted with ``=`` taking over
the contents of the variable after the ``+``, displaying a total of seven
characters including the plus or minus sign, ``metrics`` and the percent sign.
``.2`` provides two decimal places, while the ``%`` symbol converts the decimal
value into a percentage. For example, ``0.514172`` is converted to ``+51.42%``.

Values can also be converted into binary and hexadecimal values:

.. code-block:: pycon

   >>> block_size = 192
   >>> print(f"Binary block size: {block_size:b}")
   Binary block size: 11000000
   >>> print(f"Hex block size: {block_size:x}")
   Hex block size: c0

There are also formatting specifications that are ideally suited for :abbr:`CLI
(Command Line Interface)` output, for example:

.. code-block:: pycon

   >>> data_types = [(7, "Data types", 19), (7.1, "Numbers", 19), (7.2, "Lists", 23)]
   >>> for n, title, page in data_types:
   ...     print(f"{n:.1f} {title:.<25} {page: >3}")
   ...
   7.0 Data types...............  19
   7.1 Numbers..................  19
   7.2 Lists....................  23

In general, the format is as follows, whereby all information in square brackets
is optional:

:samp:`:[[FILL]ALIGN][SIGN][0b|0o|0x|d|n][0][WIDTH][GROUPING]["." PRECISION][TYPE]`

The following table lists the fields for character string formatting and their
meaning:

+-----------------------+-------------------------------------------------------+
| Field                 | Meaning                                               |
+=======================+=======================================================+
| :samp:`FILL`          | Character used to fill in :samp:`ALIGN`. The default  |
|                       | value is a space.                                     |
+-----------------------+-------------------------------------------------------+
| :samp:`ALIGN`         | Text alignment and fill character:                    |
|                       |                                                       |
|                       | | ``<``: left-aligned                                 |
|                       | | ``>``: right-aligned                                |
|                       | | ``^``: centred                                      |
|                       | | ``=``: Fill character after :samp:`SIGN`            |
+-----------------------+-------------------------------------------------------+
| :samp:`SIGN`          | Display sign:                                         |
|                       |                                                       |
|                       | | ``+``: Display sign for positive and negative       |
|                       |    numbers                                            |
|                       | | ``-``: Default value, ``-`` only for negative       |
|                       |   numbers or space for positive                       |
+-----------------------+-------------------------------------------------------+
| :samp:`0b|0o|0x|d|n`  | Sign for integers:                                    |
|                       |                                                       |
|                       | | ``0b``: Binary numbers                              |
|                       | | ``0o``: Octal numbers                               |
|                       | | ``0x``: Hexadecimal numbers                         |
|                       | | ``d``: Default value, decimal integer with base 10  |
|                       | | ``n``: uses the current ``locale`` setting to       |
|                       |   insert the corresponding number separators          |
+-----------------------+-------------------------------------------------------+
| :samp:`0`             | fills with zeros                                      |
+-----------------------+-------------------------------------------------------+
| :samp:`WIDTH`         | Minimum field width                                   |
+-----------------------+-------------------------------------------------------+
| :samp:`GROUPING`      | Number separator: [#]_                                |
|                       |                                                       |
|                       | | ``,``: comma as thousands separator                 |
|                       | | ``_``: underscore for thousands separator           |
+-----------------------+-------------------------------------------------------+
| :samp:`.PRECISION`    | | For floating point numbers, the number of digits    |
|                       |   after the point                                     |
|                       | | For non-numeric values, the maximum length          |
+-----------------------+-------------------------------------------------------+
| :samp:`TYPE`          | Output format as number type or string                |
|                       |                                                       |
|                       | … for integers:                                       |
|                       |                                                       |
|                       | | ``b``: binary format                                |
|                       | | ``c``: converts the integer to the corresponding    |
|                       |   Unicode character                                   |
|                       | | ``d``: default value, decimal character             |
|                       | | ``n``: same as ``d``, th the difference that it     |
|                       |   uses the current ``locale`` setting to insert the   |
|                       |   corresponding number separators                     |
|                       | | ``o``: octal format                                 |
|                       | | ``x``: Hexadecimal format in base 16, using         |
|                       |   lowercase letters for the digits above 9            |
|                       | | ``X``: Hexadecimal format based on 16, using        |
|                       |   capital letters for digits above 9                  |
|                       |                                                       |
|                       | … for floating point numbers:                         |
|                       |                                                       |
|                       | | ``e``: Exponent with ``e`` as separator between     |
|                       |   coefficient and exponent                            |
|                       | | ``E``: Exponent with ``E`` as separator between     |
|                       |   coefficient and exponent                            |
|                       | | ``g``: Standard value for floating point numbers,   |
|                       |   whereby the exponent has a fixed width for large    |
|                       |   and small numbers                                   |
|                       | | ``G``: Like ``g``, but changes to ``E`` if the      |
|                       |   number becomes too large. The representations       |
|                       |   of infinity and NaN are also written in capital     |
|                       |   letters                                             |
|                       | | ``n``: Like ``g`` with the difference that it uses  |
|                       |   the current ``locale`` setting to insert the        |
|                       |   corresponding number separators                     |
|                       | | ``%``: Percentage. Multiplies the number by 100     |
|                       |   and displays it in the fixed format ``f`` followed  |
|                       |   by a percent sign                                   |
+-----------------------+-------------------------------------------------------+

.. [#] The format identifier ``n`` formats a number in a locally customised way,
    for example:

    .. code-block:: pycon

       >>> value = 635372
       >>> import locale
       >>> locale.setlocale(locale.LC_NUMERIC, "en_US.utf-8")
       'en_US.utf-8'
       >>> print(f"{value:n}")
       635,372

.. tip::
   A good source for F-strings is the help function:

   .. code-block:: pycon

      >>> help()
      help> FORMATTING
      ...

   You can browse through the help here and find many examples.

   You can exit the help function again with :kbd:`:`–:kbd:`q` and :kbd:`⏎`.

.. seealso::
   * `PyFormat <https://pyformat.info>`_
   * :ref:`python3:f-strings`
   * :pep:`498`

Debugging F-Strings
~~~~~~~~~~~~~~~~~~~

In Python 3.8, a specifier was introduced to help with debugging F-string
variables. By adding an equals sign ``=``, the code is included within the
F-string:

.. code-block:: pycon

   >>> uid = "veit"
   >>> print(f"My name is {uid.capitalize()=}")
   My name is uid.capitalize()='Veit'

Formatting date and time formats and IP addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:py:mod:`datetime` supports the formatting of strings using the same syntax as
the :py:meth:`strftime <datetime.datetime.strftime>` method for these objects.

.. code-block:: pycon

   >>> import datetime
   >>> import locale
   >>> locale.setlocale(locale.LC_TIME, "de_DE.utf-8")
   ... "de_DE.utf-8"
   'de_DE.utf-8'
   >>> today = datetime.date.today()
   >>> print(f"Heute ist {today:%A, %d. %B %Y}.")
   Heute ist Dienstag, 25. November 2025.

The :py:mod:`ipaddress` module of Python also supports the formatting of
``IPv4Address`` and ``IPv6Address`` objects.

Finally, third-party libraries can also add their own support for formatting
strings by adding a ``__format__`` method to their objects.

.. seealso::
   * :ref:`format-codes`
   * `Python strftime cheatsheet <https://strftime.org>`_
