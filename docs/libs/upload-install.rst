Upload package
==============

Finally, you can deploy the package on the :term:`Python Package Index`
(:term:`PyPI`) or another index, for example :doc:`gitlab` or :term:`devpi`.

For this you should register on *Test PyPI*. *Test-PyPI* is a separate instance
that is intended for testing and experimentation. To set up an account there, go
to  https://test.pypi.org/account/register/. For more information, see `Using
TestPyPI <https://packaging.python.org/en/latest/guides/using-testpypi/>`_.

Now you can create the :file:`~/.pypirc` file:

.. code-block:: ini

    [distutils]
    index-servers=
        test

    [test]
    repository = https://test.pypi.org/legacy/
    username = veit

.. seealso::
    If you’d like to automate PyPI registration, read `Careful With That PyPI
    <https://glyph.twistedmatrix.com/2017/10/careful-with-that-pypi.html>`_.

After you are registered, you can upload your :term:`Distribution Package` with
:term:`twine`. To do this, however, you must first install twine with:

.. code-block:: console

    $ python -m pip install --upgrade pip build twine
    …
    All dependencies are now up-to-date!

.. note::
   Run this command before each release to ensure that all release tools are up
   to date.

Now you can create your :term:`Distribution Packages <Distribution Package>`
with:

.. code-block:: console

    $ cd /path/to/your/distribution_package
    $ rm -rf build dist
    $ python -m build

After installing Twine you can upload all archives in ``/dist`` to the Python
Package Index with:

.. code-block:: console

    $ twine upload -r test -s dist/*

``-r``, ``--repository``
    The repository to upload the package.

    In our case, the ``test`` section from the :file:`~/.pypirc` file is used.

``-s``, ``--sign``
    signs the files to be uploaded with GPG.

You will be asked for the password you used to register on *Test PyPI*. You
should then see a similar output:

.. code-block:: console

    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: veit
    Enter your password:
    Uploading example-0.0.1-py3-none-any.whl
    100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
    Uploading example-0.0.1.tar.gz
    100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]

.. note::
   If you get an error message similar to

   .. code-block:: console

    The user 'veit' isn't allowed to upload to project 'example'

   you have to choose a unique name for your package:

   #. change the ``name`` argument in the :file:`setup.py` file
   #. remove the ``dist`` directory
   #. regenerate the archives

Check
-----

Installation
~~~~~~~~~~~~

You can use ``pip`` to install your package and check if it works. Create
a new :term:`virtual environment` and install your package on *Test PyPI*:

.. code-block:: console

    $ python3 -m venv test_env
    $ source test_env/bin/activate
    $ pip install -i https://test.pypi.org/simple/ minimal_example

.. note::
   If you have used a different package name, replace it with your package name
   in the command above.

:term:`pip` should install the package from *Test PyPI* and the output should
look something like this:

.. code-block:: console

    Looking in indexes: https://test.pypi.org/simple/
    Collecting minimal_example
      …
    Installing collected packages: minimal_example
    Successfully installed minimal_example-0.0.1

You can test whether your package has been installed correctly by importing the
module and referencing the ``name`` property that was previously ntered in
``__init__.py``:

.. code-block:: console

    $ python
    Python 3.13.0 (main, Oct  7 2024, 05:02:14) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
    …
    >>> import minimal_example
    >>> minimal_example.name
    'minimal_example'

.. note::

    The packages on *Test-PyPI* are only stored temporarily. If you want to
    upload a package to the real :term:`Python Package Index` (:term:`PyPI`),
    you can do so by creating an account on :term:`pypi.org` and following the
    same instructions, but using ``twine upload dist/*``.

README
~~~~~~

Also check whether the ``README.rst`` is displayed correctly on the test PyPI
page.

PyPI
----

Now register on the :term:`Python Package Index` (:term:`PyPI`) and make sure
that `two-factor authentication
<https://blog.python.org/2019/05/use-two-factor-auth-to-improve-your.html>`_
is activated by adding the following to the :file:`~/.pypirc` file:

.. code-block:: ini

    [distutils]
    index-servers=
        pypi
        test

    [test]
    repository = https://test.pypi.org/legacy/
    username = veit

    [pypi]
    username = __token__

With this configuration, the name/password combination is no longer used for
uploading but an upload token.

.. seealso::
    * `PyPI now supports uploading via API token
      <https://pyfound.blogspot.com/2019/07/pypi-now-supports-uploading-via-api.html>`_
    * `What is two factor authentication and how does it work on PyPI?
      <https://pypi.org/help/#twofa>`_

Finally, you can publish your package on PyPI:

.. code-block:: console

    $ twine upload -r pypi -s dist/*

.. note::
    You cannot simply replace releases as you cannot re-upload packages with the
    same version number.

.. note::
    Do not remove old versions from the Python Package Index.This only causes
    work for those who want to keep using that version and then have to switch
    to old versions on GitHub. PyPI has a `yank
    <https://pypi.org/help/#yanked>`_ function that you can use instead. This
    will ignore a particular version if it is not explicitly specified with
    ``==`` or ``===``.

.. seealso::
    * `PyPI Release Checklist
      <https://cookiecutter-namespace-template.readthedocs.io/en/latest/pypi-release-checklist.html>`_

GitHub Action
-------------

You can also create a GitHub action, which creates a package and uploads it to
PyPI at every time a release is created. Such a
:file:`.github/workflows/pypi.yml` file could look like this:

.. code-block:: yaml
   :linenos:

   name: Publish Python Package

    on:
      release:
        types: [created]

   jobs:
     test:
       …
     package-and-deploy:
       runs-on: ubuntu-latest
       needs: [test]
       steps:
       - name: Checkout
         uses: actions/checkout@v2
         with:
           fetch-depth: 0
       - name: Set up Python
         uses: actions/setup-python@v5
         with:
           python-version: '3.11'
           cache: pip
           cache-dependency-path: '**/pyproject.toml'
       - name: Install dependencies
         run: |
           python -m pip install -U pip
           python -m pip install -U setuptools build twine wheel
       - name: Build
         run: |
           python -m build
       - name: Publish
         env:
           TWINE_PASSWORD: ${{ secrets.TWINE_PASSWORD }}
           TWINE_USERNAME: ${{ secrets.TWINE_USERNAME }}
         run: |
           twine upload dist/*

Lines 3–5
    This ensures that the workflow is executed every time a new GitHub
    release is created for the repository.
Line 12
    The job waits for the ``test`` job to pass before it is executed.

.. seealso::

   * `GitHub Actions <https://docs.github.com/en/actions>`_

Trusted Publishers
------------------

`Trusted Publishers <https://docs.pypi.org/trusted-publishers/>`_ is an
alternative method for publishing packages on the :term:`PyPI`. It is based on
OpenID Connect and requires neither a password nor a token. Only the following
steps are required:

#. Add a *Trusted Publishers* on PyPI

   Depending on whether you want to publish a new package or update an existing
   one, the process is slightly different:

   * to update an existing package, see `Adding a trusted publisher to an
     existing PyPI project
     <https://docs.pypi.org/trusted-publishers/adding-a-publisher/>`_
   * to publish a new package, there is a special procedure called *Pending
     Publisher*; see also `Creating a PyPI project with a trusted publisher
     <https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/>`_

     You can also use it to reserve a package name before you publish the first
     version. This allows you to ensure that you can publish the package under
     the desired name.

     To do this, you need to create a new *Pending Publisher* in
     `pypi.org/manage/account/publishing/
     <https://pypi.org/manage/account/publishing/>`_ with

     * Name of the PyPI project
     * GitHub repository owner
     * Name of the workflow, for example :file:`publish.yml`
     * Name of the environment (optional), for example ``release``

#. Create an environment for the GitHub actions

   If we have specified an environment on :term:`PyPI`, we must now also create
   it. This can be done in :menuselection:`Settings --> Environments` for the
   repository. The name of our environment is ``release``.

#. Configure the workflow

   To do this, we now create the :file:`.github/workflows/publish.yml` file in
   our repository:

   .. code-block:: yaml
      :linenos:

      …
      jobs:
        …
        deploy:
          runs-on: ubuntu-latest
          environment: release
          permissions:
            id-token: write
          needs: [test]
          steps:
          - name: Checkout
            …
          - name: Set up Python
            …
          - name: Install dependencies
            …
          - name: Build
            …
          - name: Publish
            uses: pypa/gh-action-pypi-publish@release/v1

   Line 6
       This is needed because we have configured an environment in :term:`PyPI`.
   Lines 7–8
       They are required for the OpenID Connect token authentication to work.
   Lines 19–20
       The package uses the `github.com/pypa/gh-action-pypi-publish
       <https://github.com/pypa/gh-action-pypi-publish>`_ action to publish the
       package.
