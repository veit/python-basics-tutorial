Creating modules
================

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

For larger projects, there is a generalisation of the module concept called
packages that allows you to group modules in a directory or subdirectory and
then import and refer to them hierarchically using a
``package.subpackage.module`` syntax. This doesn’t require much more than
creating a possibly empty initialisation file for each package or subpackage.
You can find a template for this in my `ccokiecutter-namespace-template
<https://github.com/veit/cookiecutter-namespace-template>`_.
