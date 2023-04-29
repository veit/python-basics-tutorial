Coverage
========

You can create a report for the test coverage with `Coverage.py
<https://github.com/nedbat/coveragepy>`_.

.. seealso::
   * `GitHub <https://github.com/nedbat/coveragepy>`_
   * `Docs <https://coverage.readthedocs.io/>`_

Installation
------------

.. tab:: Linux/macOS

   .. code-block:: console

      $ bin/python -m pip install coverage

.. tab:: Windows

   .. code-block:: ps1con

         C:> Scripts\python -m pip install coverage

.. note::
   If you want to determine the test coverage for Python 2 and Python<3.6, you
   must use Coverage<6.0.

Use
---

You can run your usual test runner together with Coverage

* … mit `pytest <https://docs.pytest.org/>`_:

  .. tab:: Linux/macOS

     .. code-block:: console

        $ bin/python -m pip install pytest-cov

  .. tab:: Windows

     .. code-block:: ps1con

        C:> Scripts\python -m pip install pytest-cov

  or for distributed tests

  .. tab:: Linux/macOS

     .. code-block:: console

        $ bin/python -m pip install pytest-xdist

  .. tab:: Windows

     .. code-block:: ps1con

        C:> Scripts\python -m pip install pytest-xdist

  You can then check the test coverage with

  .. tab:: Linux/macOS

     .. code-block:: console

        $ bin/pytest --cov=myproj tests/

  .. tab:: Windows

     .. code-block:: ps1con

        C:> Scripts\pytest --cov=myproj tests\

  .. seealso::
     * `pytest-cov’s documentation <https://pytest-cov.readthedocs.io/>`_

* … with :doc:`unittest`:

  .. tab:: Linux/macOS

     .. code-block:: console

        $ bin/coverage run -m unittest discover

  .. tab:: Windows

     .. code-block:: ps1con

        C:> Scripts\coverage run -m unittest discover

* … with `nose <https://nose.readthedocs.io/>`_:

  .. tab:: Linux/macOS

     .. code-block:: console

        $ bin/coverage run -m nose arg1 arg2

  .. tab:: Windows

     .. code-block:: ps1con

        C:> Scripts\coverage run -m nose arg1 arg2

Extensions
----------

In `Coverage.py plugins
<https://gist.github.com/nedbat/2e9dbf7f33b1e0e857368af5c5d06202>`_ you will
find a number of extensions for Coverage.

.. _coverage-github-actions:

Test coverage of all tests with GitHub actions
----------------------------------------------

After you have checked the test coverage, you can upload the files as GitHub
actions, for example in a :download:`tests.yaml` as artefacts, to be able to
reuse them later in other jobs:

.. literalinclude:: tests.yaml
   :language: yaml
   :lines: 49-54
   :lineno-start: 49

``if-no-files-found: ignore``
    is useful if the test coverage is not to be measured for all Python versions
    in order to get the result more quickly. Therefore, you should only upload
    the data for those elements of your matrix that you want to consider.

After all tests have been run, you can define another job that combines the
results:

.. literalinclude:: tests.yaml
   :language: yaml
   :lines: 56-94
   :lineno-start: 56

``needs: tests``
    ensures that all tests are performed. If your job that runs the tests has
    a different name, you need to change it here.
``name: "Download coverage data"``
    downloads the test coverage data previously uploaded with ``name: "Upload
    coverage data"``.
``name: "Combine coverage and fail it it’s under 100 %"``
    combines the test coverage and creates an HTML report if the condition ``--fail-under=100`` is met.

Once the workflow is complete, you can download the HTML report from
:menuselection:`YOUR_REPO --> Actions --> tests --> Combine and check coverage`.

.. seealso::
   * `How to Ditch Codecov for Python Projects
     <https://hynek.me/articles/ditch-codecov-python/>`_
   * `structlog main.yml
     <https://github.com/hynek/structlog/blob/main/.github/workflows/ci.yml>`_

.. _coverage-badge:

Badge
-----

You can use GitHub Actions to create a badge with your code coverage. In
addition, a GitHub Gist is needed to store the parameters for the badge that is
rendered by `shields.io <https://shields.io>`_. For this we extend our
:download:`tests.yaml` as follows:

.. literalinclude:: tests.yaml
   :language: yaml
   :lines: 96-
   :lineno-start: 96

Line 86
    ``GIST_TOKEN`` is a personal GitHub access token.
Line 87
    You should replace ``YOUR_GIST_ID`` with your own Gist-ID. If you don’t have
    the Gist ID yet, you can create one with:

    #. Go to https://gist.github.com and create a new gist, which you can call
       :file:`test.json`, for example. The ID of the gist is the long
       alphanumeric part of the URL, which you need here.
    #. Then go to https://github.com/settings/tokens and create a new token for
       the gist area.
    #. Finally, go to :menuselection:`YOUR_REPO --> Settings --> Secrets -->
       Actions` and add this token. You can give it any name you like, for
       example :samp:`GIST_SECRET`.

       If you use `Dependabot <https://github.com/dependabot>`_ to automatically
       update your repository’s dependencies, you will also need to add the
       :samp:`GIST_SECRET` to :menuselection:`YOUR_REPO --> Settings --> Secrets
       --> Dependabot`.

Lines 91–93
    The badge is automatically coloured:

    * ≤ 50 % in red
    * ≥ 90 % in green
    * with a colour gradient between the two.

Now the badge can be displayed with a URL like this:
:samp:`https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/{YOUR_GITHUB_NAME}/{GIST_SECRET}/raw/covbadge.json`.

.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_40.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_45.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_50.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_55.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_60.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_65.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_70.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_75.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_80.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_85.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_90.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_95.json
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/nedbat/a27aaed4944c1f760a969a543fb52767/raw/covbadge2_100.json
