.. _direnumerate:

Directory Scan in websites:
=============================

**When running the script, direnumerate automatically creates a wordlist that can be customized later**::

        from direnumerate import DirScan

        url = "testphp.vulnweb.com"
        wordlist = "wordlist.txt"

        enum = Scan(url)
        enum.dirs(log=True, wordlist_file=wordlist)


**Directory scan with all outputs verbose**::

        from direnumerate import Scan

        url = "testphp.vulnweb.com"
        wordlist = "wordlist.txt"

        enum = Scan(url)
        enum.dirs(wordlist, verbose=True)

