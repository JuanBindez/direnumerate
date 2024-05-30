.. _dirs:

Dirs Scan
==========

**To scan directories on websites:**::

        from direnumerate import Scan

        url = "testphp.vulnweb.com"
        wordlist = "wordlist.txt"

        enum = Scan(url)
        enum.dirs(wordlist_file=wordlist)
