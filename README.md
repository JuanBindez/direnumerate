<h1 align="#">
  <img alt="" title="" src="https://github.com/JuanBindez/direnumerate/blob/main/img/logo.png" width="110px"/>
</h1>

# Direnumerate

![PyPI - Downloads](https://img.shields.io/pypi/dm/direnumerate)
![PyPI - License](https://img.shields.io/pypi/l/direnumerate)
![PyPI - Version](https://img.shields.io/pypi/v/direnumerate)


## Description

Direnumerate is an open source tool written in Python designed to automate directory and file enumeration on web servers. It is useful for security professionals and system administrators who want to identify hidden resources and assess the security of web applications.

## Key Features

- Enumeration of directories and files on web servers.
- Creates a wordlist automatically
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
## Command line usage:


### Directory Scan:

    direnumerate Ds -t "testphp.vulnweb.com" -w wordlist.txt

### Post Scan:

    direnumerate Ps -t 44.228.249.3 -p 22 80 443

### Finds patterns in logs:

    direnumerate Fp -log test.log -key ERROR

### IP Info:

    direnumerate info -t 8.8.8.8




