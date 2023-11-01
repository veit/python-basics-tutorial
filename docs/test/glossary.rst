Glossary
========

.. glossary::

    ``assert``
         A keyword that stops code execution if its argument is false.

    Continuous integration
    CI
        Automatic checking of the creation and test process on different
        platforms.

    Dummy
        Object that is passed around but never actually used. Normally they are
        only used to fill parameter lists.

    ``exception``
        Customisable form of :term:`assert`.

    ``except``
        Keyword used to catch an :term:`exception` and handle it carefully.

    Fake
        Object that has an actual working implementation, but usually takes a
        shortcut that makes it unsuitable for production.

    Integration test
        Tests that verify that the different parts of the software work together
        as expected.

    Mock
        Objects that are programmed with :term:`exception` that form a
        specification of the calls you are likely to receive.

        .. seealso::
           * `Mock object <https://en.wikipedia.org/wiki/Mock_object>`_

    pytest
        A Python package with test utilities.

    Regression test
        Test to protect against new errors or regressions that can occur due to
        new software and updates.

    Stubs
        provide ready-made responses to calls made during the test and usually
        do not respond at all to anything that has not been programmed for the
        test.

    Test-driven development
    TDD
        A software development strategy in which the tests are written before the
        code.

    ``try``
        A keyword that protects a part of the code that can trigger an
        :term:`exception`.
