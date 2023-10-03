import argparse
from direnumerate.__main__ import DirScan, PortScan, FindPattern
from direnumerate.colors import Color
from direnumerate.version import __version__


def dir_scan(args):
    """
    Perform directory enumeration based on the provided arguments.

    Args:
        args (argparse.Namespace): Command-line arguments and options.
    """
    try:
        url = args.target
        wordlist_file = args.wordlist

        enum = DirScan(url, wordlist_file)
        enum.dir_enum()
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
    try:
        host = args.target
        ports = args.ports

        scanner = PortScan(host, ports)
        scanner.scan_ports()
    except KeyboardInterrupt:
        print(Color.GREEN + "-------------- Port scan interrupted by user ------------" + Color.RESET)


def find_pattern(args):
    file_name_log = args.logname
    key = args.keyword

    fp = FindPattern(file_name_log)
    fp.find_in_log(keyword=key)
    
    
def main():
    """
    The main function for the Direnumerate application.

    Parses command-line arguments and options, and executes the appropriate subcommand (dir_scan or port_scan).
    """
    parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
    subparsers = parser.add_subparsers(title="subcommands")

    dir_parser = subparsers.add_parser("Ds", help="Perform directory enumeration")
    dir_parser.add_argument("-t", "--target", required=True, help="Target URL (including scheme, e.g. http://www.example.com)")
    dir_parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    dir_parser.set_defaults(func=dir_scan)

    port_parser = subparsers.add_parser("Ps", help="Perform port scanning")
    port_parser.add_argument("-t", "--target", required=True, help="Target host")
    port_parser.add_argument("-p", "--ports", nargs='+', type=int, required=True, help="Ports to scan (e.g., 22 80 443)")
    port_parser.set_defaults(func=port_scan)

    find_pattern_parser = subparsers.add_parser("Fp", help="Perform port scanning")
    find_pattern_parser.add_argument("-ln", "--logname", required=True, help="Log Name")
    find_pattern_parser.add_argument("-k", "--keyword", required=True, help="Key Word")
    find_pattern_parser.set_defaults(func=find_pattern)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()


