Extensions
==========

.. seealso::
    `Sphinx Extensions
    <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_

Built-in extensions
-------------------

`sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
    Integrate documentation from docstrings
`sphinx.ext.autosummary <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_
    generates summaries of functions, methods and attributes from docstrings
`sphinx.ext.autosectionlabel <https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html>`_
    references section using the title
`sphinx.ext.graphviz <https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html>`_
    Rendering of `Graphviz <https://www.graphviz.org/>`_ graphs
`sphinx.ext.ifconfig <https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html>`_
    includes content only under certain conditions
`sphinx.ext.intersphinx <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
    allows the linking of other project documentation
`sphinx.ext.mathjax <https://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax>`_
    Rendering via JavaScript
`sphinx.ext.napoleon <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_
    Support for NumPy and Google style docstrings
`sphinx.ext.todo <https://www.sphinx-doc.org/en/master/usage/extensions/todo.html>`_
    Support for ToDo items
`sphinx.ext.viewcode <https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html>`_
    adds links to the source code of the Sphinx documentation

.. seealso::
    `sphinx/sphinx/ext/
    <https://github.com/sphinx-doc/sphinx/tree/master/sphinx/ext>`_

Third-party extensions
----------------------

`nbsphinx <https://nbsphinx.readthedocs.io/>`_
    Jupyter Notebooks in Sphinx
`jupyter-sphinx <https://github.com/jupyter/jupyter-sphinx>`_
    allows rendering of Jupyter interactive widgets in Sphinx.

    .. seealso::

        `Embedding Widgets in the Sphinx HTML Documentation
        <https://ipywidgets.readthedocs.io/en/latest/embedding.html#embedding-widgets-in-the-sphinx-html-documentation>`_

`Breathe <https://github.com/breathe-doc/breathe>`_
    ReStructuredText and Sphinx bridge to `Doxygen <https://www.doxygen.nl>`_
`numpydoc <https://github.com/numpy/numpydoc>`_
    `NumPy <https://numpy.org/>`_’s Sphinx extension
`Releases <https://github.com/bitprophet/releases>`_
    writes a changelog file
`sphinxcontrib-napoleon <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/>`_
    Napoleon is a pre-processor for parsing NumPy- and Google-style docstrings
`sphinx-autodoc-annotation <https://github.com/nicolashainaux/sphinx-autodoc-annotation>`_
    use Python 3 annotations in sphinx-enabled docstrings
`sphinx-autodoc-typehints <https://github.com/agronholm/sphinx-autodoc-typehints>`_
    Type hints support for the Sphinx autodoc extension
`sphinx-git <https://sphinx-git.readthedocs.io/en/latest/>`_
    `git <https://git-scm.com/>`_-Changelog for Sphinx
`Sphinx Gitstamp Generator Extension <https://github.com/jdillard/sphinx-gitstamp>`_
    inserts a git datestamp into the context
`sphinx-issues <https://pypi.org/project/sphinx-issues/>`_
    creates links to GitHub or GitLab issues, pull requests and user profiles.
`sphinx-intl <https://pypi.org/project/sphinx-intl/>`_
    Sphinx extension for translations
`sphinx-autobuild <https://github.com/sphinx-doc/sphinx-autobuild>`_
    monitors a Sphinx repository and creates new documentation as soon as
    changes are made
`Sphinx-Needs <https://sphinx-needs.readthedocs.io/en/latest/>`_
    allows the definition, linking and filtering of need-objects, for example
    requirements and test cases
`Sphinx-pyreverse <https://github.com/alendit/sphinx-pyreverse>`_
    generate a UML diagram from python modules
`sphinx-jsonschema <https://github.com/lnoor/sphinx-jsonschema>`_
    display a `JSON Schema <https://json-schema.org>`_ in the Sphinx
    documentation
`Sphinxcontrib-mermaid <https://github.com/mgaitan/sphinxcontrib-mermaid>`_
    allows you to embed Mermaid graphics in your documents.
`Sphinx Sitemap Generator Extension <https://github.com/jdillard/sphinx-sitemap>`_
    generate multiversion and multilanguage `sitemaps
    <https://www.sitemaps.org/protocol.html>`_ for the HTML version
`Sphinx Lint <https://github.com/sphinx-contrib/sphinx-lint>`_
    based on `rstlint.py
    <https://github.com/python/cpython/blob/e0433c1e7/Doc/tools/rstlint.py>`_
    from CPython.
`sphinx-toolbox <https://sphinx-toolbox.readthedocs.io/en/stable/index.html>`_
    Toolbox for Sphinx with many useful tools.

.. seealso::
    `sphinx-contrib <https://github.com/sphinx-contrib/>`_
        A repository of Sphinx extensions maintained by their respective authors.
    `sphinx-extensions <https://sphinx-extensions.readthedocs.io/en/latest/>`_
        Curated site with Sphinx extensions with live examples and their
        configuration.

Own Extensions
--------------

Local extensions in a project should be specified relative to the documentation.
The appropriate path is specified in the Sphinx configuration ``docs/conf.py``.
If your extension is in the directory ``exts`` in the file ``foo.py``, then the
``conf.py`` should look like this:

.. code-block:: python

    import sys
    import os

    sys.path.insert(0, os.path.abspath("exts"))

    extensions = ["foo", ...]

.. seealso::
    * `Developing extensions for Sphinx
      <https://www.sphinx-doc.org/en/master/extdev/>`_
    * `Application API
      <https://www.sphinx-doc.org/en/master/extdev/appapi.html>`_
