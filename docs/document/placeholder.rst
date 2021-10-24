Placeholder
===========

Sphinx distinguishes the following placeholder variables:

.. rst:role:: envvar

    Environment variable that also creates a reference to the appropriate
   :rst:dir:`envvar` directive if it exists.

.. rst:role:: file

    The name of a file or directory. Curly brackets can be used to specify a
   variable part, for example::
   
        … is installed in :file:`/usr/lib/python3.{x}/site-packages` …

In the generated HTML documentation, the ``x`` is specially marked with ``em
.pre`` and italicised to show that it is to be replaced by the specific Python
version.

.. rst:role:: makevar

    The name of a :command:`make` variable

.. rst:role:: samp

   Text example, such as code within which curly braces can be used to indicate
   a variable part, as in :rst:role:`file` or in :samp:`print 1+{VARIABLE}`.
  
   As of Sphinx≥1.8, curly braces can be displayed with a backslash (``\``).

.. note::
    .. rst:role:: content

   This role has no special meaning by default. You can therefore use it for
   anything, for example also for variable names.
