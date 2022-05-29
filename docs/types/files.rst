Files
=====

A file is accessed via a Python file object:

.. code-block:: python
    :linenos:

    >>> f = open("my_file", "w")
    >>> f.write("My first line")
    13
    >>> f.write("\nAdditional line with preceding newline character")
    49
    >>> f.close()
    >>> f = open("my_file", "r")
    >>> line1 = f.readline()
    >>> line2 = f.readline()
    >>> f.close()
    >>> print(line1, line2)
    My first line
     Additional line with preceding newline character
    >>> import os
    >>> print(os.getcwd())
    /home/veit
    >>> os.chdir(os.path.join("/home/", "veit/", "Documents/"))
    >>> filename = os.path.join("/home", "veit/", "my_file")
    >>> print(filename)
    /home/veit/my_file
    >>> f = open(filename, "r")
    >>> print(f.readline())
    My first line
    >>> f.close()

Line 1
    creates a file object. Here the file ``my_file`` in the current home
    directory is opened in write mode (``"w"``).
Line 2, 4 and 6
    writes two lines to the file and closes the file.
Line 7
    opens the file again, this time in read mode (``"r"``).
Line 14
    imports the built-in :doc:`os <python3:library/os>` module, which offers
    several functions to move around the file system and work with the
    pathnames of files and directories.
Line 17
    changes to another directory.
Zeile 18
    addresses the file with an absolute pathname, so you can still access it.

There are several other input and output options:

:doc:`fileinput <python3:library/fileinput>`
    allows you to quickly write a loop over standard input or a list of files.
:doc:`sys <python3:library/sys>`
    allows you to access  ``stdin``, ``stdout`` and ``stderr``.
:doc:`struct <python3:library/struct>`
    provides support for reading and writing files created by or to be used by
    C programs.
:doc:`pickle <python3:library/pickle>`
    persists Python data types, see also :doc:`../save-data/pickle`.
