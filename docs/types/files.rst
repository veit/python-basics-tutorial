Files
=====

Opening files
-------------

In Python, you open and read a file using the built-in :func:`python3:open`
function and various built-in read operations. The following short Python
program reads a line from a text file called :samp:`{myfile}`:

.. code-block:: python

    >>> f = open('docs/types/myfile', 'r')
    >>> line = f.readline()

:func:`python3:open` does not read anything from the file, but returns a
so-called file object that you can use to access the open file. It keeps track
of a file and how much of the file has been read or written. All file input in
Python is done with file objects, not file names.

The first call to :mod:`python3:readline` returns the first line of the file
object, which is everything up to and including the first line break, or the
entire file if there is no line break in the file; the next call to ``readline``
returns the second line if it exists, and so on.

The first argument of the ``open`` function is a pathname. In the previous
example, you open a file that you assume is in the current working directory.
The following example opens a file in an absolute location – :samp:`{C:\\My
Documents\\myfile}`:

.. code-block:: python

    >>> import os
    >>> pathname = os.path.join('C:', 'Users', 'Veit', 'Documents', 'myfile')
    >>> with open(pathname, 'r') as f:
    ...     line = f.readline()

.. note::

    This example uses the ``with`` keyword, which means that the file is opened
    with a context manager, which is explained in more detail in
    :doc:`/control-flows/with`. This way of opening files manages possible I/O
    errors better and should generally be preferred.

Closing files
-------------

After all data has been read from or written to a file object, the file object
should be closed again to free up system resources, allow other code to read or
write to the underlying file, and make the program more reliable overall. For
small scripts, this usually does not have a large impact because file objects
are automatically closed when the script or program exits. However, for larger
programs, too many open file objects can exhaust system resources, causing the
program to terminate. You close a file object with the ``close`` method when the
file object is no longer needed:

.. code-block:: python

    >>> f = open('docs/types/myfile', 'r')
    >>> line = f.readline()
    >>> f.close()

However, using a :doc:`/control-flows/with` usually remains the better option to
automatically close files when you are done:

.. code-block:: python

    >>> with open('docs/types/myfile', 'r') as f:
    ...     line = f.readline()

Opening files in write or other modes
-------------------------------------

The second argument of the :func:`python3:open` function is a string that
specifies how the file should be opened. ``'r'`` opens the file for reading,
``'w'`` opens the file for writing, and ``'a'`` opens the file for attaching. If
you want to open the file for reading, you can omit the second argument, because
``'r'`` is the default value. The following short program writes :samp:`Hi,
Pythonistas!` to a file:

.. code-block:: python

    >>> f = open('docs/types/myfile', 'w')
    >>> f.write('Hi, Pythonistas!\n')
    18
    >>> f.close()

Depending on the operating system, :func:`python3:open` may also have access to
other file modes. However, these modes are not necessary for most purposes.

``open`` can take an optional third argument that defines how read or write
operations for this file are buffered. Buffering keeps data in memory until
enough data has been requested or written to justify the time required for a
disk access. Other parameters for ``open`` control the encoding for text files
and the handling of line breaks in text files. Again, you don’t usually need to
worry about these functions, but as you become more advanced with Python you may
want to read up on them.

Read and write functions
------------------------

I have already introduced the most common function for reading text files,
:mod:`python3:readline`. This function reads a single line from a file object
and returns it, including all line breaks at the end of the line. If there is
nothing more to read, readline returns an empty string, which makes it easy to
determine, for example, the number of lines in a file:

.. code-block:: python

    >>> f = open('docs/types/myfile', 'r')
    >>> lc = 0
    >>> while f.readline() != '':
    ...     lc = lc + 1
    ... 
    >>> print(lc)
    2
    >>> f.close()

A shorter way to count all lines is with the ``readlines`` method, which is also
built in, that reads all lines of a file and returns them as a list of strings
with one string per line:

.. code-block:: python

    >>> f = open('docs/types/myfile', 'r')
    >>> print(len(f.readlines()))
    2
    >>> f.close()

If you count all the lines in a large file, this method may cause the memory to
fill up because the entire file is read at once. It is also possible that memory
overflows with :mod:`python3:readline` if you try to read a line from a large
file that does not contain newline characters. To better deal with such
situations, both methods have an optional argument that affects the amount of
data read at a time. Another way to iterate over all the lines in a file is to
treat the file object as an iterator in a :ref:`for-loop`:

.. code-block:: python

    >>> f = open('docs/types/myfile', 'r')
    >>> lc = 0
    >>> for l in f:
    ...     lc = lc + 1
    ... 
    >>> print(lc)
    2
    >>> f.close()

This method has the advantage that the lines are read into the memory as needed, so that even with large files there is no need to fear a lack of memory. The other advantage of this method is that it is simpler and more readable.

However, a possible problem with the read method can arise when conversions are
done in text mode on Windows and macOS if you use the :func:`open` command in
text mode, that is without appending a ``b``. In text mode on macOS, each ``\r``
is converted to ``\n``, while on Windows, ``\r\n`` pairs are converted to
``\n``. You can specify how line breaks are handled by using the ``newline``
parameter when opening the file and specifying ``newline='\n'``, ``\r`` or
``\r\n``, which will cause only that string to be used as a line break:

.. code-block:: python

    >>> f = open('docs/types/myfile', newline='\n')

In this example, only ``\n`` is considered a line break. However, if the file
was opened in binary mode, the ``newline`` parameter is not necessary, as all
bytes are returned exactly as they are in the file.

The write methods corresponding to ``readline`` and ``readlines`` are ``write``
and ``writelines``. Note that there is no ``writeline`` function. ``write``
writes a single string that can span multiple lines if newline characters are
embedded in the string, as in the following example:

.. code-block:: python

    f.write('Hi, Pythinistas!\n\n')

The ``writelines`` method is confusing, however, because it does not necessarily
write multiple lines; it takes a list of strings as an argument and writes them
sequentially to the specified file object without inserting line breaks between
the list items; only if the strings in the list contain line breaks are line
breaks added to the file object; otherwise they are concatenated. ``writelines``
is thus the exact inverse of ``readlines``, since it can be applied to the list
returned by ``readlines`` to write a file identical to the source file. Assuming
that ``myfile.txt`` exists and is a text file, the following example creates an
exact copy of :file:`myfile` named :file:`myfile2`:

Using binary mode
~~~~~~~~~~~~~~~~~

If you want to read all the data in a file (partially) into a single byte object
and transfer it to memory to be treated as a byte sequence, you can use the
``read`` method. Without an argument, it reads the entire file from the current
position and returns the data as a byte object. With an integer argument, it
reads a maximum of this number of bytes and returns a bytes object of the
specified size:

.. code-block:: python
    :linenos:

    >>> f = open('myfile', 'rb')
    >>> head = f.read(16)
    >>> print(head)
    b'Hi, Pythonistas!'
    >>> body = f.read()
    >>> print(body)
    b'\n\n'
    >>> f.close()

Line 1
    opens a file for reading in binary mode
Line 2
    reads the first 16 bytes as ``head`` string
Line 3
    outputs the ``head`` string
Line 5
    reads the rest of the file

.. note::

   Files opened in binary mode work only with bytes and not with strings. To use
   the data as strings, you must decode all byte objects into string objects.
   This point is often important when dealing with network protocols, where data
   streams often behave like files, but must be interpreted as bytes and not
   strings.

There are several other input and output options:

:doc:`fileinput <python3:library/fileinput>`
    allows you to quickly write a loop over standard input or a list of files.
:doc:`sys <python3:library/sys>`
    allows you to access ``stdin``, ``stdout`` and ``stderr``.
:doc:`struct <python3:library/struct>`
    provides support for reading and writing files created by or to be used by C
    programs.
:doc:`pickle <python3:library/pickle>`
    persists Python data types, :abbr:`s.a. (see also)`
    :doc:`../save-data/pickle`.
