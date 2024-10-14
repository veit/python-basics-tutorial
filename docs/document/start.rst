Create a Sphinx project
=======================

Installation and start
----------------------

#. Create a virtual environment for your documentation project:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ python3 -m venv .venv

   .. tab:: Windows

      .. code-block:: ps1con

         C:> python -m venv .venv

#. Switch to the virtual environment and install Sphinx there:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ . .venv/bin/activate
         $ (.venv) python -m pip install sphinx
         Creating a virtualenv for this project…
         …

   .. tab:: Windows

      .. code-block:: ps1con

         C:> .venv\Scripts\activate.bat
         C:> (.venv) python -m pip install sphinx
         Creating a virtualenv for this project…
         …

#. Create your Sphinx documentation project:

   .. tab:: Linux/macOS

      .. code-block:: console

         $ sphinx-quickstart docs
         Selected root path: docs
         > Separate source and build directories (y/n) [n]:
         > Name prefix for templates and static dir [_]:
         > Project name: my.package
         > Author name(s): Veit Schiele
         > Project release []: 1.0
         > Project language [en]:
         > Source file suffix [.rst]:
         > Name of your master document (without suffix) [index]:
         > autodoc: automatically insert docstrings from modules (y/n) [n]: y
         > doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
         > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
         > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
         > coverage: checks for documentation coverage (y/n) [n]:
         > imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
         > mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
         > ifconfig: conditional inclusion of content based on config values (y/n) [n]:
         > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
         > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:
         > Create Makefile? (y/n) [y]:
         > Create Windows command file? (y/n) [y]:

         Creating file docs/source/conf.py.
         Creating file docs/source/index.rst.
         Creating file docs/Makefile.
         Creating file docs/make.bat.

   .. tab:: Windows

      .. code-block:: ps1con

         C:> sphinx-quickstart docs
         Selected root path: docs
         > Separate source and build directories (y/n) [n]:
         > Name prefix for templates and static dir [_]:
         > Project name: my.package
         > Author name(s): Veit Schiele
         > Project release []: 1.0
         > Project language [en]:
         > Source file suffix [.rst]:
         > Name of your master document (without suffix) [index]:
         > autodoc: automatically insert docstrings from modules (y/n) [n]: y
         > doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
         > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
         > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
         > coverage: checks for documentation coverage (y/n) [n]:
         > imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
         > mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
         > ifconfig: conditional inclusion of content based on config values (y/n) [n]:
         > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
         > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:
         > Create Makefile? (y/n) [y]:
         > Create Windows command file? (y/n) [y]:

         Creating file docs\conf.py.
         Creating file docs\index.rst.
         Creating file docs\Makefile.
         Creating file docs\make.bat.

Sphinx layout
-------------

::

    .
    └── docs
        ├── Makefile
        ├── _static
        ├── _templates
        ├── conf.py
        ├── index.rst
        └── make.bat

``index.rst`` is the initial file for the documentation, in which the table of
contents is located. The table of contents will be expanded by you as soon as
you add new ``*.rst`` files.

Generate the documentation
--------------------------

You can now generate the documentation, for example with:

.. tab:: Linux/macOS

   .. code-block:: console

      $ sphinx-build -ab html docs/ docs/_build

.. tab:: Windows

   .. code-block:: ps1con

      C:> sphinx-build -ab html docs\ docs\_build

``a``
    regenerates all pages of the documentation.

    .. note::
       This is always useful if you have added new pages to your documentation.
       to your documentation.

``b``
    specifies which builder should be used to generate the documentation. In our
    example this is ``html``.
