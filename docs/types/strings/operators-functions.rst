Operators and functions
=======================

The operators and functions that work with character strings return new
character strings derived from the original. The operators (``in``, ``+`` and
``*``) and built-in functions (``len``, ``max`` and ``min``) work with character
strings in the same way as with :doc:`lists <../sequences-sets/lists>` and
:doc:`tuples <../sequences-sets/tuples>`.

.. code-block:: pycon

   >>> welcome = "Hello pythonistas!\n"
   >>> 2 * welcome
   'Hello pythonistas!\nHello pythonistas!\n'
   >>> welcome + welcome
   'Hello pythonistas!\nHello pythonistas!\n'
   >>> "python" in welcome
   True
   >>> max(welcome)
   'y'
   >>> min(welcome)
   '\n'

Indexing and slicing
--------------------

The index and slice notation works in the same way to obtain individual elements
or slices:

.. code-block:: pycon

   >>> welcome[0:5]
   'Hello'
   >>> welcome[6:-1]
   'pythonistas!'

However, the index and slice notation cannot be used to add, remove or replace
elements, as character strings are immutable:

.. code-block:: pycon

   >>> welcome[6:-1] = "everybody!"
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment

Conversions
-----------

Converting character strings into numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the :class:`python3:int` and :class:`python3:float` functions to
convert character strings into integer or floating point numbers. If a character
string is passed that cannot be interpreted as a number of the specified type,
these functions trigger a :class:`python3:ValueError` exception. Exceptions are
explained in more detail in :doc:`control flows
<../../control-flows/exceptions>`. You can also pass :class:`python3:int` an
optional second :doc:`parameter  <../../functions/params>` that specifies the
numerical base to be used when interpreting the string:

.. code-block:: pycon
   :linenos:

   >>> float("12.34")
   12.34
   >>> float("12e3")
   12000.0
   >>> int("1000")
   1000
   >>> int("1000", base=10)
   1000
   >>> int("1000", 8)
   512
   >>> int("1000", 2)
   8
   >>> int("1234", 2)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: invalid literal for int() with base 2: '1234'

Lines 5–8
    If no second :doc:`parameter <../../functions/params>` is specified,
    :class:`python3:int` calculates with a base of ``10``.
Lines 9, 10
    ``1000`` is interpreted as an `octal number
    <https://en.wikipedia.org/wiki/Octal>`_.
Lines 11, 12
    ``1000`` is interpreted as a `binary number
    <https://en.wikipedia.org/wiki/Binary_number>`_.
Lines 13–16
    ``1234`` cannot be specified as an integer on base ``2``. A
    :class:`python3:ValueError` exception is therefore triggered.

Changing character strings with list manipulations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since :ref:`str <python3:textseq>` objects are immutable, there is no way to
change them directly like :doc:`lists <../sequences-sets/lists>`. However, you
can convert them into lists:

.. code-block:: pycon

   >>> palindromes = "lol level gag"
   >>> palindromes_list = list(palindromes)
   >>> palindromes_list.reverse()
   >>> "".join(palindromes_list)
   'gag level lol'

Converting objects into strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Python, almost anything can be converted into a string using the built-in
:ref:`str <python3:textseq>` function:

.. code-block:: pycon

   >>> data_types = [(7, "Data types", 19), (7.1, "Numbers", 19), (7.2, "Lists", 23)]
   >>> (
   ...     "The title of chapter "
   ...     + str(data_types[0][0])
   ...     + " is «"
   ...     + data_types[0][1]
   ...     + "»."
   ... )
   'The title of chapter 7 is «Data types».'

The example uses :ref:`str <python3:textseq>` to convert an integer from the
``data_types`` list into a string, which is then concatenated again to form the
final string.

.. note::
   While :ref:`str <python3:textseq>` is mostly used to generate human readable
   text, :func:`python3:repr` is more commonly used for debugging output or
   status reports, for example to get information about the built-in Python
   function :func:`python3:len`:

   .. code-block:: pycon

      >>> repr(len)
      '<built-in function len>'

Checks
------

* For example, can you add or multiply a string with an integer, a floating
  point number or a complex number?

* Which of the following strings cannot be converted into numbers and why?

 * ``int("1e2")``
 * ``int(1e+2)``
 * ``int("1+2")``
 * ``int("+2")``
