Editors
=======

Interactive Shell
-----------------

With the interactive shell you can easily run most of the examples in this
tutorial. Later, you will also learn how to easily include code written to a
file as a module.

.. tab:: Linux

   Type ``python3`` in the terminal:

   .. code-block:: console

      $ python3
      Python 3.13.0 (main, Oct  7 2024, 05:02:14) on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>>

.. tab:: macOS

   Open a terminal window and enter ``python3``:

   .. code-block:: console


      $ python3
      Python 3.13.0 (main, Oct  7 2024, 05:02:14) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
      Type "help", "copyright", "credits" or "license" for more information.
      >>>

   .. note::
      If you get the error message *Command not found*, you can run
      :file:`Update Shell Profile`, which can be found in
      :file:`Applications/Python3.{10}`.

.. tab:: Windows

   You can start the interactive Python shell in :menuselection:`Start -->
   Applications --> Python 3.13`.

   Alternatively, you can search for the directly executable file
   :file:`Python.exe`, for example in
   :file:`C:\\Users\\VEIT\\AppData\\Local\\Programs\\Python\\Python310-64` and
   then double-click.

You can scroll through previous entries with the arrow keys :kbd:`Home`,
:kbd:`End`, :kbd:`Page up` and :kbd:`Page down` and repeat with the :kbd:`Enter`
key.

Exiting the interactive shell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To exit the interactive shell, simply use :kbd:`Ctrl-d` on Linux and macOS or
:kbd:`Ctrl-z` on Windows. Alternatively, you can type ``exit()``.

.. _idle:

IDLE
----

:doc:`python3:library/idle` is the acronym for *Integrated Development and
Learning Environment* and combines an interactive interpreter with tools for
code editing and debugging. It is very easy to run on the various platforms:

.. tab:: Linux/macOS

   Enter the following into your terminal:

   .. code-block:: console

      $ idle-python3.13

.. tab:: Windows

   You can start IDLE in :menuselection:`Windows --> All Apps --> IDLE (Python
   GUI)`

You can scroll through the history of previous commands with the :kbd:`alt-p`
and :kbd:`alt-n` keys.
