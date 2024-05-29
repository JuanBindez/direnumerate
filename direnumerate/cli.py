import argparse
from direnumerate.__main__ import Scan
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

                enum = Scan(url)
                enum.dirs(log=True, wordlist_file=wordlist_file, verbose=True)
            except TypeError:
                print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
            except KeyboardInterrupt:
                print(Color.GREEN + "-------------- Attempt interrupted by user ------------" + Color.RESET)
    else:
        pass

    try:
        url = args.target
        wordlist_file = args.wordlist

        enum = Scan(url)
        enum.dirs(log=True, wordlist_file=wordlist_file, return_only_found=True)
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

        scanner = Scan(host)
        scanner.ports(log=True, ports=ports)
    except KeyboardInterrupt:
        print(Color.GREEN + "-------------- Port scan interrupted by user ------------" + Color.RESET)


def main():
    """
    The main function for the Direnumerate application.

    Parses command-line arguments and options, and executes the appropriate function.
    """
    parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
    
    parser.add_argument("-v", "--verbose", required=False, action="store_true", help="Verbose output")
    parser.add_argument("-t", "--target", required=False, help="Target URL (including scheme, e.g. http://www.example.com)")
    parser.add_argument("-w", "--wordlist", required=False, help="Wordlist file")
    
    parser.add_argument("-p", "--ports", nargs='+', type=int, help="Ports to scan (e.g., 22 80 443)")
    
    args = parser.parse_args()

    if args.ports:
        port_scan(args)
    else:
        dir_scan(args)

if __name__ == "__main__":
    main()
