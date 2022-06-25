Document
========

A ``README`` file in the root directory should contain general information for
both users and maintainers of a project.

* It should be written in a very easy to read markup, such as
  :doc:`rest` or Markdown.
* It should explain the purpose of the project or library in a
  non-presuppositional way.
* It should include links to the main sources of the software.

A ``LICENSE`` file should always be present to make clear which rights of use
apply.

.. seealso::
   * `Eric Holscher: Why You Shouldn’t Use “Markdown” for Documentation
     <https://ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/>`_
   * `Tom Johnson: 10 reasons for moving away from DITA
     <https://idratherbewriting.com/2015/01/28/10-reasons-for-moving-away-from-dita/>`_
   * `Tom Johnson: Jekyll versus DITA
     <https://idratherbewriting.com/2015/03/23/new-series-jekyll-versus-dita/>`_
   * `Google developer documentation style guide
     <https://developers.google.com/style/>`_
   * `Google Technical Writing Courses for Engineers
     <https://developers.google.com/tech-writing/overview>`_

.. toctree::
   :titlesonly:
   :hidden:

   start
   rest
   code-blocks
   placeholder
   ui-elements
   directives
   docstrings
   intersphinx
   uml/index
   extensions
   test

Badges
------

Some of this information and more can be accessed as badges. They are helpful in
getting a quick overview of a product. For the
`cookiecutter-namespace-template
<https://github.com/veit/cookiecutter-namespace-template>`_ these are, for
example:

|Downloads| |Updates| |Versions| |Contributors| |License| |Docs|

.. |Downloads| image::
   https://static.pepy.tech/badge/cookiecutter-namespace-template
   :target: https://pepy.tech/project/cookiecutter-namespace-template
.. |Updates| image::
   https://pyup.io/repos/github/veit/cookiecutter-namespace-template/shield.svg
   :target: https://pyup.io/repos/github/veit/cookiecutter-namespace-template/
.. |Versions| image::
   https://img.shields.io/pypi/pyversions/cookiecutter-namespace-template.svg
   :target: https://pypi.org/project/cookiecutter-namespace-template/
.. |Contributors| image::
   https://img.shields.io/github/contributors/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/graphs/contributors
.. |License| image::
   https://img.shields.io/github/license/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/blob/main/LICENSE
.. |Docs| image::
   https://readthedocs.org/projects/cookiecutter-namespace-template/badge/?version=latest
   :target: https://cookiecutter-namespace-template.readthedocs.io/en/latest/

Sphinx
------

For extensive documentation you can, for example, use `Sphinx
<https://www.sphinx-doc.org/>`_, a documentation tool that converts
reStructuredText into HTML or PDF, EPub and man pages. The Python Basics are
also created with Sphinx. To get a first impression of Sphinx, you can have a
look at the source code of this page by following the link `Sources
<../_sources/document/index.rst.txt>`_.

Originally, Sphinx was developed for the documentation of Python and is now
used in almost all Python projects, including `NumPy and SciPy
<https://docs.scipy.org/doc/>`_, `Matplotlib
<https://matplotlib.org/users/index.html>`_, `Pandas
<https://pandas.pydata.org/docs/>`_ and `SQLAlchemy
<https://docs.sqlalchemy.org/>`_.

The Sphinx `autodoc
<http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ feature,
which can be used to create documentation from Python
:doc:`docstrings`, may also be conducive to the spread of Sphinx among Python
developers. Overall, Sphinx allows developers to create complete documentation
in place. Often the documentation is also stored in the same :doc:`Git
<jupyter-tutorial:productive/git/index>` repository, so that the creation of the
latest software documentation remains easy.

Sphinx is also used in projects outside the Python community, e.g. for the
documentation of the Linux kernel: `Kernel documentation update
<https://lwn.net/Articles/705224/>`_.

`Read the Docs <https://readthedocs.org/>`_ was developed to forther simplify
documentation. Read the Docs makes it easy to create and publish documentation
after each commit.

For project documentation, visualising :doc:`Git feature branches
<jupyter-tutorial:productive/git/workflows/feature-branches>` and :doc:`tags
<jupyter-tutorial:productive/git/tagging>` with
:doc:`jupyter-tutorial:productive/git/git-big-picture` can be helpful.

.. note::
   If the content of ``long_description`` in ``setuptools.setup()`` is written
   in reStructured Text, it is displayed as well-formatted HTML on the
   :term:`Python Package Index (PyPI)`.

.. seealso::
   * `reStructuredText Primer
     <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
   * `reStructuredText Quick Reference
     <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_

Other documentation tools
-------------------------

`Pycco <https://pycco-docs.github.io/pycco/>`_
    is a Python port of `Docco <https://github.com/jashkenas/docco>`_.
