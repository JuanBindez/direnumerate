# Direnumerate



![PyPI - Downloads](https://img.shields.io/pypi/dm/direnumerate)
![PyPI - License](https://img.shields.io/pypi/l/direnumerate)
[![Documentation Status](https://readthedocs.org/projects/direnumerate/badge/?version=latest)](https://direnumerate.readthedocs.io/en/latest/?badge=latest)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/direnumerate?include_prereleases&link=https%3A%2F%2Fgithub.com%2FJuanBindez%2Fdirenumerate%2Ftags)
<a href="https://pypi.org/project/direnumerate/"><img src="https://img.shields.io/pypi/v/direnumerate" /></a>


## Description

Direnumerate is an open source tool written in Python designed to automate directory and file enumeration on web servers. It is useful for security professionals and system administrators who want to identify hidden resources and assess the security of web applications.

## Key Features

- Enumeration of directories and files on web servers.
- Creates a wordlist automatically
- Wordlist customization.
- Detailed output of findings.
- Support for multiple URL schemes (http, https, etc.).


## install:

    pip install direnumerate

-----------------

## Command line usage:

### Directory Scan:

    direnumerate -t testphp.vulnweb.com -w wordlist.txt

### Post Scan:

    direnumerate -t 44.228.249.3 -p 22 80 443

## Scripts usage:

### Directory Scan in Websites:

```python

from direnumerate import Scan

url = "testphp.vulnweb.com"
wordlist = "wordlist.txt"

enum = Scan(url)
print(enum.dirs(log=True, wordlist_file=wordlist))
```
----------

### Port Scan:

```python

from direnumerate import Scan

ip = '44.228.249.3'

enum = Scan(ip)
print(enum.ports(ports=[22, 443, 8080, 8280, 80, 25]))

```
----------
