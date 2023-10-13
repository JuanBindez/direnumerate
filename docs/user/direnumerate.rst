.. _direnumerate:

Directory Scan in websites:
=============================

**When running the script, direnumerate automatically creates a wordlist that can be customized later**::

        from direnumerate import DirScan

        url = "testphp.vulnweb.com"
        wordlist = "wordlist.txt"

        enum = DirScan(url)
        enum.dir_enum(wordlist)


**Directory scan with all outputs verbose**::

        from direnumerate import DirScan

        url = "testphp.vulnweb.com"
        wordlist = "wordlist.txt"

        enum = DirScan(url)
        enum.dir_enum(wordlist, verbose=True)

