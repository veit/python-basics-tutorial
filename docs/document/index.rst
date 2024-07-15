Document
========

In order for your software package to be useful, documentation is required that
describes how your software can be installed, operated, used and improved:

* Those who want to use your package need information,

  * what problems your software solves and what the main features and
    limitations of the software are (``README``)
  * how the software can be used as an example
  * what changes have come in more recent software versions (``CHANGELOG``)

* Those who want to run the software need an installation guide for your
  software and the required dependencies.

* Those who want to improve the software need information about

  * how to help improve the product with bug fixes (``CONTRIBUTING``)
  * how to communicate with others (``CODE_OF_CONDUCT``)

All together need information on how the product is licensed (``LICENSE`` file
or ``LICENSES`` folder) and how to get help if needed.

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
   shot-scraper

Badges
------

Some of this information and more can be accessed as badges. They are helpful in
getting a quick overview of a product. For the
`cookiecutter-namespace-template
<https://github.com/veit/cookiecutter-namespace-template>`_ these are, for
example:

|Downloads| |Versions| |Contributors| |License| |Docs|

.. |Downloads| image::
   https://static.pepy.tech/badge/cookiecutter-namespace-template
   :target: https://www.pepy.tech/projects/cookiecutter-namespace-template
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

You can also create your own badges, for example:

 .. image:: https://img.shields.io/badge/dynamic/json?label=Mastodon&query=totalItems&url=https%3A%2F%2Fmastodon.social%2F@JupyterTutorial%2Ffollowers.json&logo=mastodon
    :alt: Mastodon
    :target: https://mastodon.social/@JupyterTutorial

.. seealso::
    * `shields.io <https://shields.io>`_

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
   reStructured Text, it is displayed as well-formatted HTML on ther
   :term:`Python Package Index` (:term:`PyPI`).

Other documentation tools
-------------------------

`Pycco <https://pycco-docs.github.io/pycco/>`_
    is a Python port of `Docco <https://github.com/jashkenas/docco>`_.
