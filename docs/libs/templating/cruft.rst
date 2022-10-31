cruft
=====

One problem with cookiecutter templates is that projects based on older versions
of the template become obsolete when only the template is adapted to changing
requirements over time. `cruft <https://cruft.github.io/cruft/>`_ tries to
simplify the transfer of changes in the :doc:`Cookiecutter-Templates
<templates>`’s Git repository to projects derived from it.

The main features of cruft are:

* With ``cruft check`` you can quickly check if a project uses the latest
  version of a template. This check can also be easily integrated into CI
  pipelines to ensure that your projects are in sync.
* cruft also automates the update of projects from cookiecutter templates.

Installation
------------

.. code-block:: console

    $ python3.8 -m pip install cruft

Create a new project
--------------------

To create a new project with cruft, you can run :samp:`cruft create
{PROJECT_URL}` on the command line, for example:

.. code-block:: console

    $ cruft create https://github.com/veit/cookiecutter-namespace-template
    full_name [Veit Schiele]:
    …

cruft uses :doc:`Cookiecutter <features>` for this and the only difference in
the resulting output is a :file:`.cruft.json` file that contains the git hash of
the template used as well as the specified parameters.

.. tip::

    Certain files are rarely suitable for updating, for example test cases or
    :file:`__init__` files. You can tell cruft to always skip updating these
    files in a project by creating the project with the arguments
    :samp:`--skip vsc/__init__.py --skip tests` or manually adding them to a
    skip section in your :file:`.cruft.json` file:

    .. code-block:: javascript
        :emphasize-lines: 4-7

        {
          "template": "https://github.com/veit/cookiecutter-namespace-template",
          "commit": "521d4b2aa603aec186cd7e542295edb458ba4552",
          "skip": [
              "vsc/__init__.py",
              "tests"
          ],
          "checkout": null,
          "context": {
            "cookiecutter": {
              "full_name": "Veit Schiele",
              ...
            }
          },
          "directory": null
        }

Updating a project
------------------

To update an existing project that was created with cruft, you can run ``cruft
update`` in the root directory of the project. If there are updates, cruft will
first ask you to review them. If you accept the changes, cruft will apply them
to your project and update the :file:`.cruft.json` file.

Checking a project
------------------

To see if a project has missed a template update, you can easily call ``cruft
check``. If the project is out of date, an error and exit code 1 will be
returned. ``cruft check`` can also be added to
:doc:`jupyter-tutorial:productive/git/pre-commit` and CI pipelines to ensure
projects don’t become unintentionally stale.

Linking an existing project
---------------------------

If you have an existing project that you created in the past with Cookiecutter
directly from a template, you can :samp:`cruft link {TEMPLATE_REPOSITORY}` to
link it to the template it was created with, for example:

.. code-block:: console

    $ cruft link https://github.com/veit/cookiecutter-namespace-template

You can then specify the last commit of the template that updated the project,
or accept the default to use the last commit.

Show diff
---------

Over time, your project may differ greatly from the actual cookiecutter
template. ``cruft diff`` allows you to quickly see what has changed in your
local project compared to the template.
