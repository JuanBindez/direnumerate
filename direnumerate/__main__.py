import requests
import socket
import os
import webbrowser
from typing import Optional

from direnumerate.createlist import create_wordlist
from direnumerate.colors import Color
from direnumerate.banner import banner


class DirScan():
    """
    A class for directory scanning.

    Attributes:
        url (str): The URL to scan.
        wordlist_file (str): The path to the wordlist file.
    """
    def __init__(self, url, wordlist_file):
        """
        Initializes a DirScan instance.

        Args:
            url (str): The URL to scan.
            wordlist_file (str): The path to the wordlist file.
        """
        self.url = "http://" + url
        self.wordlist_file = wordlist_file

    def dir_enum(self, verbose: bool = False):
        """
        Perform directory enumeration.

        This method reads paths from a wordlist file, appends them to the URL, and sends HTTP requests to
        check for the existence of the resources. It prints the results based on the response status code.

        - 200: Found
        - 204: No Content
        - 400: Bad Request
        - 401: Unauthorized
        - 403: Forbidden
        - 404: Not Found
        - 500: Internal Server Error

        If the wordlist file is not found, it attempts to create one.
        """
        banner()

        if verbose:
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
                print("Word list file not found.")
                
            except TypeError:
                print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
                
            except KeyboardInterrupt:
                print(Color.GREEN + "-------------- Attempt interrupted by user ------------" + Color.RESET)

            except requests.exceptions.ConnectionError as rec:
                print(rec)
                print(Color.RED + "[Error] Don't put http:// in hosts, the software already does that" + Color.RESET)

        else:
            try:
                with open(self.wordlist_file, "r") as self.wordlist_file:
                        for line in self.wordlist_file:
                            path = line.strip()
                            full_url = self.url + "/" + path
                            response = requests.get(full_url)
                            
                            if response.status_code == 200:
                                print(Color.GREEN + f"Target access [Found]: -> {Color.RESET + full_url}")
            
            except FileNotFoundError:
                print("Word list file not found.")
                
            except TypeError:
                print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
                
            except KeyboardInterrupt:
                print(Color.GREEN + "-------------- Attempt interrupted by user ------------" + Color.RESET)

            except requests.exceptions.ConnectionError as rec:
                print(rec)
                print(Color.RED + "[Error] Don't put http:// in hosts, the software already does that" + Color.RESET)

class PortScan:
    """
    A class for port scanning.

    Attributes:
        host (str): The host to scan for open ports.
        ports (list): A list of ports to scan.
        open_ports (list): A list to store open ports.
    """
    def __init__(self, host, ports):
        """
        Initializes a PortScan instance.

        Args:
            host (str): The host to scan for open ports.
            ports (list): A list of ports to scan.
        """
        self.host = host
        self.ports = ports
        self.open_ports = []

    def scan_ports(self):
        """
        Scan the specified ports on the target host.

        This method attempts to establish a TCP connection to each port in the list of ports on the target host.
        If the connection is successful (result == 0), the port is considered open, and it is added to the open_ports list.
        If the connection fails, the port is considered closed.

        The results are printed to the console, indicating whether each port is open or closed.

        Raises:
            socket.gaierror: If an invalid host is provided.
        """
        try:
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
        except socket.gaierror as sq:
            print(sq)
            print(Color.RED + "[Error] Don't put http:// in hosts, the software already does that" + Color.RESET)


class FindPattern:
    """
    A class for searching for a keyword in a log file.

    Attributes:
        file_log (str): The path to the log file.
        keyword (str): The keyword to search for in the log file.
    """

    def __init__(self, file_log):
        """
        Initializes a LogScan instance.

        Args:
            file_log (str): The path to the log file.
            keyword (str, optional): The keyword to search for in the log file.
        """
        self.file_log = file_log

    def find_in_log(self, keyword: str = None):
        """
        Search for the specified keyword in the log file and display matching lines.

        This method reads the lines from the log file and identifies lines that contain the specified keyword.
        It then prints the matching lines along with their line numbers.

        If no matching lines are found, a message is printed indicating that no occurrences were found.
        """
        self.keyword = keyword

        with open(self.file_log, 'r') as file:
            lines = file.readlines()

        matching_lines = [line for line in lines if self.keyword in line]

        if matching_lines:
            banner()
            print(Color.GREEN + f"Lines with the word --> '{self.keyword}':" + Color.RESET)
            for i, line in enumerate(matching_lines, start=1):
                print(f"Line {i}: {line.strip()}")
        else:
            banner()
            print(Color.RED + f"No occurrence of the word --> '{self.keyword}' found." + Color.RESET)