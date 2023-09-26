import requests
import os

from createlist import create_wordlist
from colors import Color

def dir_enum(url, wordlist):
    try:
        with open(wordlist, "r") as wordlist_file:
            for line in wordlist_file:
                path = line.strip()
                full_url = url + "/" + path
                response = requests.get(full_url)
                
                if response.status_code == 200:
                    print(Color.GREEN + f"Found: {Color.RESET + full_url}")
                elif response.status_code == 403:
                    print(Color.RED + f"Access prohibited: {Color.RESET+ full_url}")
    except FileNotFoundError:
        print("Word list file not found.")

if __name__ == "__main__":
    url = input("Target url-> ")
    wordlist_file = "wordlist.txt"

    # Cria a wordlist se ela ainda não existir
    if not os.path.isfile(wordlist_file):
        create_wordlist(wordlist_file)

    dir_enum(url, wordlist_file)
