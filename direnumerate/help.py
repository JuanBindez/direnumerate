
def help_direnumerate():
    print(
        """usage: direnumerate [-h] [-v] [-t TARGET] [-w WORDLIST] [-i INFO]
                        [-p PORTS [PORTS ...]] [-log LOGNAME] [-key KEYWORD]

        Direnumerate - Directory Enumeration on Web Servers

        options:
        -h, --help            show this help message and exit
        -v, --verbose         Verbose output
        -t TARGET, --target TARGET
                                Target URL (including scheme, e.g.
                                http://www.example.com)
        -w WORDLIST, --wordlist WORDLIST
                                Wordlist file
        -i INFO, --info INFO  Target host for info scanning
        -p PORTS [PORTS ...], --ports PORTS [PORTS ...]
                                Ports to scan (e.g., 22 80 443)
        -log LOGNAME, --logname LOGNAME
                                Log Name
        -key KEYWORD, --keyword KEYWORD
                                Key Word
        """
    )