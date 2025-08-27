behave
======

`behave <https://behave.readthedocs.io/en/latest/>`_ implements behaviour-driven
development (:abbr:`BDD (Behavior-Driven Development)`). BDD is an agile
software development technique that promotes collaboration between development,
quality assurance and non-technical or business staff on a software project. The
term was originally coined in 2003 by `Daniel Terhorst-North
<https://dannorth.net/introducing-bdd>`_ in response to :term:`test-driven
development <Test-driven development>` and encompasses :term:`acceptance testing
<Acceptance test>` or customer-test-driven development practices as found in
:term:`extreme programming <Extreme programming>`. In `Selling BDD to the
Business <https://speakerdeck.com/tastapod/selling-bdd-to-the-business>`_, he
gave the following definition:

    *‚BDD is a second-generation, outside–in, pull-based, multiple-stakeholder,
    multiple-scale, high-automation, agile methodology. It describes a cycle of
    interactions with well-defined outputs, resulting in the delivery of
    working, tested software that matters.‘*

Gherkin
-------

Description language based on natural written language for the textual
specification of software requirements. Only certain keywords are predefined.

.. code-block:: gherkin

   Scenario: Add an item to the database
     Given an empty database
      When an item with a summary is added
      Then the number of items should be 1
       and the queried item from the db should correspond to the added object.

Each scenario is an example intended to illustrate a specific aspect of the
application’s behaviour.

Installation
------------

You can install behave in your :ref:`virtual environments <venv>` with:

.. tab:: Linux/macOS

   .. code-block:: console

      $ python -m pip install behave

.. tab:: Windows

   .. code-block:: ps1con

      C:> python -m pip install behave

.. toctree::
   :titlesonly:
   :hidden:

   example
