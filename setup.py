#!/usr/bin/env python
"""This module contains setup instructions for direnumerate."""

import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open(os.path.join(here, "direnumerate", "version.py")) as fp:
    exec(fp.read())



setup(name = "direnumerate",
      version = __version__,  # noqa: F821
      author = "Juan Bindez",
      author_email = "juanbindez780@gmail.com",
      packages = ["direnumerate"],
      package_data = {
          "direnumerate": ["https://github.com/JuanBindez/direnumerate/raw/main/img/logo.png", "LICENSE"],
      },
      url = "https://github.com/juanbindez/direnumerate",
      license = "GPLv2 license",
      entry_points={
          "console_scripts": [
          "direnumerate = direnumerate.cli:main"],},
      install_requires=[
          'requests',
      ],
      
      classifiers = [
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python",
          "Topic :: Internet",
          "Topic :: Multimedia :: Video",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Terminals",
          "Topic :: Utilities",
      ],
      description = ("Python 3 library for directory enumeration tool in web applications."),
      include_package_data = True,
      long_description_content_type = "text/markdown",
      long_description = long_description,
      zip_safe = True,
      python_requires = ">=3.7",
      project_urls = {
           "Bug Reports": "https://github.com/juanbindez/direnumerate/issues",
           "Read the Docs": "https://github.com/JuanBindez/direnumerate/tree/main/docs/user",
      },
      keywords = ["web", "enumerate", "directory", "tools", "cli", "scan",],)
