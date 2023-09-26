# Direnumerate

## Description

Direnumerate is an open source tool written in Python designed to automate directory and file enumeration on web servers. It is useful for security professionals and system administrators who want to identify hidden resources and assess the security of web applications.

## Key Features

- Enumeration of directories and files on web servers.
- Wordlist customization.
- Detailed output of findings.
- Support for multiple URL schemes (http, https, etc.).

## Prerequisites

-Python 3.x

## Clone the repository:

```bash
    git clone https://github.com/seu-usuario/Direnumerate.git
'''

-----------------

### pip:

    pip install direnumerate

#### usage:

```python

from direnumerate import DirScan

url = input("url target here >")
wordlist = "wordlist.txt"

enum = DirScan(url, wordlist)
enum.dir_enum()
```

----------
