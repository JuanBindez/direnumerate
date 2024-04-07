# this is part of the Direnumerate project.
#
# Copyright ©  2023 - 2024 Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import requests
import socket
import os
import webbrowser
from typing import Optional

from direnumerate.createlist import create_wordlist
from direnumerate.colors import Color
from direnumerate.banner import *
from direnumerate.getinfo import get_info_ip
from direnumerate.ipcalculator import *
from direnumerate.list_urls_accounts import *
from direnumerate.help import help_direnumerate


class DirScan:
    """
    A class for directory scanning.

    Attributes:
        url (str): The URL to scan.
        wordlist_file (str): The path to the wordlist file.
    """
    def __init__(self, url):
        """
        Initializes a DirScan instance.

        Args:
            url (str): The URL to scan.
            wordlist_file (str): The path to the wordlist file.
        """
        try:
            url_verify = url[4]
        except IndexError:
            help_direnumerate()

        if url_verify == ":":
            url = url.replace("http://", "https://")
            self.url = url

        elif url_verify == "s":
            self.url = url

        else:
            self.url = "https://" + url

    def dir_enum(self, wordlist_file, verbose: bool = False):
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
        self.wordlist_file = wordlist_file
        

        if verbose:
            try:
                with open(self.wordlist_file, "r") as self.wordlist_file:
                    for line in self.wordlist_file:
                        path = line.strip()
                        full_url = self.url + "/" + path
                        response = requests.get(full_url)
                        
                        if response.status_code == 200:
                            results = f"{Color.GREEN}[Found]:{Color.RESET} {full_url}"
                            print(results)
                            
                        elif response.status_code == 204:
                            results = f"{Color.BLUE}[No Content]:{Color.RESET} {full_url}"
                            print(results)
                            
                        elif response.status_code == 400:
                            results = f"{Color.YELLOW}[Bad Request]:{Color.RESET} {full_url}"
                            print(results)
                            
                        elif response.status_code == 401:
                            results = f"{Color.RED}[Unauthorized]:{Color.RESET} {full_url}"
                            print(results)
                            
                        elif response.status_code == 403:
                            results = f"{Color.RED}[Forbidden]:{Color.RESET} {full_url}"
                            print(results)
                            
                        elif response.status_code == 404:
                            results =f"{Color.YELLOW}[Not Found]:{Color.RESET} {full_url}"
                            print(results)
                            
                        elif response.status_code == 500:
                            results = f"{Color.BLUE}[Internal Server Error]:{Color.RESET} {full_url}"
                            print(results)
                            

            except FileNotFoundError:
                print(Color.RED + "Word list file not found." + Color.RESET)
                
            except TypeError:
                print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
                
            except KeyboardInterrupt:
                print(Color.GREEN + "-------------- Attempt interrupted by user ------------" + Color.RESET)

            except requests.exceptions.ConnectionError as rec:
                print(rec)
                print(Color.RED + "[Error] " + Color.RESET)

        else:
            try:
                with open(self.wordlist_file, "r") as self.wordlist_file:
                        for line in self.wordlist_file:
                            path = line.strip()
                            full_url = self.url + "/" + path
                            response = requests.get(full_url)
                            
                            if response.status_code == 200:
                                results = f"{Color.GREEN}[Found]:{Color.RESET} {full_url}"
                                print(results)
            
            except FileNotFoundError:
                print(Color.RED + "Word list file not found." + Color.RESET)
                
            except TypeError:
                print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
                
            except KeyboardInterrupt:
                print(Color.GREEN + "-------------- Attempt interrupted by user ------------" + Color.RESET)

            except requests.exceptions.ConnectionError as rec:
                print(rec)
                print(Color.RED + "[Error]" + Color.RESET)

class PortScan:
    """
    A class for port scanning.

    Attributes:
        host (str): The host to scan for open ports.
        ports (list): A list of ports to scan.
        open_ports (list): A list to store open ports.
    """
    def __init__(self, host):
        """
        Initializes a PortScan instance.

        Args:
            host (str): The host to scan for open ports.
            ports (list): A list of ports to scan.
        """
        self.host = host.replace("https://", "")
        self.open_ports = []

    def scan_ports(self, ports):
        """
        Scan the specified ports on the target host.

        This method attempts to establish a TCP connection to each port in the list of ports on the target host.
        If the connection is successful (result == 0), the port is considered open, and it is added to the open_ports list.
        If the connection fails, the port is considered closed.

        The results are printed to the console, indicating whether each port is open or closed.

        Raises:
            socket.gaierror: If an invalid host is provided.
        """
        self.ports = ports
        
        try:
            for port in self.ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)

                result = sock.connect_ex((self.host, port))

                if result == 0:
                    self.open_ports.append(port)
                    results = f"{Color.GREEN} [http://{self.host}] port: {port} is open, {Color.RESET}"
                    print(results)
                   
                else:
                    results = f"{Color.RED} [http://{self.host}] port: {port} is closed, {Color.RESET}"
                    print(results)
                
        except socket.gaierror as sq:
            print(sq)
            print(Color.RED + "[Error]" + Color.RESET)
        sock.close()

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
            
            print(Color.GREEN + f"Lines with the word --> '{self.keyword}':" + Color.RESET)
            for i, line in enumerate(matching_lines, start=1):
                print(f"Line {i}: {line.strip()}")
        else:
            
            print(Color.RED + f"No occurrence of the word --> '{self.keyword}' found." + Color.RESET)


class InfoIp:
    """
    A class for obtaining and analyzing information about an IP address, as well as performing IP-related calculations.

    Args:
        ip (str): The IP address to be analyzed.

    Methods:
        ip_calculator(self, all=False, verify_valid_ip=False, verify_class=False, calc_subnet_mask=False, calc_count=False):
            Perform various IP-related calculations and verifications based on the specified flags.

        show_info(self):
            Display detailed information about the IP address, including its geographical location, hostname, and more.

    Attributes:
        ip (str): The IP address to be analyzed.

    The `ip_calculator` method allows you to perform different IP-related tasks based on the specified flags. You can verify if the IP is valid, calculate its class, subnet mask, or the number of IP addresses in its block.

    The `show_info` method retrieves and displays comprehensive information about the IP address, including its geographical details, hostname, and more.

    Example:
        ip_info = InfoIp("192.168.1.1")
        ip_info.show_info()
        ip_info.ip_calculator(verify_valid_ip=True)

    Note:
        This class relies on external functions (not provided in this code snippet) such as `is_valid_ip`, `calculate_ip_class`,
        `calculate_subnet_mask`, `calculate_ip_count`, and `get_info_ip` for its functionality.

    For detailed information on the individual methods and their parameters, please refer to the method's documentation.
    """
    def __init__(self, ip):
        self.ip = ip


    def ip_calculator(self,
                         all: bool = False,
                         verify_valid_ip: bool = False,
                         verify_class: bool = False,
                         calc_subnet_mask: bool = False,
                         calc_count: bool = False,):
        """
        Perform various IP-related calculations and verifications based on the specified flags.

        Args:
            all (bool): Calculate all available information if set to True.
            verify_valid_ip (bool): Verify if the IP address is valid.
            verify_class (bool): Calculate and display the IP address class.
            calc_subnet_mask (bool): Calculate and display the subnet mask.
            calc_count (bool): Calculate and display the number of IP addresses in the block.

        Returns:
            None

        Note:
            This method relies on external functions (not provided in this code snippet) for its functionality.
        """

        if all:
            if is_valid_ip(self.ip):
                # print(Color.GREEN + "Valid IP address." + Color.RESET)
                ip_class = calculate_ip_class(self.ip)
                print(Color.GREEN + "IP address class:" + Color.RESET, f"{ip_class}")
                subnet_mask = calculate_subnet_mask(self.ip)
                print(Color.GREEN + "Subnet mask:" + Color.RESET, f"{subnet_mask}")
                ip_count = calculate_ip_count(self.ip)
                if ip_count == "Not applicable":
                    print(Color.RED + "Cannot calculate for this address class." + Color.RESET)
                else:
                    print(Color.GREEN + "The number of IP addresses in the block is:" + Color.RESET, f"{ip_count}")

               
            else:
                print(Color.RED + "Invalid IP address. Make sure you use the correct format." + Color.RESET)

        elif verify_valid_ip:

            if is_valid_ip(self.ip):
                print(Color.GREEN + "Valid IP address." + Color.RESET)

        elif verify_class:

            ip_class = calculate_ip_class(self.ip)
            print(Color.GREEN + f"IP address class: ",  + Color.RESET + {ip_class})

        elif calc_subnet_mask:

            subnet_mask = calculate_subnet_mask(self.ip)
            print(Color.GREEN + f"Subnet mask:", + Color.RESET + {subnet_mask})

        elif calc_count:
            if is_valid_ip(self.ip):
                ip_count = calculate_ip_count(self.ip)
                if ip_count == "Not applicable":
                    print(Color.RED + "Cannot calculate for this address class.", + Color.RESET)
                else:
                    print(Color.GREEN + f"The number of IP addresses in the block is:"+ Color.RESET, {ip_count})
            else:
                print(Color.RED + "Invalid IP address. Make sure to use the correct format.", + Color.RESET)
    

    def show_info(self):
        """
        Display detailed information about the IP address, including its geographical location, hostname, and more.

        Args:
            None

        Returns:
            None

        Note:
            This method relies on external functions (not provided in this code snippet) for its functionality.
        """
        
        informations = get_info_ip(self.ip)

        print(Color.GREEN + "Information about the IP address:" + Color.RESET, self.ip)
        print(Color.GREEN + "IP:" + Color.RESET, informations["ip"])
        print(Color.GREEN + "Hostname:" + Color.RESET, informations["hostname"])
        print(Color.GREEN + "Location:" + Color.RESET, informations["loc"])
        print(Color.GREEN + "City:" + Color.RESET, informations["city"])
        print(Color.GREEN + "Region:" + Color.RESET, informations["region"])
        print(Color.GREEN + "Country:" + Color.RESET, informations["country"])
        print(Color.GREEN + "Internet Service Provider:" + Color.RESET, informations["org"])

        # Additional information (if available)
        print(Color.GREEN + "Postal Code:" + Color.RESET, informations.get("postal"))
        print(Color.GREEN + "Time Zone:" + Color.RESET, informations.get("timezone"))
        print(Color.GREEN + "Coordinates:" + Color.RESET, informations.get("loc"))
        print(Color.GREEN + "Company Name:" + Color.RESET, informations.get("company"))
        print(Color.GREEN + "ASN (Autonomous System Number):" + Color.RESET, informations.get("asn"))
        print(Color.GREEN + "Network Prefix:" + Color.RESET, informations.get("network"))
        print(Color.GREEN + "Network Prefix CIDR:" + Color.RESET, informations.get("cidr"))
        print(Color.GREEN + "Connection Type:" + Color.RESET, informations.get("type"))
        print(Color.GREEN + "Regional Internet Registry (RIR):" + Color.RESET, informations.get("region"))
        print(Color.GREEN + "IP Block:" + Color.RESET, informations.get("ip_block"))
        
        ic = InfoIp(self.ip)
        ic.ip_calculator(all=True)


class UserScan:
    def __init__(self, user_name):
        self.user_name = user_name

    def found_users(self):
        for user in list_accounts:

            full_url = user + self.user_name
            response = requests.get(full_url)
                        
            if response.status_code == 200:
                print(Color.GREEN + f"User Account [Found]: -> {Color.RESET + full_url}")
            else:
                print(Color.RED + f"User Account [Not Found]: -> {Color.RESET + full_url}")

