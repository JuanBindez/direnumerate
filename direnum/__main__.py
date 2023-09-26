import requests
import os

from direnum.createlist import create_wordlist
from direnum.colors import Color


class DirScan():
    def __init__(self, url, wordlist_file):
        self.url = url
        self.wordlist_file = wordlist_file

    def dir_enum(self):
        try:
            with open(self.wordlist_file, "r") as self.wordlist_file:
                for line in self.wordlist_file:
                    path = line.strip()
                    full_url = self.url + "/" + path
                    response = requests.get(full_url)
                    
                    if response.status_code == 200:
                        print(Color.GREEN + f"Found: {Color.RESET + full_url}")
                    elif response.status_code == 403:
                        print(Color.RED + f"Access prohibited: {Color.RESET+ full_url}")
        except FileNotFoundError:
            print("Word list file not found.")

        if not os.path.isfile(self.wordlist_file):
            create_wordlist(self.wordlist_file)
