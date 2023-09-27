[![PyPI version](https://badge.fury.io/py/direnumerate.svg)](https://badge.fury.io/py/direnumerate)

# Direnumerate

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

## usage:

```python

from direnumerate import DirScan

url = "http://www.exemplo.com"
wordlist = "wordlist.txt"

enum = DirScan(url, wordlist)
enum.dir_enum()
```

----------

## Port Scan:

```python

from direnumerate import PortScan

ip = "192.168.0.1"
start_port = 22
end_port = 2425

scan = PortScan(ip, start_port, end_port)
scan.scan_ports()
```
----------

## Command line:

    direnumerate -u http://www.exemple.com -w wordlist.txt


### Directory Scan:

    direnumerate dirscan -u "http://www.exemple.com" -w wordlist.txt

### Post Scan:

    direnumerate portscan -t "192.168.1.0" -s 20 -e 80




