Introduction
============

Welcome to Python Basics! I have written this book to provide an easy and
practical introduction to Python. The book is not intended to be a comprehensive
reference guide to Python, but rather the goal is to give you a basic
familiarity with Python and enable you to quickly write your own programs.

About Python
------------

You may be asking yourself why you should learn Python. There are many
programming languages from C and C++ to Java, Lua and Go.

.. figure:: tiobe-index.svg
   :alt: TIOBE Index für Oktober 2022

   `TIOBE Index für Oktober 2022 <https://www.tiobe.com/tiobe-index/>`_

Python has become very widely used and one of the reasons might be that it runs
on many different platforms, from IoT devices to common operating systems to
supercomputers. It can be used well for developing small applications and fast
prototypes. In the process, there are countless software libraries to make your
work easier.

Python is a modern programming language developed by Guido van Rossum in the
1990s. Some strengths of Python are

ease of use
    Some of the reasons for this are that types are associated with objects, not
    variables; a variable can be assigned values of any type and a list can
    contain objects of different types. Also, the syntax rules are very simple
    and you can quickly learn to write useful code.
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
        * :doc:`jupyter-tutorial:performance/index`

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
Support for mobile devices
    Even though mobile devices have proliferated in recent years, Python does
    not have a strong presence in this area. While there are a few options to
    deploy and run Python on mobile devices, this is not always easy.
Support for concurrent computation
    Processors with multiple cores are now widespread and lead to significant
    performance gains in many areas. However, the standard implementation of
    Python is not designed to use multiple cores.

    .. seealso::
        * :doc:`jupyter-tutorial:performance/multiprocessing-threading-async`
