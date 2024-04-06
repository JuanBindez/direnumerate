# Direnumerate


![PyPI - Downloads](https://img.shields.io/pypi/dm/direnumerate)
![PyPI - License](https://img.shields.io/pypi/l/direnumerate)
[![Documentation Status](https://readthedocs.org/projects/direnumerate/badge/?version=latest)](https://direnumerate.readthedocs.io/en/latest/?badge=latest)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/direnumerate?include_prereleases&link=https%3A%2F%2Fgithub.com%2FJuanBindez%2Fdirenumerate%2Ftags)
<a href="https://pypi.org/project/direnumerate/"><img src="https://img.shields.io/pypi/v/direnumerate" /></a>

[PDF documentation](https://direnumerate.readthedocs.io/_/downloads/en/latest/pdf/)


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

## install in ubuntu:

    pip install direnumerate --break-system-packages
----------

## Command line usage:

### Directory Scan:

    direnumerate -t testphp.vulnweb.com -w wordlist.txt

### Post Scan:

    direnumerate -t 44.228.249.3 -p 22 80 443

### Finds patterns in logs:

    direnumerate -log test.log -key ERROR

### IP Info:

    direnumerate -t 8.8.8.8 -i


## Scripts usage:

### Directory Scan in Websites:

```python

from direnumerate import DirScan

url = "testphp.vulnweb.com"
wordlist = "wordlist.txt"

enum = DirScan(url)
enum.dir_enum(wordlist)
```
----------

### Port Scan:

```python

from direnumerate import PortScan

ip = "44.228.249.3"
list_ports = [22, 80, 443]

scan = PortScan(ip)
scan.scan_ports(list_ports)

```
----------

### Finds patterns in logs:

```python

from direnumerate import FindPatterns

log = "test.log"
key = "ERROR"

fp = FindPatterns(log)
fp.find_in_log(keyword=key)
```

### IP Info:

```python

from direnumerate import InfoIp

ip = "8.8.8.8"

ipinfo = InfoIp(ip)
ipinfo.show_info()

```
----------
