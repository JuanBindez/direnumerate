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

## Command line:

    direnumerate -u http://www.exemple.com -w wordlist.txt

## Exemple:

<pre><font color="#26A269"><b>juan@juan-MS-7680</b></font>:<font color="#12488B"><b>~</b></font>$ direnumerate -u http://www.exemple.com -w wordlist.txt
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/admin
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/login
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/images
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/js
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/css
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/config
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/index
<font color="#33DA7A">target found: -&gt; </font>http://www.exemple.com/robots.txt
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/backup
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/secret
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/support
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/contact
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/blog
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/forum
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/product
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/category
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/brand
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/password
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/123456
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/qwerty
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/letmein
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/access
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/admin123
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/administrator
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/superuser
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/root
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/test
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/guest
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/demo
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/webmaster
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/developer
<font color="#33DA7A">target found: -&gt; </font>http://www.exemple.com/api
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/api_key
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/db
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/database
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/user
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/users
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/auth
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/authentication
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/login.php
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/wp-admin
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/wp-login.php
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/upload
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/uploads
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/download
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/downloads
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/private
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/public
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/static
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/media
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/files
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/file
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/images/
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/js/
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/css/
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/assets/
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/images/uploads
<font color="#33DA7A">target found: -&gt; </font>http://www.exemple.com/userfiles
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/data
<font color="#F66151">target access prohibited: -&gt; </font>http://www.exemple.com/temp
</pre>
