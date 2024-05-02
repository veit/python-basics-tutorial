Testing
=======

Formatting
----------

Whether the :doc:`Sphinx <start>` documentation is written in valid :doc:`rest`
format can be checked with `sphinx-lint
<https://pypi.org/project/sphinx-lint/>`_. We usually include this in our
:doc:`pre-commit
<Python4DataScience:productive/git/advanced/hooks/pre-commit>` configuration:

.. code-block:: yaml
   :caption: .pre-commit-config.yaml

   - repo: https://github.com/sphinx-contrib/sphinx-lint
     rev: v0.9.1
     hooks:
       - id: sphinx-lint
         args: [--jobs=1]
         types: [rst]

.. seealso::
   With :doc:`Sybil:index` you can not only check :doc:`rest`, but also
   :doc:`Markdown <Sybil:markdown>` and :doc:`Myst <Sybil:myst>`, for example.
   Sybil can also check code blocks in the documentation with either
   :doc:`../test/pytest/index` or :doc:`../test/unittest`.

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

.. _build-errors:

Build errors
------------

You have the option of checking whether your content is built correctly before
publishing your changes. `Sphinx <https://www.sphinx-doc.org/>`_ has a nitpicky
mode for this, which can be called up with the ``-n`` option, for example with:

.. tab:: Linux/macOS

   .. code-block:: console

       $ bin/python -m sphinx -nb html docs/ docs/_build/

.. tab:: Windows

   .. code-block:: ps1con

       C:> Scripts\python -m sphinx -nb html docs\ docs\_build\

.. _link-checks:

Check links
-----------

You can also automatically ensure that the link targets you specify are
accessible. Our documentation tool Sphinx uses a ``linkcheck`` builder for this,
which you can call up with:

.. tab:: Linux/macOS

   .. code-block:: console

       $ bin/python -m sphinx -b linkcheck docs/ docs/_build/

.. tab:: Windows

   .. code-block:: ps1con

       C:> Scripts\python -m sphinx -b linkcheck docs\ docs\_build\

The output can then look like this, for example:

.. tab:: Linux/macOS

   .. code-block:: console

       $ bin/python -m sphinx -b linkcheck docs/ docs/_build/
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

       C:> Scripts\python -m sphinx -b linkcheck docs\ docs\_build\
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
----------------------

If necessary, you can also check automatically in your :term:`CI` pipeline
whether the documentation is being built and the links are valid. In
:doc:`../test/tox`, the configuration can be added as follows:

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
