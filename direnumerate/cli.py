import argparse
from direnumerate.__main__ import DirScan, PortScan, FindPattern, InfoIp
from direnumerate.colors import Color
from direnumerate.banner import *
from direnumerate.version import __version__


def dir_scan(args):
    """
    Perform directory enumeration based on the provided arguments.

    Args:
        args (argparse.Namespace): Command-line arguments and options.
    """
    show_banner()

    if args.verbose:
            try:
                url = args.target
                wordlist_file = args.wordlist

                enum = DirScan(url)
                enum.dir_enum(wordlist_file, verbose=True)
            except TypeError:
                print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
            except KeyboardInterrupt:
                print(Color.GREEN + "-------------- Attempt interrupted by user ------------" + Color.RESET)
    else:
        pass

    try:
        url = args.target
        wordlist_file = args.wordlist

        enum = DirScan(url)
        enum.dir_enum(wordlist_file)
    except TypeError:
        print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
    except KeyboardInterrupt:
        print(Color.GREEN + "-------------- Attempt interrupted by user ------------" + Color.RESET)


def port_scan(args):
    """
    Perform port scanning based on the provided arguments.

    Args:
        args (argparse.Namespace): Command-line arguments and options.
    """
    show_banner()
    try:
        host = args.target
        ports = args.ports

        scanner = PortScan(host)
        scanner.scan_ports(ports)
    except KeyboardInterrupt:
        print(Color.GREEN + "-------------- Port scan interrupted by user ------------" + Color.RESET)


def find_pattern(args):
    show_banner()
    file_name_log = args.logname
    key = args.keyword

    fp = FindPattern(file_name_log)
    fp.find_in_log(keyword=key)


def show_info_ip(args):
    show_banner()
    ip_address = args.target

    ipinfo = InfoIp(ip_address)
    ipinfo.show_info()


import argparse

def dir_scan(args):
    """
    Function to perform directory enumeration.
    """
    # Implement directory scanning functionality here
    print("Performing directory enumeration...")
    print("Target URL:", args.target)
    print("Wordlist file:", args.wordlist)
    if args.verbose:
        print("Verbose output enabled")

def port_scan(args):
    """
    Function to perform port scanning.
    """
    # Implement port scanning functionality here
    print("Performing port scanning...")
    print("Target host:", args.target)
    print("Ports to scan:", args.ports)

def find_pattern(args):
    """
    Function to perform log scanning.
    """
    # Implement log scanning functionality here
    print("Performing log scanning...")
    print("Log Name:", args.logname)
    print("Key Word:", args.keyword)

def show_info_ip(args):
    """
    Function to perform info of IP scanning.
    """
    # Implement IP info scanning functionality here
    print("Performing IP info scanning...")
    print("Target host:", args.target)


def main():
    """
    The main function for the Direnumerate application.

    Parses command-line arguments and options, and executes the appropriate function.
    """
    parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
    
    # Add arguments for directory enumeration
    parser.add_argument("-v", "--verbose", required=False, action="store_true", help="Verbose output")
    parser.add_argument("-t", "--target", required=True, help="Target URL (including scheme, e.g. http://www.example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    
    # Add arguments for port scanning
    parser.add_argument("-p", "--ports", nargs='+', type=int, help="Ports to scan (e.g., 22 80 443)")
    
    # Add arguments for log scanning
    parser.add_argument("-log", "--logname", help="Log Name")
    parser.add_argument("-key", "--keyword", help="Key Word")
    
    # Add arguments for IP info scanning
    parser.add_argument("--info-target", help="Target host for info scanning")

    args = parser.parse_args()
    
    if args.logname and args.keyword:
        find_pattern(args)
    elif args.ports:
        port_scan(args)
    elif args.info_target:
        show_info_ip(args)
    else:
        dir_scan(args)

if __name__ == "__main__":
    main()