.. direnumerate documentation master file,

.. image:: https://github.com/JuanBindez/direnumerate/blob/main/img/logo.png
  :width: 50px
  :height: 50px

direnumerate
======
Release v\ |version|. (:ref:`Installation<install>`)


.. image:: https://img.shields.io/pypi/v/direnumerate.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/direnumerate/

.. image:: https://img.shields.io/pypi/pyversions/direnumerate.svg
  :alt: Python Versions
  :target: https://pypi.python.org/pypi/direnumerate/


**direnumerate** Direnumerate is an open source tool written in Python designed to automate directory and file enumeration on web servers..

-------------------

**Behold, a perfect balance of simplicity versus flexibility**::

    from direnumerate import DirScan

    url = "testphp.vulnweb.com"
    wordlist = "wordlist.txt"

    enum = DirScan(url)
    enum.dir_enum(wordlist)

Features
--------

- Enumeration of directories and files on web servers.
- Creates a wordlist automatically
- Wordlist customization.
- Detailed output of findings.
- Support for multiple URL schemes (http, https, etc.).

The User Guide
--------------
This part of the documentation begins with some background information about
the project, then focuses on step-by-step instructions for getting the most out
of direnumerate.

.. toctree::
   :maxdepth: 2

   user/install
   user/direnumerate
   user/cli

