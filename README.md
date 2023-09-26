# direnum

Python 3 library for directory enumeration tool in web applications

#### usage:

```python

from direnum import DirScan

url = input("url target here >")
wordlist = "wordlist.txt"

enum = DirScan(url, wordlist)
enum.dir_enum()
```

----------
