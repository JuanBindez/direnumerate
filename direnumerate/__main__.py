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
from typing import Optional

from direnumerate.createlist import create_wordlist
from direnumerate.colors import Color
from direnumerate.banner import *
from direnumerate.help import help_direnumerate
import direnumerate.exceptions as exception
from direnumerate.warning import deprecated


class Dire:
    pass


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

    def dir_enum(self, 
                 wordlist_file, 
                 verbose_only_found: bool = False,
                 verbose: bool = False
                 ) -> list:
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

        results_list = []

        if verbose_only_found == False and verbose == False:
            with open(wordlist_file, "r") as file:
                    for line in file:
                        path = line.strip()
                        full_url = f"{self.url}/{path}"
                        response = requests.get(full_url)
                        
                        if response.status_code == 200:
                            results_list.append(f'[Found] {full_url}')
                            print(f"{Color.GREEN}[Found]:{Color.RESET} {full_url}")
                            
                        elif response.status_code == 204:
                            results_list.append(f'[No Content] {full_url}')
                            print(f"{Color.BLUE}[No Content]:{Color.RESET} {full_url}")
                        elif response.status_code == 400:
                            results_list.append(f'[Bad Request] {full_url}')
                            print(f"{Color.YELLOW}[Bad Request]:{Color.RESET} {full_url}")
                        elif response.status_code == 401:
                            results_list.append(f'[Unauthorized] {full_url}')
                            print(f"{Color.RED}[Unauthorized]:{Color.RESET} {full_url}")
                        elif response.status_code == 403:
                            results_list.append(f'[Forbidden] {full_url}')
                            print(f"{Color.RED}[Forbidden]:{Color.RESET} {full_url}")
                        elif response.status_code == 404:
                            results_list.append(f'[Not Found] {full_url}')
                            print(f"{Color.YELLOW}[Not Found]:{Color.RESET} {full_url}")
                        elif response.status_code == 500:
                            results_list.append(f'[Internal Server Error] {full_url}')
                            print(f"{Color.BLUE}[Internal Server Error]:{Color.RESET} {full_url}")

        if verbose_only_found: 
            with open(wordlist_file, "r") as file:
                for line in file:
                    path = line.strip()
                    full_url = f"{self.url}/{path}"
                    response = requests.get(full_url)
                        
                    if response.status_code == 200:
                        results_list.append(f'[Found] {full_url}')
                        print(f"{Color.GREEN}[Found]:{Color.RESET} {full_url}")

        if verbose:
            try:
                with open(wordlist_file, "r") as file:
                    for line in file:
                        path = line.strip()
                        full_url = f"{self.url}/{path}"
                        response = requests.get(full_url)
                        
                        if response.status_code == 200:
                            results_list.append(f'[Found] {full_url}')
                            if verbose:
                                print(f"{Color.GREEN}[Found]:{Color.RESET} {full_url}")
                            
                        elif response.status_code == 204:
                            results_list.append(f'[No Content] {full_url}')
                            if verbose:
                                print(f"{Color.BLUE}[No Content]:{Color.RESET} {full_url}")
                        elif response.status_code == 400:
                            results_list.append(f'[Bad Request] {full_url}')
                            if verbose:
                                print(f"{Color.YELLOW}[Bad Request]:{Color.RESET} {full_url}")
                        elif response.status_code == 401:
                            results_list.append(f'[Unauthorized] {full_url}')
                            if verbose:
                                print(f"{Color.RED}[Unauthorized]:{Color.RESET} {full_url}")
                        elif response.status_code == 403:
                            results_list.append(f'[Forbidden] {full_url}')
                            if verbose:
                                print(f"{Color.RED}[Forbidden]:{Color.RESET} {full_url}")
                        elif response.status_code == 404:
                            results_list.append(f'[Not Found] {full_url}')
                            if verbose:
                                print(f"{Color.YELLOW}[Not Found]:{Color.RESET} {full_url}")
                        elif response.status_code == 500:
                            results_list.append(f'[Internal Server Error] {full_url}')
                            if verbose:
                                print(f"{Color.BLUE}[Internal Server Error]:{Color.RESET} {full_url}")

            except FileNotFoundError:
                print(f"{Color.RED}Word list file not found.{Color.RESET}")
            except KeyboardInterrupt:
                print(f"{Color.GREEN}Attempt interrupted by user.{Color.RESET}")
            except requests.exceptions.ConnectionError as rec:
                print(f"{Color.RED}[Error] {rec}{Color.RESET}")
            
        return results_list