Sphinx
======

For extensive documentation you can, for example, use `Sphinx
<https://www.sphinx-doc.org/>`_, a documentation tool that converts
reStructuredText into HTML or PDF, EPub and man pages. The Python Basics are
also created with Sphinx. To get a first impression of Sphinx, you can have a
look at the source code of this page by following the link `Sources
<../_sources/document/index.rst.txt>`_.

Originally, Sphinx was developed for the documentation of Python and is now
used in almost all Python projects, including `NumPy and SciPy
<https://docs.scipy.org/doc/>`_, `Matplotlib
<https://matplotlib.org/stable/users/index.html>`_, `Pandas
<https://pandas.pydata.org/docs/>`_ and `SQLAlchemy
<https://docs.sqlalchemy.org/>`_.

The Sphinx `autodoc
<https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ feature,
which can be used to create documentation from Python
:doc:`docstrings`, may also be conducive to the spread of Sphinx among Python
developers. Overall, Sphinx allows developers to create complete documentation
in place. Often the documentation is also stored in the same :doc:`Git
<Python4DataScience:productive/git/index>` repository, so that the creation of
the latest software documentation remains easy.

Sphinx is also used in projects outside the Python community, e.g. for the
documentation of the Linux kernel: `Kernel documentation update
<https://lwn.net/Articles/705224/>`_.

`Read the Docs <https://about.readthedocs.com/>`_ was developed to forther
simplify documentation. Read the Docs makes it easy to create and publish
documentation after each commit.

For project documentation, visualising :doc:`Git feature branches
<Python4DataScience:productive/git/workflows/feature-branches>` and :doc:`tags
<Python4DataScience:productive/git/tag>` with
:doc:`Python4DataScience:productive/git/advanced/git-big-picture` can be
helpful.

.. note::
   If the content of ``long_description`` in ``setup()`` is written in
   reStructured Text, it is displayed as well-formatted HTML on the
   :term:`Python Package Index` (:term:`PyPI`).

.. toctree::
   :titlesonly:
   :hidden:

   start
   rest
   convert
   code-blocks
   placeholder
   ui-elements
   directives
   docstrings
   intersphinx
   uml/index
   extensions
   test
