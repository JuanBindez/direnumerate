import requests
import os

from direnumerate.createlist import create_wordlist
from direnumerate.colors import Color


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
                        print(Color.GREEN + f"target access [Found]: -> {Color.RESET + full_url}")
                    elif response.status_code == 204:
                        print(Color.RED + f"target access [No Content]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 400:
                        print(Color.YELLOW + f"target access [Bad Request]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 401:
                        print(Color.RED + f"target access [Unauthorized]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 403:
                        print(Color.RED + f"target access [Forbidden]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 404:
                        print(Color.RED + f"target access [Not Found]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 500:
                        print(Color.BLUE + f"target access [Internal Server Error]: -> {Color.RESET+ full_url}")
        except FileNotFoundError:
            if not os.path.isfile(self.wordlist_file):
                create_wordlist(self.wordlist_file)
            print("Word list file not found.")
            
        except TypeError:
            print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
            
        except KeyboardInterrupt:
            print(Color.GREEN + "-------------- attempt interrupted by user ------------" + Color.RESET)

        if not os.path.isfile(self.wordlist_file):
            create_wordlist(self.wordlist_file)
