Mock
====

In this chapter, we will test the :abbr:`CLI (Command Line Interface)`. To do
this, we will use the :doc:`mock <python3:library/unittest.mock>` library, which
has been included as part of the standard Python library since Python 3.3 under
the name ``unittest.mock``.

Objects that are not real can be either :term:`dummies <Dummy>`, :term:`fakes
<Fake>`, :term:`stubs <Stub>`, :term:`mocks <Mock>` or :term:`spies <Spy>`. They
are all what are known as test doubles. However, with pytest’s own
:ref:`monkeypatch-fixture` fixture and :doc:`unittest.mock
<python3:library/unittest.mock>`, you should have all the functionality you
need.

The three core functionalities of :doc:`unittest.mock
<python3:library/unittest.mock>` are:

:class:`Mock <python3:unittest.mock.Mock>`
    The Mock class can be used to simulate any object.
:class:`MagickMock <python3:unittest.mock.MagicMock>`
    A subclass of Mock that contains all magic methods, such as ``__str__``,
    ``__len__``, :abbr:`etc (et cetera)`.
:func:`patch <python3:unittest.mock.patch>`-Methode
    An object is searched for within a specific module and replaced with another
    object.

In the following, we will look at mocking return values, checking calls to mock
functions, and mocking exceptions. However, there are a whole range of other
mocking techniques that we will not cover. So be sure to read
:doc:`python3:library/unittest.mock` if you wish to make extensive use of
mocking.

.. toctree::
   :titlesonly:
   :hidden:

   examples
   spies
   autospec
   assert_called
   limitations
   plugins
