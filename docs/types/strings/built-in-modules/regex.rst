:orphan:

Regular expressions
===================

.. seealso::
   * `www.regular-expressions.info <https://www.regular-expressions.info/>`_
   * `AutoRegex <https://www.autoregex.xyz>`_

``[]``
------

Square brackets define a list or range of characters to search for:

``[abc]``
    corresponds to a, b or c

``[a-z]``
    corresponds to any lower case letter
``[A-Za-z]``
    corresponds to each letter
``[A-Za-z0-9]``
    corresponds to any letter or digit

Number
------

``.``
    corresponds to a single character
``*``
    corresponds to zero or more times the preceding element, for example
    ``colou*r`` matches ``color``, ``colour``, ``colouur`` etc.
``?``
    corresponds to zero or once the preceding element. ``colou?r`` matches
    ``color`` and ``colour``.
``+``
    matches the previous element one or more times, for example ``.+`` matches
    ``.,`` ``..``, ``...`` etc.
``{N}``
    corresponds ``N`` times to the preceding element.
``{N,}``
    matches the previous element ``N`` or more times.
``{N,M}``
    corresponds at least ``N`` times to the preceding element, but not more than
    ``M`` times.

Position
--------

``^``
    puts the position at the beginning of the line.
``$``
    puts the position at the end of the line.

Link
----

``|``
    means *or*.

Escape characters and literals
------------------------------

``\``
    is used to search for a special character, for example to find ``.org`` you
    have to use the regular expression ``\.org`` because ``.`` is the special
    character that matches every character.
``\d``
    matches every single digit.
``\w``
    matches any part of a word character and is equivalent to ``[A-Za-z0-9]``.
``\s``
    matches any space, tab or newline.
``\b``
    matches a pattern on a word boundary.
