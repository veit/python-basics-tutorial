*„Batteries included“*
======================

In Python kann eine Bibliothek aus mehreren Komponenten bestehen, einschließlich
eingebauter Datentypen und Konstanten, die ohne eine Importanweisung verwendet
werden können, wie :abbr:`z.B. (zum Beispiel)` :doc:`/types/numbers` und
:doc:`/types/lists`, sowie einiger eingebauter :doc:`/functions/index` und
:doc:`/control-flows/exceptions`. Der größte Teil der Bibliothek ist eine
umfangreiche Sammlung von :doc:`Modulen </modules/index>`. Wenn ihr Python
installiert habt, stehen euch auch verschiedene Bibliotheken zur Verfügung zum

* :ref:`data-types`
* :ref:`files-storage`
* :ref:`os`
* :ref:`internet`
* :ref:`dev-debug`

.. _data-types:

Managen von Datentypen
----------------------

Die Standardbibliothek enthält natürlich Unterstützung für die in Python
eingebauten Typen. Darüber hinaus gibt es in der Standardbibliothek drei
Kategorien, die sich mit verschiedenen Datentypen befassen: Module für Strings,
Datentypen und Zahlen.

String-Module
~~~~~~~~~~~~~

.. include:: ../types/strings.rst
   :start-after: string-modules

Module für Datentypen
~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-------------------------------------------------------------------------------+
| Modul                 | Beschreibung                                                                  |
+=======================+===============================================================================+
| :py:mod:`datetime`,   | Zeit- und Kalenderoperationen                                                 |
| :py:mod:`calendar`    |                                                                               |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`collections` | Container-Datentypen                                                          |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`enum`        | ermöglicht die Erstellung von Aufzählungsklassen, die symbolische Namen an    |
|                       | konstante Werte binden                                                        |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`array`       | Effiziente Arrays von numerischen Werten                                      |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`sched`       | Event-Scheduler                                                               |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`queue`       | Synchronisierte Queue-Klasse                                                  |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`copy`        | Flache und tiefe Kopieroperationen                                            |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`pprint`      | druckt Python-Datenstrukturen „hübsch“ aus                                    |
+-----------------------+-------------------------------------------------------------------------------+
| :py:mod:`typing`      | unterstützt die Kommentierung von Code mit Hinweisen auf die Typen von        |
|                       | Objekten, insbesondere von Funktionsparametern und Rückgabewerten             |
+-----------------------+-------------------------------------------------------------------------------+

Module für Zahlen
~~~~~~~~~~~~~~~~~

.. include:: ../types/numbers.rst
   :start-after: number-modules

.. _files-storage:

Ändern von Dateien
------------------

.. include:: ../types/files.rst
   :start-after: file-modules

.. _os:

Interagieren mit dem Betriebssystem
-----------------------------------

+-------------------------------+-------------------------------------------------------------------------------+
| Modul                         | Beschreibung                                                                  |
+===============================+===============================================================================+
| :py:mod:`os`                  | Verschiedene Betriebssystemschnittstellen                                     |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`platform`            | Zugang zu den Identifizierungsdaten der zugrunde liegenden Plattform          |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`time`                | Zeitzugriff und Konvertierungen                                               |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`io`                  | Werkzeuge für die Arbeit mit Datenströmen                                     |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`select`              | Warten auf I/O-Abschluss                                                      |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`optparse`            | Parser für Befehlszeilenoptionen                                              |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`curses`              | Terminal-Handling für Zeichenzellen-Displays                                  |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`getpass`             | Portable Passworteingabe                                                      |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`ctypes`              | bietet C-kompatible Datentypen                                                |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`threading`           | High-Level Threading-Interface                                                |
+-------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`multiprocessing`     | Prozessbasierte Threading-Schnittstelle                                       |
+-------------------------------+-------------------------------------------------------------------------------+
| :doc:`subprocess              | Verwaltung von Unterprozessen                                                 |
| <python3:library/subprocess>` |                                                                               |
+-------------------------------+-------------------------------------------------------------------------------+

.. _internet:

Verwenden von Internet-Protokollen
----------------------------------

+-----------------------------------+-------------------------------------------------------------------------------+
| Modul                             | Beschreibung                                                                  |
+===================================+===============================================================================+
| :py:mod:`socket`,                 | Low-Level-Netzwerkschnittstelle und SSL-Wrapper für Socket-Objekte            |
| :py:mod:`ssl`                     |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`email`                   | E-Mail- und MIME-Verarbeitungspaket                                           |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`mailbox`                 | Manipulation von Postfächern in verschiedenen Formaten                        |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`cgi`,                    | Common Gateway Interface-Unterstützung                                        |
| :py:mod:`cgitb`                   |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`wsgiref`                 | WSGI-Dienstprogramme und Referenzimplementierung                              |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`urllib.request`,         | Öffnen und Parsen von URLs                                                    |
| :py:mod:`urllib.parse`            |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`ftplib`,                 | Clients für verschiedene Internetprotokolle                                   |
| :py:mod:`poplib`,                 |                                                                               |
| :py:mod:`imaplib`,                |                                                                               |
| :py:mod:`nntplib`,                |                                                                               |
| :py:mod:`smtplib`,                |                                                                               |
| :py:mod:`telnetlib`               |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`socketserver`            | Framework für Netzwerkserver                                                  |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`http.server`             | HTTP-Server                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`xmlrpc.client`,          | XML-RPC-Client und -Server                                                    |
| :py:mod:`xmlrpc.server`           |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+


.. _dev-debug:

Entwickeln und Debuggen
-----------------------

+-----------------------------------+-------------------------------------------------------------------------------+
| Modul                             | Beschreibung                                                                  |
+===================================+===============================================================================+
| :py:mod:`pydoc`                   | Dokumentationsgenerator und Online-Hilfesystem                                |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`doctest`                 | Beispiele aus Python-Docstrings testen                                        |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`unittest`                | Framework für Unittests, :abbr:`s.a. (siehe auch)` :doc:`/test/unittest`      |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`test.support`            | Utility-Funktionen für Tests                                                  |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`trace`                   | verfolgt die Ausführung von Python-Anweisungen                                |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`pdb`                     | Python-Debugger                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`logging`                 | Protokollierungsfunktion für Python                                           |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`timeit`                  | misst die Ausführungszeit von kleinen Codeschnipseln                          |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`profile`,                | Python-Profiler                                                               |
| :py:mod:`cProfile`                |                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`sys`                     | Systemspezifische Parameter und Funktionen                                    |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`gc`                      | Funktionen des Python-Garbage-Collectors                                      |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`inspect`                 | inspiziert Objekte live                                                       |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`atexit`                  | Exit-Handler                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`__future__`              | Zukünftige Statement-Definitionen                                             |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`imp`                     | erlaubt den Zugriff auf die Import-Interna                                    |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`zipimport`               | importiert von Modulen aus Zip-Archiven                                       |
+-----------------------------------+-------------------------------------------------------------------------------+
| :py:mod:`modulefinder`            | findet Module, die von einem Skript verwendet werden                          |
+-----------------------------------+-------------------------------------------------------------------------------+
