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

    Parses command-line arguments and options, and executes the appropriate subcommand (dir_scan or port_scan).
    """
    parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
    subparsers = parser.add_subparsers(title="subcommands")

    dir_parser = subparsers.add_parser("Ds", help="Perform directory enumeration")
    dir_parser.add_argument("-v", "--verbose", required=False, action="store_true", help="Verbose output")
    dir_parser.add_argument("-t", "--target", required=True, help="Target URL (including scheme, e.g. http://www.example.com)")
    dir_parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    dir_parser.set_defaults(func=dir_scan)

    port_parser = subparsers.add_parser("Ps", help="Perform port scanning")
    port_parser.add_argument("-t", "--target", required=True, help="Target host")
    port_parser.add_argument("-p", "--ports", nargs='+', type=int, required=True, help="Ports to scan (e.g., 22 80 443)")
    port_parser.set_defaults(func=port_scan)

    find_pattern_parser = subparsers.add_parser("Fp", help="Perform log scanning")
    find_pattern_parser.add_argument("-log", "--logname", required=True, help="Log Name")
    find_pattern_parser.add_argument("-key", "--keyword", required=True, help="Key Word")
    find_pattern_parser.set_defaults(func=find_pattern)

    info_parser = subparsers.add_parser("info", help="Perform info of ip scanning")
    info_parser.add_argument("-t", "--target", required=True, help="Target host")
    info_parser.set_defaults(func=show_info_ip)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()


