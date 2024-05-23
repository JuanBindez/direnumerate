__title__ = "direnumerate"
__author__ = "Juan Bindez"
__license__ = "GPLv2 License"
__js__ = None
__js_url__ = None

import os

from direnumerate.version import __version__
from direnumerate.__main__ import Scan
from direnumerate.port_scan import PortScan
from direnumerate.createlist import create_wordlist

wordlist_file = "wordlist.txt"

if not os.path.isfile(wordlist_file):
            create_wordlist(wordlist_file)