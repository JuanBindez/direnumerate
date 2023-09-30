# Direnumerate

![PyPI - Downloads](https://img.shields.io/pypi/dm/direnumerate)
![PyPI - License](https://img.shields.io/pypi/l/direnumerate)
![PyPI - Version](https://img.shields.io/pypi/v/direnumerate)


## Description

Direnumerate is an open source tool written in Python designed to automate directory and file enumeration on web servers. It is useful for security professionals and system administrators who want to identify hidden resources and assess the security of web applications.

## Key Features

- Enumeration of directories and files on web servers.
- Wordlist customization.
- Detailed output of findings.
- Support for multiple URL schemes (http, https, etc.).

## pip:

    pip install direnumerate

-----------------

## Scripts usage:

### Directory Scan

```python

from direnumerate import DirScan

url = "www.exemplo.com"
wordlist = "wordlist.txt"

enum = DirScan(url, wordlist)
enum.dir_enum()
```

----------

### Port Scan:

```python

from direnumerate import PortScan

ip = "www.exemple.com"
list_ports = [22, 80, 443]

scan = PortScan(ip, list_ports)
scan.scan_ports()

```
----------

### Payload:

```python

from direnumerate import PayLoad

url = "testphp.vulnweb.com/login.php"

pl = PayLoad(url)
pl.start_inject(verbose=True, rocket5=True, term="name")

```
----------
## Command line usage:


### Directory Scan:

    direnumerate Ds -u "www.exemple.com" -w wordlist.txt

### Post Scan:

    direnumerate Ps -t "192.168.1.0" -p 22 80 443




