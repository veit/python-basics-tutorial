Behavior-Driven Development
===========================

Dan North began talking about Behaviour-Driven Development (BDD) in 2006 to
clear up misunderstandings about :doc:`tdd`:

    *“Programmers wanted to know where to start, what to test and what not to
    test, how much to test in one go, what to call their tests, and how to
    understand why a test fails.”*

– `Introducing BDD <https://dannorth.net/blog/introducing-bdd/>`_ by Dan North

He realised that it was clearer if he told them to test behaviours rather than
functions. More specifically:

* Think of changes to the system as changes in behaviour. Deciding which test or
  series of tests to write next is easier if you think in terms of behaviours.
  What is the next most important behaviour? Write tests for that.
* Name your test functions after the expected behaviour, even if this makes the
  test names sound almost like sentences. This makes it clear what is wrong if
  the test fails. It also makes it clear which aspects you should be checking in
  the test. If a test can fail for a reason that does not match the name of the
  test, it should be a different test.
* Formulating or reformulating requirements as Given-When-Then (GWT) makes it
  easier to write tests.

Given-When-Then and Arrange-Act-Assert actually mean the same thing, but GWT
fits better with the behaviour-oriented mindset. Furthermore, :term:`acceptance
tests <Acceptance test>` can be created very easily from requirements written as
Given-When-Then.

BDD thus facilitates agile collaboration between development, quality assurance
and the product owner on a software project. In `Selling BDD to the Business
<https://speakerdeck.com/tastapod/selling-bdd-to-the-business>`_, Dan North
explores this process in more detail:

    *“BDD is a second-generation, outside–in, pull-based, multiple-stakeholder,
    multiple-scale, high-automation, agile methodology. It describes a cycle of
    interactions with well-defined outputs, resulting in the delivery of
    working, tested software that matters.”*

Gherkin
-------

The structured acceptance criteria, which were written in plain language rather
than code, were further formalised using the Gherkin description language so
that they could be parsed automatically.

.. code-block:: gherkin

   Scenario: Add a task to the database
     Given an empty database
      When a task with a summary is added
      Then the number of tasks should be 1
       and the queried task from the db should correspond to the added object.

Each scenario is intended to serve as an example illustrating a specific aspect
of the application’s behaviour.

In Python, both `behave <https://behave.readthedocs.io/en/latest/>`_ and
`pytest-bdd <https://pypi.org/project/pytest-bdd/>`_ can parse Gherkin.
