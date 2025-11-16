Plugins
=======

As powerful as pytest is, it can do even more when we add plugins. The pytest
codebase is designed to allow customisation and extensions, and there are hooks
that allow changes and improvements through plugins.

You may be surprised to find that you have already written some plugins if you
have worked through the previous sections. Every time you add fixtures or hook
functions to a project’s :file:`conftest.py` file, you are creating a local
plugin. It’s just a little extra work to turn these :file:`conftest.py` files
into installable plugins that you can share between projects, with other people,
or with the world.

But first, let’s start with where you can find third-party plugins. There are
quite a few plugins out there, so there’s a good chance that any changes you
want to make to pytest have already been written.

Finding plugins
---------------

You can find third-party pytest plugins in various places, for example the
:doc:`pytest documentation <pytest:reference/plugin_list>` contains an
alphabetical list of plugins from :term:`pypi.org`. You can also search pypi.org
itself, for `pytest <https://pypi.org/search/?q=pytest>`_ or for the `pytest
framework <https://pypi.org/search/?q=&c=Framework+%3A%3A+Pytest>`_. Finally,
many popular pytest plugins can also be found in `pytest-dev
<https://github.com/pytest-dev>`_ on GitHub.

Installing plugins
------------------

Like other Python packages, pytest plugins can be easily installed with
:term:`pip`: :samp:`python -m pip install {pytest-cov}`.

Plugins for …
-------------

… modified test sequences
~~~~~~~~~~~~~~~~~~~~~~~~~

pytest usually executes our tests in a predictable order. For a directory of
test files, pytest executes each file in alphabetical order. Within each file,
each test is executed in the order in which it appears in the file. However, it
can sometimes be useful to change this order. The following plugins change the
usual sequence of a test:

.. _xdist-plugin:

`pytest-xdist <https://pypi.org/project/pytest-xdist/>`_
    executes tests in parallel, either with several CPUs on one machine or
    several remote machines.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-xdist
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-xdist/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-xdist
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-xdist/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-xdist
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-xdist/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-xdist
       :alt: License
       :target: https://github.com/pytest-dev/pytest-xdist?tab=MIT-1-ov-file#readme

`pytest-freethreaded <https://pypi.org/project/pytest-freethreaded/>`_
    for checking whether tests and libraries are thread-safe with Python 3.13’s
    experimental freethreaded mode.

    .. image:: https://raster.shields.io/github/stars/tonybaloney/pytest-freethreaded
       :alt: Stars
       :target: https://github.com/tonybaloney/pytest-freethreaded/stargazers
    .. image:: https://raster.shields.io/github/contributors/tonybaloney/pytest-freethreaded
       :alt: Contributors
       :target: https://github.com/tonybaloney/pytest-freethreaded/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/tonybaloney/pytest-freethreaded
       :alt: Commit activity
       :target: https://github.com/tonybaloney/pytest-freethreaded/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/tonybaloney/pytest-freethreaded
       :alt: License
       :target: https://github.com/tonybaloney/pytest-freethreaded?tab=MIT-1-ov-file#readme

`pytest-rerunfailures <https://pypi.org/project/pytest-rerunfailures/>`_
    re-executes failed tests and is particularly helpful in the case of faulty
    tests.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-rerunfailures
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-rerunfailures
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-rerunfailures
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-rerunfailures/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-rerunfailures
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-rerunfailures/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-rerunfailures
       :alt: License
       :target: https://github.com/pytest-dev/pytest-rerunfailures?tab=License-1-ov-file#readme

`pytest-repeat <https://pypi.org/project/pytest-repeat/>`_
    makes it easy to repeat one or more tests.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-repeat
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-repeat/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-repeat
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-repeat/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-repeat
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-repeat/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-repeat
       :alt: License
       :target: https://github.com/pytest-dev/pytest-repeat?tab=License-1-ov-file#readme

`pytest-order <https://pypi.org/project/pytest-order/>`_
    enables the order to be defined using :doc:`markers`.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-order
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-order/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-order
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-order/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-order
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-order/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-xdist
       :alt: License
       :target: https://github.com/pytest-dev/pytest-xdist?tab=MIT-1-ov-file#readme

`pytest-randomly <https://pypi.org/project/pytest-randomly/>`_
    runs the tests in random order, first by file, then by class, then by test
    file.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-randomly
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-randomly/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-randomly
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-randomly/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-randomly
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-randomly/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-randomly
       :alt: License
       :target: https://github.com/pytest-dev/pytest-randomly?tab=MIT-1-ov-file#readme

… modified output
~~~~~~~~~~~~~~~~~

The normal pytest output mainly shows dots for passed tests and characters for
other output. If you pass ``-v``, you will see a list of test names with the
result. However, there are plugins that change the output even further:

`pytest-instafail <https://pypi.org/project/pytest-instafail/>`_
    adds a ``--instafail`` option that reports tracebacks and output from failed
    tests immediately after the failure. Normally, pytest reports tracebacks and
    output from failed tests only after all tests have completed.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-instafail
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-instafail/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-instafail
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-instafail/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-instafail
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-instafail/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-instafail
       :alt: License
       :target: https://github.com/pytest-dev/pytest-rerunfailures?tab=License-1-ov-file#readme

`pytest-edit <https://pypi.org/project/pytest-edit/>`_
    opens an editor after a failed test.

    .. image:: https://raster.shields.io/github/stars/mrmino/pytest-edit
       :alt: Stars
       :target: https://github.com/mrmino/pytest-edit/stargazers
    .. image:: https://raster.shields.io/github/contributors/mrmino/pytest-edit
       :alt: Contributors
       :target: https://github.com/mrmino/pytest-edit
    .. image:: https://raster.shields.io/github/commit-activity/y/mrmino/pytest-edit
       :alt: Commit activity
       :target: https://github.com/mrmino/pytest-edit/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/mrmino/pytest-edit
       :alt: License
       :target: https://github.com/mrmino/pytest-edit?tab=MIT-1-ov-file#readme

`pytest-sugar <https://pypi.org/project/pytest-sugar/>`_
    shows green checkmarks instead of dots for passed tests and has a nice
    progress bar. Like pytest-instafail, it also shows failures immediately.

    .. image:: https://raster.shields.io/github/stars/Teemu/pytest-sugar
       :alt: Stars
       :target: https://github.com/Teemu/pytest-sugar/stargazers
    .. image:: https://raster.shields.io/github/contributors/Teemu/pytest-sugar
       :alt: Contributors
       :target: https://github.com/Teemu/pytest-sugar/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/Teemu/pytest-sugar
       :alt: Commit activity
       :target: https://github.com/Teemu/pytest-sugar/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/Teemu/pytest-sugar
       :alt: License
       :target: https://github.com/Teemu/pytest-sugar?tab=License-1-ov-file#readme

`pytest-html <https://pypi.org/project/pytest-html/>`_
    enables the creation of HTML reports. Reports can be extended with
    additional data and images, such as screenshots of error cases.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-html
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-html/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-html
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-html/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-html
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-html/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-html
       :alt: License
       :target: https://github.com/pytest-dev/pytest-html?tab=License-1-ov-file#readme

`pytest-icdiff <https://pypi.org/project/pytest-icdiff/>`_
    improves diffs in the error messages of the pytest assertion with `ICDiff
    <https://www.jefftk.com/icdiff>`_.

    .. image:: https://raster.shields.io/github/stars/hjwp/pytest-icdiff
       :alt: Stars
       :target: https://github.com/hjwp/pytest-icdiff/stargazers
    .. image:: https://raster.shields.io/github/contributors/hjwp/pytest-icdiff
       :alt: Contributors
       :target: https://github.com/hjwp/pytest-icdiff/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/hjwp/pytest-icdiff
       :alt: Commit activity
       :target: https://github.com/hjwp/pytest-icdiff/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/hjwp/pytest-icdiff
       :alt: License
       :target: https://github.com/hjwp/pytest-icdiff?tab=MIT-1-ov-file#readme

… web development
~~~~~~~~~~~~~~~~~

pytest is used extensively for testing web projects and there is a long list of
plugins that further simplify testing:


`pytest-httpx <https://pypi.org/project/pytest-httpx/>`_
    facilitates the testing of `HTTPX <https://www.python-httpx.org>`_ and
    `FastAPI <https://fastapi.tiangolo.com>`_ applications.

    .. image:: https://raster.shields.io/github/stars/Colin-b/pytest_httpx
       :alt: Stars
       :target: https://github.com/Colin-b/pytest_httpx/stargazers
    .. image:: https://raster.shields.io/github/contributors/Colin-b/pytest_httpx
       :alt: Contributors
       :target: https://github.com/Colin-b/pytest_httpx/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/Colin-b/pytest_httpx
       :alt: Commit activity
       :target: https://github.com/Colin-b/pytest_httpx/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/Colin-b/pytest_httpx
       :alt: License
       :target: https://github.com/Colin-b/pytest_httpx?tab=MIT-1-ov-file#readme

`Playwright for Python <https://pypi.org/project/playwright/>`_
    was specially developed for end-to-end testing. Playwright supports all
    modern rendering engines such as Chromium, WebKit and Firefox with a single
    :abbr:`API (Application Programming Interface)`.

    .. image:: https://raster.shields.io/github/stars/Microsoft/playwright-python
       :alt: Stars
       :target: https://github.com/Microsoft/playwright-python/stargazers
    .. image:: https://raster.shields.io/github/contributors/Microsoft/playwright-python
       :alt: Contributors
       :target: https://github.com/Microsoft/playwright-python/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/Microsoft/playwright-python
       :alt: Commit activity
       :target: https://github.com/Microsoft/playwright-python/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/Microsoft/playwright-python
       :alt: License
       :target: https://github.com/Microsoft/playwright-python?tab=MIT-1-ov-file#readme

`pyleniumio <https://pypi.org/project/pyleniumio/>`_
    is a thin Python wrapper around Selenium with simple and clear syntax.

    .. image:: https://raster.shields.io/github/stars/ElSnoMan/pyleniumio
       :alt: Stars
       :target: https://github.com/ElSnoMan/pyleniumio/stargazers
    .. image:: https://raster.shields.io/github/contributors/ElSnoMan/pyleniumio
       :alt: Contributors
       :target: https://github.com/ElSnoMan/pyleniumio/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/ElSnoMan/pyleniumio
       :alt: Commit activity
       :target: https://github.com/ElSnoMan/pyleniumio/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/ElSnoMan/pyleniumio
       :alt: License
       :target: https://github.com/ElSnoMan/pyleniumio?tab=MIT-1-ov-file#readme

`pytest-selenium <https://pypi.org/project/pytest-selenium/>`_
    provides fixtures that enable simple configuration of browser-based tests
    with `Selenium <https://www.selenium.dev>`_.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-selenium
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-selenium/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-selenium
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-selenium
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-selenium
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-selenium/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-selenium
       :alt: License
       :target: https://github.com/pytest-dev/pytest-selenium?tab=License-1-ov-file#readme

.. _fake_plugins:

… fake data
~~~~~~~~~~~

We have already used `Faker <https://pypi.org/project/Faker/>`_ in
:ref:`marker_fixtures_combined` to create multiple item instances. There are
many cases in different areas where it is helpful to generate fake data. It is
therefore not surprising that there are several plugins that fulfil this need:

`Faker <https://pypi.org/project/Faker/>`_
    generates fake data for you and offers a faker fixture for use with pytest.

    .. image:: https://raster.shields.io/github/stars/joke2k/faker
       :alt: Stars
       :target: https://github.com/joke2k/faker/stargazers
    .. image:: https://raster.shields.io/github/contributors/joke2k/faker
       :alt: Contributors
       :target: https://github.com/joke2k/faker/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/joke2k/faker
       :alt: Commit activity
       :target: https://github.com/joke2k/faker/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/joke2k/faker
       :alt: License
       :target: https://github.com/joke2k/faker?tab=MIT-1-ov-file#readme

`time-machine <https://github.com/adamchainz/time-machine>`_
    provides both a fixture and a marker to control the time during testing.

    .. image:: https://raster.shields.io/github/stars/adamchainz/time-machine
       :alt: Stars
       :target: https://github.com/pytest-dev/adamchainz/time-machine

    .. image:: https://raster.shields.io/github/contributors/adamchainz/time-machine
       :alt: Contributors
       :target: https://github.com/adamchainz/time-machine/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/adamchainz/time-machine
       :alt: Commit activity
       :target: https://github.com/adamchainz/time-machine/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/adamchainz/time-machine
       :alt: License
       :target: https://github.com/adamchainz/time-machine?tab=MIT-1-ov-file

`pytest-factoryboy <https://pypi.org/project/pytest-factoryboy/>`_
    contains fixtures for `factory-boy
    <https://pypi.org/project/factory-boy/>`_, a database model data generator.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-factoryboy
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-factoryboy/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-factoryboy
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-factoryboy/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-factoryboy
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-factoryboy/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-factoryboy
       :alt: License
       :target: https://github.com/pytest-dev/pytest-factoryboy?tab=MIT-1-ov-file#readme

… various things
~~~~~~~~~~~~~~~~

`pytest-testinfra <https://github.com/pytest-dev/pytest-testinfra>`_
    is a `Serverspec <https://serverspec.org/>`_ equivalent for pytest to test
    the current status of your servers with management tools such as `Salt
    <https://saltproject.io>`_, `Ansible
    <https://www.redhat.com/en/ansible-collaborative>`_, `Puppet
    <https://www.puppet.com>`_, `Chef <https://www.chef.io>`_ and so on.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-testinfra
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-testinfra/stargazers

    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-testinfra
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-testinfra/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-testinfra
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-testinfra/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-testinfra
       :alt: License
       :target: https://github.com/pytest-dev/pytest-testinfra?tab=Apache-2.0-1-ov-file

`pytest-cov <https://pypi.org/project/pytest-cov/>`_
    executes the  :doc:`../pytest/coverage` during testing.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-cov
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-cov/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-cov
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-cov/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-cov
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-cov/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-cov
       :alt: License
       :target: https://github.com/pytest-dev/pytest-cov?tab=MIT-1-ov-file#readme

`pytest-benchmark <https://pypi.org/project/pytest-benchmark/>`_
    performs benchmark timing for code within tests.

    .. image:: https://raster.shields.io/github/stars/ionelmc/pytest-benchmark
       :alt: Stars
       :target: https://github.com/ionelmc/pytest-benchmark/stargazers
    .. image:: https://raster.shields.io/github/contributors/ionelmc/pytest-benchmark
       :alt: Contributors
       :target: https://github.com/ionelmc/pytest-benchmark/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/ionelmc/pytest-benchmark
       :alt: Commit activity
       :target: https://github.com/ionelmc/pytest-benchmark/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/ionelmc/pytest-benchmark
       :alt: License
       :target: https://github.com/ionelmc/pytest-benchmark?tab=BSD-2-Clause-1-ov-file#readme

`pytest-timeout <https://pypi.org/project/pytest-timeout/>`_
    prevents tests from running too long.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-timeout
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-timeout/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-timeout
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-timeout/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-timeout
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-timeout/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-timeout
       :alt: License
       :target: https://github.com/pytest-dev/pytest-timeout?tab=MIT-1-ov-file#readme

`pytest-asyncio <https://pypi.org/project/pytest-asyncio/>`_
    tests asynchronous functions.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-asyncio
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-asyncio/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-asyncio
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-asyncio/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-asyncio
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-asyncio/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-asyncio
       :alt: License
       :target: https://github.com/pytest-dev/pytest-asyncio?tab=MIT-1-ov-file#readme

`pytest-mock <https://pypi.org/project/pytest-mock/>`_
    is a thin wrapper around the  :doc:`unittest.mock <../mock>` patching API.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-mock
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-mock/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-mock
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-mock/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-mock
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-mock/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-mock
       :alt: License
       :target: https://github.com/pytest-dev/pytest-mock?tab=MIT-1-ov-file#readme

`pytest-patterns <https://pypi.org/project/pytest-patterns/>`_
    provides a pattern matching engine optimised for tests.

    .. image:: https://raster.shields.io/github/stars/flyingcircusio/pytest-patterns
       :alt: Stars
       :target: https://github.com/flyingcircusio/pytest-patterns/stargazers
    .. image:: https://raster.shields.io/github/contributors/flyingcircusio/pytest-patterns
       :alt: Contributors
       :target: https://github.com/flyingcircusio/pytest-patterns/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/flyingcircusio/pytest-patterns
       :alt: Commit activity
       :target: https://github.com/flyingcircusio/pytest-patterns/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/flyingcircusio/pytest-patterns
       :alt: License
       :target: https://github.com/flyingcircusio/pytest-patterns?tab=MIT-1-ov-file#readme

:doc:`pytest-grpc <Python4DataScience:data-processing/apis/grpc/test>`
    is a Pytest plugin for
    :doc:`Python4DataScience:data-processing/apis/grpc/index`.

    .. image:: https://raster.shields.io/github/stars/kataev/pytest-grpc
       :alt: Stars
       :target: https://github.com/kataev/pytest-grpc/stargazers
    .. image:: https://raster.shields.io/github/contributors/kataev/pytest-grpc
       :alt: Contributors
       :target: https://github.com/kataev/pytest-grpc/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/kataev/pytest-grpc
       :alt: Commit activity
       :target: https://github.com/kataev/pytest-grpc/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/kataev/pytest-grpc
       :alt: License
       :target: https://github.com/kataev/pytest-grpc?tab=MIT-1-ov-file#readme

`pytest-bdd <https://pypi.org/project/pytest-bdd/>`_
    writes :abbr:`BDD (Behavior Driven Development)` tests with pytest.

    .. image:: https://raster.shields.io/github/stars/pytest-dev/pytest-bdd
       :alt: Stars
       :target: https://github.com/pytest-dev/pytest-bdd/stargazers
    .. image:: https://raster.shields.io/github/contributors/pytest-dev/pytest-bdd
       :alt: Contributors
       :target: https://github.com/pytest-dev/pytest-bdd/graphs/contributors
    .. image:: https://raster.shields.io/github/commit-activity/y/pytest-dev/pytest-bdd
       :alt: Commit activity
       :target: https://github.com/pytest-dev/pytest-bdd/graphs/commit-activity
    .. image:: https://raster.shields.io/github/license/pytest-dev/pytest-bdd
       :alt: License
       :target: https://github.com/pytest-dev/pytest-bdd?tab=MIT-1-ov-file#readme

Own plugins
-----------

.. seealso::
   * `Writing plugins
     <https://docs.pytest.org/en/latest/how-to/writing_plugins.html>`_
