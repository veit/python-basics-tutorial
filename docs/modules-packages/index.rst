Modules and packages
====================

Creating modules
----------------

It is easy to create your own modules that can be imported and used in the same
way as Python's built-in library modules. The example in this listing is a
simple module with a function that prompts for a file name and determines the
number of words that occur in that file.

.. literalinclude:: wc.py
   :linenos:

:doc:`../document/docstrings` are standard methods for documenting modules,
functions, methods and classes. ``read`` returns a string containing all the
characters in a file, and ``split`` returns a list of the words in a string that
has been split using spaces. You can use an ``\`` to spread a long statement
over several lines. With the ``if`` statement, you can run the program as a
script by typing ``python3 wc.py`` on the command line.

If you place a file in one of the directories of the module search path, which
can be found with ``sys.path``, it can be imported like any of the built-in
library modules with the ``import`` statement:

.. code-block:: python

    >>> import wc
    >>> wc.words_occur()

This function is called with the same attribute syntax used for library module
functions.

.. note::
    If you change the ``wc.py`` file on disk, import will not bring the changes
    into the same interactive session. In this case, you should use the
    ``reload`` function from the :doc:`imp <python3:library/imp>` library
    instead:

    .. code-block:: python

        >>> import imp
        >>> imp.reload(wc)
        <module 'wc'>

Packages
~~~~~~~~

For larger projects, there is a generalisation of the module concept called
packages that allows you to group modules in a directory or subdirectory and
then import and refer to them hierarchically using a
``package.subpackage.module`` syntax. This doesn’t require much more than
creating a possibly empty initialisation file for each package or subpackage.

Wheel
~~~~~

The current standard format for distributing Python modules and applications is
to use `Wheels <https://pythonwheels.com/>`_. Wheels were developed to make the
installation of Python code more reliable and to make dependency management
easier. However, the details of creating wheels are beyond the scope of this
section, but full details of the requirements and the process for creating
wheels can be found in doc:`jupyter-tutorial:productive/packaging/distribution`.

``py2exe`` and ``py2app``
~~~~~~~~~~~~~~~~~~~~~~~~~

`py2exe <https://www.py2exe.org/>`_ creates standalone Windows applications and
`py2app <https://py2app.readthedocs.io/en/latest/>`_ does the same for macOS. In
both cases, these are single executables that can run on machines that do not
have Python installed. In many ways, however, standalone executables are not
ideal, as they tend to be larger and less flexible than native Python
applications, but in some in some situations they can also be the best or only
solution.

``freeze``
~~~~~~~~~~

The ``freeze`` tool also creates an executable Python programme that runs on
computers that do not have Python installed. If you want to use the ``freeze``
tool, you will probably need to download the Python source code.

*Freezing* a Python program creates C files that are then compiled and linked
with a C compiler that you must have installed on your system. The application
thus frozen will only run on platforms for which the C compiler used provides
its executables.

.. seealso::

    * `Tools/freeze <https://github.com/python/cpython/tree/main/Tools/freeze>`_
