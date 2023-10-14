# this is part of the Direnumerate project.
#
# Copyright ©  2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.



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
           "Read the Docs": "https://direnumerate.readthedocs.io/",
      },
      keywords = ["web", "enumerate", "directory", "tools", "cli", "scan",],)
