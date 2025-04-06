Docstrings
==========

With the Sphinx extension `sphinx.ext.autodoc
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_,
docstrings can also be included in the documentation. The following directives
can be specified

.. rst:directive::  automodule
                    autoclass
                    autoexception

… for function-like objects:

.. rst:directive::  autofunction
                    automethod
                    autoproperty
                    autodecorator

… for data and attributes:


.. rst:directive::  autodata
                    autoattribute

These document a module, a class or an exception using the docstring of the
respective object.

Installation
------------

``sphinx.ext.autodoc`` is usually already specified in the Sphinx configuration
file  ``docs/conf.py``:

.. code-block:: python

   extensions = ["sphinx.ext.autodoc", ...]

If your package and its documentation are part of the same repository, they will
always have the same relative position in the filesystem. In this case you can
simply edit the Sphinx configuration for ``sys.path`` to indicate the relative
path to the package, so:

.. code-block:: python

   sys.path.insert(0, os.path.abspath(".."))
   import requests

If you have installed your Sphinx documentation in a virtual environment, you
can also install your package there with:

.. code-block:: console

   $ python -m pip install my.package

or, if you want to develop the package further with:

.. code-block:: console

   $ python -m pip install -e https://github.com/veit/my.package.git

Examples
--------

Here you can find some examples from the documentation of the Python
:py:mod:`string` module:

.. literalinclude:: autodoc-examples.rst
   :language: rest
   :lines: 3-

This leads to the :doc:`autodoc-examples`.

Guidelines
----------

In :pep:`8` there is only a brief reference to conventions for a good docstring:
:pep:`Documentation Strings <8#comments>`. Other :abbr:`PEPs (Python Enhancement
Proposals)` refer to the :pep:`Docstring Processing System Framework <256>`:

:pep:`257`
    describes docstring conventions:

    * What should be documented where?
    * The first line should be a one-line summary.

:pep:`258`
    specifies the docstring processing system.

:pep:`287`
    specifies the docstring syntax.

The `Google Python Style Guide
<https://google.github.io/styleguide/pyguide.html>`_ also provides more specific
guidelines for `RPython comments and docstrings
<https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`_.
The `NumPy style guide <https://numpydoc.readthedocs.io/en/latest/format.html>`_
also provides further `docstring standards
<https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard>`_.
The main difference between the two is that Google uses indentation and NumPy
uses underlining:

Google Python Style Guide:
    .. code-block:: python

       def func(arg1, arg2):
           """Summary line.

           Extended description of function.

           Args:
               arg1 (int): Description of arg1
               arg2 (str): Description of arg2

           Returns:
               bool: Description of return value

           """
           return True

NumPy Style Guide:
    .. code-block:: python

       def func(arg1, arg2):
           """Summary line.

           Extended description of function.

           Parameters
           ----------
           arg1 : int
               Description of arg1
           arg2 : str
               Description of arg2

           Returns
           -------
           bool
               Description of return value

           """
           return True

.. _napoleon:

``sphinx.ext.napoleon``
~~~~~~~~~~~~~~~~~~~~~~~

The Sphinx extension `sphinx.ext.napoleon
<https://sphinxcontrib-napoleon.readthedocs.io/>`_ processes docstrings that
correspond to both the Google Python Style Guide and the NumPy Style Guide:

You can find the detailed configuration options in
`sphinxcontrib.napoleon.Config
<https://sphinxcontrib-napoleon.readthedocs.io/en/latest/sphinxcontrib.napoleon.html#sphinxcontrib.napoleon.Config>`_.

``sphinx-autodoc-typehints``
----------------------------

With :pep:`484` a standard method for expressing types in Python code was
introduced. This also allows types to be expressed differently in docstrings.
The variant with types according to :pep:`484` has the advantage that type
testers and IDEs can be used for static code analysis.

Python 3 Type annotations in Docstrings:
    .. code-block:: python

       def func(arg1: int, arg2: str) -> bool:
           """Summary line.

           Extended description of function.

           Args:
               arg1: Description of arg1
               arg2: Description of arg2

           Returns:
               Description of return value

           """
           return True
