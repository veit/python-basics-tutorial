Introduction
============

About Python
------------

You may be asking yourself why you should learn Python. There are many
programming languages from C and C++ to Java, Lua and Go.

.. figure:: tiobe-index.svg
   :alt: TIOBE Index for July 2025

   `TIOBE Index for July 2025 <https://www.tiobe.com/tiobe-index/>`_

Python has become very widely used and one of the reasons might be that it runs
on many different platforms, from IoT devices to common operating systems to
supercomputers. It can be used well for developing small applications and fast
prototypes. In the process, there are countless software libraries to make your
work easier.

Python is a modern programming language developed by Guido van Rossum in the
1990s.

.. seealso::
    * `The Origins of Python
      <https://inference-review.com/article/the-origins-of-python>`_ by Lambert
      Meertens

Some strengths of Python are

ease of use
    Some of the reasons for this are that types are associated with objects, not
    variables; a variable can be assigned values of any type and a list can
    contain objects of different types. Also, the syntax rules are very simple
    and you can quickly learn to write useful code.

    .. figure:: python.png
       :alt: Python – and programming is fun again!

       `XKCD: Python <https://xkcd.com/353>`_

Expressive power
    Often you can achieve much more in a few lines of code than in other
    languages. As a result, you can complete your projects more quickly, and
    debugging and maintenance are also much easier.
Readability
    The easy readability of Python code simplifies debugging and maintenance.
    One of the ways Python achieves this is by requiring indentation.
Completeness
    With the installation of Python, everything essential needed for programming
    with Python is already available, emails, websites, databases, without the
    need to install additional libraries.
Platform independence
    Python runs on many platforms: Windows, Mac, Linux :abbr:`etc /et cetera)`.
    There are even variants that run on Java
    (`Jython <https://www.jython.org/>`_) and .NET (`IronPython
    <https://ironpython.net/>`_).
Open Source
    You can download Python and use it freely for developing commercial or
    private applications. Python is used and promoted by many established
    companies, including Google, Meta and Bloomberg. And if you want to give
    something back, you are also welcome to do so : `Python Software Foundation
    Sponsorship <https://www.python.org/psf/sponsorship/>`_

Python has some advantages, but no language is the best solution in all areas.
For example, Python performs less well in the following areas:

Speed
    Python is not a fully compiled language and code is first compiled into
    bytecode before being executed by the Python interpreter. While there are
    some tasks, such as string parsing with regular expressions, for which
    Python provides efficient implementations, and which are as fast as a C
    program, Python programs will still be slower than C programs in most cases.
    However, this rarely plays a decisive role, since there are already many
    Python modules that use C internally.

    .. seealso::
        * :doc:`Python4DataScience:performance/index`

Diverse libraries
    Python already has a lot of libraries, but in some cases you will only find
    suitable libraries in other languages. For most problems that need to be
    solved programmatically, however, Python’s library support is excellent.
Variable types
    Unlike in many other languages, variables are not containers, but rather
    labels that refer to various objects: Integers, strings, class instances and
    more. Some find it a disadvantage that Python does not simply perform type
    validation here, but the number of type errors is usually manageable and the
    flexibility of dynamic typing usually outweighs the problems.

.. _mobile:

Support for mobile devices
    There are now several options for running Python on mobile devices, for
    example with :ref:`briefcase` or :ref:`beeware`. Python itself will offer
    `Tier 3 <https://peps.python.org/pep-0011/#tier-3>`_ support for Windows,
    iOS and Pi OS, among others, from version 3.13. It will also be easier to
    create wheels for mobile devices in the future by extending tools such as
    :doc:`packs/cibuildwheel` and :term:`setuptools`.

    .. seealso::
       * `The Python Language Summit 2024: Python on Mobile
         <https://pyfound.blogspot.com/2024/06/python-language-summit-2024-python-on-mobile.html>`_
       * :pep:`730`
       * :pep:`738`

Support for concurrent computation
    Processors with multiple cores are now widespread and lead to significant
    performance gains in many areas. However, the standard implementation of
    Python is not designed to use multiple cores.

    .. seealso::
        * :doc:`Python4DataScience:performance/multiprocessing-threading-async`
