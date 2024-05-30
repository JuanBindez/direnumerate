.. _log:

log:
====

**save the log in file direnumerate.log passing the parameter log=Tr:**::

        from direnumerate import Scan

        url = "testphp.vulnweb.com"
        wordlist = "wordlist.txt"

        enum = Scan(url)
        enum.dirs(log=True, wordlist_file=wordlist)