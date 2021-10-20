Quick start
===========

Status
------

.. image:: https://img.shields.io/github/contributors/veit/python-basics-tutorial.svg
   :alt: Contributors
   :target: https://github.com/veit/python-basics-tutorial/graphs/contributors
.. image:: https://img.shields.io/github/license/veit/python-basics-tutorial.svg
   :alt: License
   :target: https://github.com/veit/python-basics-tutorial/blob/main/LICENSE
.. image:: https://readthedocs.org/projects/python-basics-tutorial/badge/?version=latest
   :alt: Docs
   :target: https://python-basics-tutorial.readthedocs.io/en/latest/
.. image:: https://pyup.io/repos/github/veit/python-basics-tutorial/shield.svg
   :alt: Pyup
   :target: https://pyup.io/repos/github/veit/python-basics-tutorial/

Installation
------------

#. Download and unpack:

   .. code-block:: console

    $ curl -O https://codeload.github.com/veit/python-basics-tutorial/zip/main
    $ unzip main
    Archive:  main
    …
       creating: python-basics-tutorial-main/
    …

#. Install Python packages:

   .. code-block:: console

    $ python3 -m venv .
    $ source bin/activate
    $ python -m pip install --upgrade pip
    $ python -m pip install -r docs/requirements.txt

#. Create HTML documentation:

   Note that pandoc has to be installed. On Debian/Ubuntu you can just run

   .. code-block:: console

    $  sudo apt-get install pandoc

    To create the HTML documentation run these commands:

   .. code-block:: console

    $ sphinx-build -ab html docs/ docs/_build/

#. Create a PDF:

   For the creation of a PDF file you need additional packages.

   For Debian/Ubuntu you get them with the following command:

   .. code-block:: console

    $ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   or for macOS with:

   .. code-block:: console

    $ brew cask install mactex
    …
    🍺  mactex was successfully installed!
    $ curl --remote-name https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
    $ sudo texlua install-getnonfreefonts
    …
    mktexlsr: Updating /usr/local/texlive/2020/texmf-dist/ls-R...
    mktexlsr: Done.

   Then you can generate a PDF with:

   .. code-block:: console

    $ cd docs/
    $ make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   You can find the PDF at ``docs/_build/latex/pythonbasics.pdf``.

Follow us
---------

* `GitHub <https://github.com/veit/python-basics-tutorial>`_

Pull-Requests
-------------

If you have suggestions for improvements and additions, I recommend that you
create a `Fork <https://github.com/veit/python-basics-tutorial/fork>`_ of my
`GitHub Repository <https://github.com/veit/python-basics-tutorial/>`_ and make
your changes there. You are also welcome to make a *pull request*. If the
changes contained therein are small and atomic, I’ll be happy to look at your
suggestions.
