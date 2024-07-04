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
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging
from typing import Optional

from direnumerate.createlist import create_wordlist
from direnumerate.colors import Color
from direnumerate.banner import *
from direnumerate.help import help_direnumerate
import direnumerate.exceptions as exception
from direnumerate.warning import deprecated
from direnumerate.port_scan import PortScan


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Scan:
    """
    A class to perform directory and port scanning on a given URL.
    """

    def __init__(self, url: str):
        """
        Initializes the Scan object with the given URL. The URL is validated and 
        adjusted to use HTTPS if needed.

        Args:
            url (str): The target URL to scan.

        Raises:
            DirenumerateError: If the URL argument is missing or incorrect.
        """
        self.url = url

        try:
            url_verify = url[4]
        
            if url_verify == ":":
                url = url.replace("http://", "https://")
                self.url = url
            elif url_verify == "s":
                self.url = url
            else:
                self.url = "https://" + url
                
        except IndexError:
            raise exception.DirenumerateError("[error] expected an argument")

        self.logger = logging.getLogger('direnumerate')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('direnumerate.log')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def dirs(self, 
             wordlist_file: str, 
             return_only_found: bool = False,
             verbose: bool = False,
             log: bool = False
             ) -> list:
        """
        Initializes the Scan object with the given URL. The URL is validated and 
        adjusted to use HTTPS if needed.

        Args:
            url (str): The target URL to scan.

        Raises:
            DirenumerateError: If the URL argument is missing or incorrect.
        """
        self.wordlist_file = wordlist_file

        results_list = []

        if return_only_found == False and verbose == False:
            try:
                with open(wordlist_file, "r") as file:
                    for line in file:
                        path = line.strip()
                        full_url = f"{self.url}/{path}"
                        response = requests.get(full_url, verify=False)
                        
                        result = ""
                        if response.status_code == 200:
                            result = f'[Found] {full_url}'
                        elif response.status_code == 204:
                            result = f'[No Content] {full_url}'
                        elif response.status_code == 400:
                            result = f'[Bad Request] {full_url}'
                        elif response.status_code == 401:
                            result = f'[Unauthorized] {full_url}'
                        elif response.status_code == 403:
                            result = f'[Forbidden] {full_url}'
                        elif response.status_code == 404:
                            result = f'[Not Found] {full_url}'
                        elif response.status_code == 500:
                            result = f'[Internal Server Error] {full_url}'
                        
                        results_list.append(result)
                        if log:
                            self.logger.debug(result)

            except FileNotFoundError:
                error_message = f"{Color.RED}Word list file not found.{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.error("Word list file not found.")
            except KeyboardInterrupt:
                error_message = f"{Color.GREEN}Attempt interrupted by user.{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.warning("Attempt interrupted by user.")
            except requests.exceptions.ConnectionError as rec:
                error_message = f"{Color.RED}[Error] {rec}{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.error(f"[Error] {rec}")

        if return_only_found: 
            try:
                with open(wordlist_file, "r") as file:
                    for line in file:
                        path = line.strip()
                        full_url = f"{self.url}/{path}"
                        response = requests.get(full_url, verify=False)
                        
                        if response.status_code == 200:

                            result = f'[Found] {full_url}'
                            results_list.append(result)
                            print(f"{Color.GREEN}[Found]:{Color.RESET} {full_url}")
                            if log:
                                self.logger.debug(result)

            except FileNotFoundError:
                error_message = f"{Color.RED}Word list file not found.{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.error("Word list file not found.")
            except KeyboardInterrupt:
                error_message = f"{Color.GREEN}Attempt interrupted by user.{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.warning("Attempt interrupted by user.")

            except requests.exceptions.ConnectionError as rec:
                error_message = f"{Color.RED}[Error] {rec}{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.error(f"[Error] {rec}")

        if verbose:
            try:
                with open(wordlist_file, "r") as file:
                    for line in file:
                        path = line.strip()
                        full_url = f"{self.url}/{path}"

                        response = requests.get(full_url, verify=False)
                        
                        result = ""
                        if response.status_code == 200:
                            result = f'[Found] {full_url}'
                            if verbose:
                                print(f"{Color.GREEN}[Found]:{Color.RESET} {full_url}")
                        elif response.status_code == 204:
                            result = f'[No Content] {full_url}'
                            if verbose:
                                print(f"{Color.BLUE}[No Content]:{Color.RESET} {full_url}")
                        elif response.status_code == 400:
                            result = f'[Bad Request] {full_url}'
                            if verbose:
                                print(f"{Color.YELLOW}[Bad Request]:{Color.RESET} {full_url}")
                        elif response.status_code == 401:
                            result = f'[Unauthorized] {full_url}'
                            if verbose:
                                print(f"{Color.RED}[Unauthorized]:{Color.RESET} {full_url}")
                        elif response.status_code == 403:
                            result = f'[Forbidden] {full_url}'
                            if verbose:
                                print(f"{Color.RED}[Forbidden]:{Color.RESET} {full_url}")
                        elif response.status_code == 404:
                            result = f'[Not Found] {full_url}'
                            if verbose:
                                print(f"{Color.YELLOW}[Not Found]:{Color.RESET} {full_url}")
                        elif response.status_code == 500:
                            result = f'[Internal Server Error] {full_url}'
                            if verbose:
                                print(f"{Color.BLUE}[Internal Server Error]:{Color.RESET} {full_url}")
                        
                        results_list.append(result)
                        if log:
                            self.logger.debug(result)

            except FileNotFoundError:
                error_message = f"{Color.RED}Word list file not found.{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.error("Word list file not found.")
            except KeyboardInterrupt:
                error_message = f"{Color.GREEN}Attempt interrupted by user.{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.warning("Attempt interrupted by user.")
            except requests.exceptions.ConnectionError as rec:
                error_message = f"{Color.RED}[Error] {rec}{Color.RESET}"
                print(error_message)
                if log:
                    self.logger.error(f"[Error] {rec}")
            
        return results_list
    
    def ports(self, ports: list, log: bool = False) -> list:
        """
        Scans the specified ports for the given URL.

        Args:
            ports (list): A list of ports to scan.
            log (bool, optional): If True, writes output to direnumerate.log file.
            Defaults to False.

        Returns:
            list: A list of scan results for the specified ports.
        """
        scan = PortScan(self.url)
        results = scan.scan_ports(ports)
        if log:
            self.logger.debug(f"open ports {results} in {self.url}")
        return results
