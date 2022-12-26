Testing
=======

.. _build-errors:

Build error
-----------

You have the option of checking that your content is built correctly before
publishing your changes. For this purpose, `Sphinx
<https://www.sphinx-doc.org/>`_ has a nitpicky mode that can be invoked with the
``-n`` option, for example with:


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
accessible. Sphinx uses a linkcheck builder for this purpose, which you can call
with:


.. tab:: Linux/macOS

   .. code-block:: console

       $ bin/python -m sphinx -b linkcheck docs/ docs/_build/

.. tab:: Windows

   .. code-block:: ps1con

       C:> Scripts\python -m sphinx -b linkcheck docs\ docs\_build\

The output may then look like this:


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

Code formatting
 --------------

`blacken-docs <https://github.com/adamchainz/blacken-docs>`_ currently supports
the following `black <https://github.com/psf/black>`_ options:

 * ``-l``/``--line-length``
 * ``-t``/``--target-version``
 * ``-s``/``--skip-string-normalization``
 * ``-E``/``--skip-errors``

.. code-block:: console

    $ bin/python -m pip install blacken-docs
