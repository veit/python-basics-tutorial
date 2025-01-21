String methods
==============

Most of the Python :ref:`string methods <python3:string-methods>` are integrated
in the :ref:`str <python3:textseq>` type so that all ``str`` objects
automatically have them:

.. code-block:: pycon

   >>> welcome = "hello pythonistas!\n"
   >>> welcome.isupper()
   False
   >>> welcome.isalpha()
   False
   >>> welcome[0:5].isalpha()
   True
   >>> welcome.capitalize()
   'Hello pythonistas!\n'
   >>> welcome.title()
   'Hello Pythonistas!\n'
   >>> welcome.strip()
   'Hello pythonistas!'
   >>> welcome.split(" ")
   ['hello', 'pythonistas!\n']
   >>> chunks = [snippet.strip() for snippet in welcome.split(" ")]
   >>> chunks
   ['hello', 'pythonistas!']
   >>> " ".join(chunks)
   'hello pythonistas!'
   >>> welcome.replace("\n", "")
   'hello pythonistas!'

Below you will find an overview of the most common :ref:`string methods
<python3:string-methods>`:

+-----------------------------------+---------------------------------------------------------------+
| Method                            | Description                                                   |
+===================================+===============================================================+
| :py:meth:`str.count`              | returns the number of non-overlapping occurrences of the      |
|                                   | string.                                                       |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.endswith`           | returns ``True`` if the string ends with the suffix.          |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.startswith`         | returns ``True`` if the string starts with the prefix.        |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.join`               | uses the string as a delimiter for concatenating a sequence   |
|                                   | of other strings.                                             |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.index`              | returns the position of the first character in the string if  |
|                                   | it was found in the string; triggers a ``ValueError`` if it   |
|                                   | was not found.                                                |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.find`               | returns the position of the first character of the first      |
|                                   | occurrence of the substring in the string; like ``index``,    |
|                                   | but returns ``-1`` if nothing was found.                      |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.rfind`              | Returns the position of the first character of the last       |
|                                   | occurrence of the substring in the string; returns ``-1`` if  |
|                                   | nothing was found.                                            |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.replace`            | replaces occurrences of a string with another string.         |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.strip`,             | strip spaces, including line breaks.                          |
| :py:meth:`str.rstrip`,            |                                                               |
| :py:meth:`str.lstrip`             |                                                               |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.split`              | splits a string into a list of substrings using the passed    |
|                                   | separator.                                                    |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.lower`              | converts alphabetic characters to lower case.                 |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.upper`              | converts alphabetic characters to upper case.                 |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.casefold`           | converts characters to lower case and converts all            |
|                                   | region-specific variable character combinations to a common   |
|                                   | comparable form.                                              |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.ljust`,             | left-aligned or right-aligned; fills the opposite side of the |
| :py:meth:`str.rjust`              | string with spaces (or another filler character) in order to  |
|                                   | obtain a character string with a minimum width.               |
+-----------------------------------+---------------------------------------------------------------+
| :py:meth:`str.removeprefix`       | In Python 3.9 this can be used to extract the suffix or file  |
| :py:meth:`str.removesuffix`       | name.                                                         |
+-----------------------------------+---------------------------------------------------------------+

``str.split`` and ``str.join``
------------------------------

While :meth:`python3:str.split` returns a list of strings,
:meth:`python3:str.join` takes a list of strings and joins them into a single
string. Normally :meth:`python3:str.split` uses whitespace as a delimiter for
the strings to be split, but you can change this behaviour with an optional
:doc:`parameter <../../../functions/params>`.

.. warning::
   Concatenating strings with ``+`` is useful but not efficient when it comes to
   joining a large number of strings into a single string, as a new string
   object is created each time ``+`` is applied.  :samp:`"Hello" +
   "Pythonistas!"` creates two objects, of which one is immediately discarded.

If you join strings with :meth:`python3:str.join`, you can insert any characters
between the strings:

.. code-block:: pycon

   >>> " :: ".join(["License", "OSI Approved"])
   'License :: OSI Approved'

You can also use an empty string,  ``""``, for example for the CamelCase
notation of Python classes:

.. code-block:: pycon

   >>> "".join(["My", "Class"])
   'MyClass'

:meth:`python3:str.split` is mostly used to split strings at spaces. However,
you can also split a string at a specific other string by passing an optional
:doc:`parameter <../../../functions/params>`:

.. code-block:: pycon

   >>> example = "1. You can have\n\twhitespaces, newlines\n   and tabs mixed in\n\tthe string."
   >>> example.split()
   ['1.', 'You', 'can', 'have', 'whitespaces,', 'newlines', 'and', 'tabs', 'mixed', 'in', 'the', 'string.']
   >>> license = "License :: OSI Approved"
   >>> license.split(" :: ")
   ['License', 'OSI Approved']

Sometimes it is useful to allow the last field in a string to contain arbitrary
text. You can do this by specifying an optional second :doc:`parameter
<../../../functions/params>` for how many splits should be performed:

.. code-block:: pycon

   >>> example.split(" ", 1)
   ['1.', 'You can have\n\twhitespaces, newlines\n   and tabs mixed in\n\tthe string.']

If you want to use :meth:`python3:str.split` with the optional second argument,
you must first specify a first argument. To ensure that all spaces are split,
use :doc:`../../none` as the first argument:

.. code-block:: pycon

   >>> example.split(None, 8)
   ['1.', 'You', 'can', 'have', 'whitespaces,', 'newlines', 'and', 'tabs', 'mixed in\n\tthe string.']

.. tip::
   I use :meth:`python3:str.split` and :meth:`python3:str.join` extensively,
   mostly for text files generated by other programmes. For writing
   :doc:`Python4DataScience:data-processing/serialisation-formats/csv/index` or
   :doc:`Python4DataScience:data-processing/serialisation-formats/json/index`
   files, however, I usually use the associated Python libraries.

Remove whitespace
-----------------

:py:meth:`str.strip` returns a new string that differs from the original string
only in that all spaces at the beginning or end of the string have been removed.
:py:meth:`str.lstrip` and :py:meth:`str.rstrip` work similarly, but only remove
the spaces at the left or right end of the original string:

.. code-block:: pycon

   >>> example = "    whitespaces, newlines \n\tand tabs. \n"
   >>> example.strip()
   'whitespaces, newlines \n\tand tabs.'
   >>> example.lstrip()
   'whitespaces, newlines \n\tand tabs. \n'
   >>> example.rstrip()
   '    whitespaces, newlines \n\tand tabs.'

In this example, the newlines ``\n`` are regarded as whitespace. The exact
assignment may differ from operating system to operating system. You can find
out what Python considers to be whitespace by accessing the variable
:py:data:`string.whitespace`. For me, the following is returned:

.. code-block:: pycon

   >>> import string
   >>> string.whitespace
   ' \t\n\r\x0b\x0c'

The characters specified in hexadecimal format (``\x0b``, ``\x0c``) represent
the vertical tab and feed characters.

.. tip::
   Do not change the value of these variables to influence the functionality of
   :py:meth:`str.strip` :abbr:`etc (et cetera)`. You can pass characters as
   additional :doc:`parameters <../../../functions/params>` to determine which
   characters these methods remove:

   .. code-block:: pycon

      >>> url = "https://www.cusy.io/"
      >>> url.strip("htps:/w.")
      'cusy.io'

Search in strings
-----------------

:ref:`str <python3:textseq>` offer several methods for a simple search for
character strings: The four basic methods for searching strings are
:py:meth:`str.find`, :py:meth:`str.rfind`, :py:meth:`str.index` and
:py:meth:`str.rindex`. A related method, :py:meth:`str.count`, counts how many
times a string can be found in another string.

:py:meth:`str.find` requires a single
:doc:`parameter <../../../functions/params>`: the substring being searched for;
the position of the first occurrence is then returned, or ``-1`` if there is no
occurrence:

.. code-block:: pycon

   >>> hipy = "Hello Pythonistas!\n"
   >>> hipy.find("\n")
   18

:py:meth:`str.find`  can also accept one or two additional :doc:`parameters
<../../../functions/params>`:

``start``
    The number of characters at the beginning of the string to be searched that
    should be ignored.
``end``
    The Number of characters at the end of the string to be searched that should
    be ignored.

In contrast to :py:meth:`find`, :py:meth:`rfind` starts the search at the end of
the string and therefore returns the position of the last occurrence.

:py:meth:`index` and :py:meth:`rindex` differ from :py:meth:`find` and
:py:meth:`rfind` in that a :class:`python3:ValueError` exception is triggered
instead of the return value ``-1``.

You can use two other :ref:`string methods <python3:string-methods>` to search
for strings: :py:meth:`str.startswith` and :py:meth:`str.endswith`. These
methods return ``True``- or ``False``, depending on whether the string to which
they are applied starts or ends with one of the strings specified as
:doc:`parameters <../../../functions/params>`:

.. code-block:: pycon

   >>> hipy.endswith("\n")
   True
   >>> hipy.endswith(("\n", "\r"))
   True

There are also several methods that can be used to check the property of a
character string:

+---------------------------+---------------+---------------+---------------+---------------+---------------+
| Method                    | ``[!#$%…]``   | ``[a-zA-Z]``  | ``[¼½¾]``     | ``[¹²³]``     | ``[0-9]``     |
+===========================+===============+===============+===============+===============+===============+
| :py:meth:`str.isprintable`| ✅            | ✅            | ✅            | ✅            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+
| :py:meth:`str.isalnum`    | ❌            | ✅            | ✅            | ✅            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+
| :py:meth:`str.isnumeric`  | ❌            | ❌            | ✅            | ✅            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+
| :py:meth:`str.isdigit`    | ❌            | ❌            | ❌            | ✅            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+
| :py:meth:`str.isdecimal`  | ❌            | ❌            | ❌            | ❌            | ✅            |
+---------------------------+---------------+---------------+---------------+---------------+---------------+

:py:meth:`str.isspace` checks for spaces.

Changing strings
----------------

:ref:`str <python3:textseq>` are :term:`immutable`, but they have several methods
that can return a modified version of the original string.

:py:meth:`str.replace` can be used to replace occurrences of the first
 :doc:`parameter <../../../functions/params>` with the second, for example:

.. code-block:: pycon

   >>> hipy.replace("\n", "\n\r")
   'Hello Pythonistas!\n\r'

:py:meth:`str.maketrans` and :py:meth:`str.translate` can be used together to
translate characters in strings into other characters, for example:

.. code-block:: pycon
   :linenos:

   >>> hipy = "Hello Pythonistas!\n"
   >>> trans_map = hipy.maketrans(" ", "-", "!\n")
   >>> hipy.translate(trans_map)
   'Hello-Pythonistas'

Line 2
    :py:meth:`str.maketrans` is used to create a translation table from the two
    string arguments. The two arguments must each contain the same number of
    characters. Characters that are not to be returned are passed as the third
    argument.
Line 3
    The table generated by :py:meth:`str.maketrans` is passed to
    :py:meth:`str.translate`.

.. toctree::
   :titlesonly:
   :hidden:

   regex

Checks
------

* How can you change a heading such as ``variables and expressions`` so that it
  contains hyphens instead of spaces and can therefore be better used as a file
  name?

* If you want to check whether a line begins with ``.. note::``, which method
  would you use? Are there any other options?

* Suppose you have a string with exclamation marks, quotation marks and line
  breaks. How can these be removed from the string?

* How can you change all spaces and punctuation marks from a string to a hyphen
  (``-``)?
