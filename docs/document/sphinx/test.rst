Testing
=======

Builds and links
----------------

.. _build-errors:

Build errors
~~~~~~~~~~~~

You have the option of checking whether your content is built correctly before
publishing your changes. `Sphinx <https://www.sphinx-doc.org/>`_ has a nitpicky
mode for this, which can be called up with the ``-n`` option, for example with:

.. tab:: Linux/macOS

   .. code-block:: console

       $ python -m sphinx -nb html docs/ docs/_build/

.. tab:: Windows

   .. code-block:: ps1con

       C:> python -m sphinx -nb html docs\ docs\_build\

.. _link-checks:

links
~~~~~

You can also automatically ensure that the link targets you specify are
accessible. Our documentation tool Sphinx uses a ``linkcheck`` builder for this,
which you can call up with:

.. tab:: Linux/macOS

   .. code-block:: console

       $ python -m sphinx -b linkcheck docs/ docs/_build/

.. tab:: Windows

   .. code-block:: ps1con

       C:> python -m sphinx -b linkcheck docs\ docs\_build\

The output can then look like this, for example:

.. tab:: Linux/macOS

   .. code-block:: console

       $ python -m sphinx -b linkcheck docs/ docs/_build/
       Running Sphinx v3.5.2
       loading translations [de]... done
       …
       building [mo]: targets for 0 po files that are out of date
       building [linkcheck]: targets for 27 source files that are out of date
       …
       (content/accessibility: line   89) ok        https://bbc.github.io/subtitle-guidelines/
       (content/writing-style: line  164) ok        http://disabilityinkidlit.com/2016/07/08/introduction-to-disability-terminology/

       …
       (   index: line    5) redirect  https://cusy-design-system.readthedocs.io/ - with Found to https://cusy-design-system.readthedocs.io/de/latest/
       …
       (accessibility/color: line  114) broken    https://chrome.google.com/webstore/detail/nocoffee/jjeeggmbnhckmgdhmgdckeigabjfbddl - 404 Client Error: Not Found for url: https://chrome.google.com/webstore/detail/nocoffee/jjeeggmbnhckmgdhmgdckeigabjfbddl

.. tab:: Windows

   .. code-block:: ps1con

       C:> python -m sphinx -b linkcheck docs\ docs\_build\
       Running Sphinx v3.5.2
       loading translations [de]... done
       …
       building [mo]: targets for 0 po files that are out of date
       building [linkcheck]: targets for 27 source files that are out of date
       …
       (content/accessibility: line   89) ok        https://bbc.github.io/subtitle-guidelines/
       (content/writing-style: line  164) ok        http://disabilityinkidlit.com/2016/07/08/introduction-to-disability-terminology/

       …
       (   index: line    5) redirect  https://cusy-design-system.readthedocs.io/ - with Found to https://cusy-design-system.readthedocs.io/de/latest/
       …
       (accessibility/color: line  114) broken    https://chrome.google.com/webstore/detail/nocoffee/jjeeggmbnhckmgdhmgdckeigabjfbddl - 404 Client Error: Not Found for url: https://chrome.google.com/webstore/detail/nocoffee/jjeeggmbnhckmgdhmgdckeigabjfbddl

Continuous integration
~~~~~~~~~~~~~~~~~~~~~~

If necessary, you can also check automatically in your :term:`CI` pipeline
whether the documentation is being built and the links are valid. In
:doc:`../../test/tox`, the configuration can be added as follows:

.. code-block:: ini
   :caption: tox.ini

   [testenv:docs]
   # Keep base_python in sync with ci.yml and .readthedocs.yaml.
   base_python = py312
   extras = docs
   commands =
     sphinx-build -n -T -W -b html -d {envtmpdir}/doctrees docs docs/_build/html

   [testenv:docs-linkcheck]
   base_python = {[testenv:docs]base_python}
   extras = {[testenv:docs]extras}
   commands = sphinx-build -W -b linkcheck -d {envtmpdir}/doctrees docs docs/_build/html

You can then define the following jobs for GitHub, for example:

.. code-block:: yaml
   :caption: .github/workflows/ci.yml

   docs:
     name: Build docs and run doctests
     needs: build-package
     runs-on: ubuntu-latest
     steps:
     - name: Download pre-built packages
       uses: actions/download-artifact@v4
       with:
         name: Packages
         path: dist
     - run: tar xf dist/*.tar.gz --strip-components=1

     - uses: actions/setup-python@v5
       with:
         # Keep in sync with tox.ini/docs and .readthedocs.yaml
         python-version: "3.12"
         cache: pip
     - run: python -m pip install tox
     - run: python -m tox run -e docs

reST formatting
---------------

Whether the :doc:`Sphinx <start>` documentation is written in valid :doc:`rest`
format can be checked with `sphinx-lint
<https://pypi.org/project/sphinx-lint/>`_. We usually include this in our
:doc:`pre-commit
<Python4DataScience:productive/git/advanced/hooks/pre-commit>` configuration:

.. code-block:: yaml
   :caption: .pre-commit-config.yaml

   - repo: https://github.com/sphinx-contrib/sphinx-lint
     rev: v1.0.0
     hooks:
       - id: sphinx-lint
         types: [rst]

.. seealso::
   With :doc:`Sybil:index` you can not only check :doc:`rest`, but also
   :doc:`Markdown <Sybil:markdown>` and :doc:`Myst <Sybil:myst>`, for example.
   Sybil can also check code blocks in the documentation with either
   :doc:`../../test/pytest/index` or :doc:`../../test/unittest`.

.. _test_code:

Code
----

With the built-in Python library :doc:`../../test/doctest`, you can also test
code in your documentation with the :func:`doctest.testfile` method:

.. code-block:: Python

   import doctest

   doctest.testfile("example.rst")

This short script executes and checks all interactive Python examples contained
in the :file:`example.rst` file. The content of the file is treated as if it
were a single huge docstring.

.. seealso::
   A simple example can be found in the Python documentation: `Simple Usage:
   Checking Examples in a Text File
   <https://docs.python.org/3/library/doctest.html#simple-usage-checking-examples-in-a-text-file>`_.

   Another way to test code in documentation is
   `pytest-doctestplus <https://github.com/scientific-python/pytest-doctestplus>`_.

Code formatting
---------------

The formatting of code blocks can be checked with `blacken-docs
<https://github.com/adamchainz/blacken-docs>`_, which uses
:doc:`Python4DataScience:productive/qa/black`. We usually integrate the library
via the :doc:`pre-commit
<Python4DataScience:productive/git/advanced/hooks/pre-commit>` framework:

.. code-block:: yaml

   - repo: https://github.com/adamchainz/blacken-docs
     rev: "v1.12.1"
     hooks:
     - id: blacken-docs
       additional_dependencies:
       - black

blacken-docs currently supports the following black options:

* `line-length
  <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#l-line-length>`_
* `preview
  <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#preview>`_
* `skip-string-normalization
  <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#s-skip-string-normalization>`_
* `target-version
  <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#t-target-version>`_

`Vale <https://vale.sh>`_ goes beyond spelling and grammar checks. It also
checks the language style: Is what is said repeated? Is the language too
informal? Is the language inconsistent? Are undesirable clichés being used? Or
is the language sexist?

Vale is used by many open source projects, including

* GitLab (`.vale.ini
  <https://gitlab.com/gitlab-org/gitlab/blob/master/.vale.ini>`_, `rules
  <https://gitlab.com/gitlab-org/gitlab/-/tree/master/doc/.vale/gitlab_base>`__)
* Homebrew (`.vale.ini
  <https://github.com/Homebrew/brew/blob/master/.vale.ini>`__, `rules
  <https://github.com/Homebrew/brew/tree/master/docs/vale-styles/Homebrew>`__)

The following styles come with Vale itself:

`Microsoft <https://github.com/errata-ai/Microsoft>`_
    An implementation of the `Microsoft Writing Style Guide
    <https://learn.microsoft.com/en-us/style-guide/welcome/>`__.
`Google <https://github.com/errata-ai/Google>`_
    An implementation of the style guide for the `Google developer
    documentation
    style guide <https://developers.google.com/style/>`__.
`write-good <https://github.com/errata-ai/write-good>`_
    An implementation of the guidelines enforced by the `write-good
    <https://github.com/btford/write-good>`__ linter.
`proselint <https://github.com/errata-ai/Joblint>`_
    An implementation of the guidelines enforced by the `proselint
    <https://github.com/amperser/proselint/>`__ linter.
`Joblint <https://github.com/errata-ai/Joblint>`_
    An implementation of the directives enforced by the `Joblint
    <https://github.com/rowanmanning/joblint>`__ linter.

Vale is configured in the :file:`.vale.ini` file:

.. code-block:: ini
   :caption: .vale.ini

   StylesPath = styles
   MinAlertLevel = suggestion
   Packages = https://github.com/cusyio/cusy-vale/archive/refs/tags/v0.1.0.zip

   [*.{md,rst}]
   BasedOnStyles = cusy-en

.. seealso::
   * `Vale Configuration <https://vale.sh/docs/topics/config/>`_

You should then update your :ref:`.gitignore <gitignore>` file if necessary:

.. code-block:: ini
   :caption: .gitignore

   styles/*

You can configure Vale for the :doc:`pre-commit
<Python4DataScience:productive/git/advanced/hooks/pre-commit>` framework with:

.. code-block:: yaml
   :caption: .pre-commit-config.yaml

   - repo: https://github.com/errata-ai/vale
     rev: v3.7.1
     hooks:
     - id: vale sync
       pass_filenames: false
       args: [sync]
     - id: vale
       args: [--output=line, --minAlertLevel=error, .]

.. _docstrings-coverage:

Docstrings coverage
-------------------

`interrogate <https://interrogate.readthedocs.io/en/latest/>`_ checks your
codebase for missing documentation strings and generates a `shields.io-like
badge <https://interrogate.readthedocs.io/en/latest/#other-usage>`_.

You can configure ``interrogate`` in the :ref:`pyproject-toml` file, for
example:

.. code-block:: toml
   :caption: pyproject.toml
   :emphasize-lines: 4, 8-

   [project.optional-dependencies]
   tests = [
       "coverage[toml]",
       "interrogate",
       "pytest>=6.0",
   ]

   [tool.interrogate]
   ignore-init-method = true
   ignore-init-module = false
   ignore-magic = false
   ignore-semiprivate = false
   ignore-private = false
   ignore-module = false
   ignore-property-decorators = false
   fail-under = 95
   exclude = ["tests/functional/sample", "setup.py", "docs"]
   verbose = 0
   omit-covered-files = false
   quiet = false
   whitelist-regex = []
   ignore-regex = []
   color = true

.. seealso::

   * `Configuration <https://interrogate.readthedocs.io/en/latest/index.html#configuration>`_

You can now insert ``interrogate`` into your :doc:`../../test/tox` file, for
example with

.. code-block:: ini
   :caption: tox.ini

   [testenv:doc]
   deps = interrogate
   skip_install = true
   commands =
       interrogate --quiet --fail-under 95 src tests

You can also use ``interrogate`` with :doc:`pre-commit
<Python4DataScience:productive/git/advanced/hooks/pre-commit>`:

.. code-block:: yaml
   :caption: .pre-commit-config.yaml

   repos:
     - repo: https://github.com/econchick/interrogate
       rev: 1.7.0
       hooks:
         - id: interrogate
           args: [--quiet, --fail-under=95]
           pass_filenames: false
