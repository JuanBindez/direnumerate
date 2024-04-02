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


def main():
    """
    The main function for the Direnumerate application.

    Parses command-line arguments and options, and executes the appropriate function.
    """
    parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
    
    # Add arguments for directory enumeration
    parser.add_argument("-v", "--verbose", required=False, action="store_true", help="Verbose output")
    parser.add_argument("-t", "--target", required=False, help="Target URL (including scheme, e.g. http://www.example.com)")
    parser.add_argument("-w", "--wordlist", required=False, help="Wordlist file")
    parser.add_argument("-i", "--info", required=False, help="Target host for info scanning")
    
    # Add arguments for port scanning
    parser.add_argument("-p", "--ports", nargs='+', type=int, help="Ports to scan (e.g., 22 80 443)")
    
    # Add arguments for log scanning
    parser.add_argument("-log", "--logname", help="Log Name")
    parser.add_argument("-key", "--keyword", help="Key Word")
    

    args = parser.parse_args()
    
    if args.logname and args.keyword:
        find_pattern(args)
    elif args.ports:
        port_scan(args)
    elif args.info:
        show_info_ip(args)
    else:
        dir_scan(args)

if __name__ == "__main__":
    main()
