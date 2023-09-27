import argparse

from direnumerate.__main__ import DirScan
from direnumerate.__main__ import PortScan
from direnumerate.colors import Color
from direnumerate.version import __version__


def dir_scan(args):
    try:
        url = args.url
        wordlist_file = args.wordlist

        enum = DirScan(url, wordlist_file)
        enum.dir_enum()
    except TypeError:
        print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
    except KeyboardInterrupt:
        print(Color.GREEN + "-------------- attempt interrupted by user ------------" + Color.RESET)


def port_scan(args):
    try:
        host = args.target
        start_port = args.start_port
        end_port = args.end_port

        scanner = PortScan(host, start_port, end_port)
        scanner.scan_ports()
    except KeyboardInterrupt:
        print(Color.GREEN + "-------------- Port scan interrupted by user ------------" + Color.RESET)


def main():
    parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
    subparsers = parser.add_subparsers(title="subcommands")

    dir_parser = subparsers.add_parser("dir-scan", help="Perform directory enumeration")
    dir_parser.add_argument("-u", "--url", required=True, help="Target URL (including scheme, e.g. http://www.example.com)")
    dir_parser.add_argument("-w", "--wordlist", required=True, help="wordlist file")
    dir_parser.set_defaults(func=dir_scan)

    port_parser = subparsers.add_parser("port-scan", help="Perform port scanning")
    port_parser.add_argument("-t", "--target", required=True, help="Target host")
    port_parser.add_argument("-s", "--start-port", required=True, type=int, help="Start port")
    port_parser.add_argument("-e", "--end-port", required=True, type=int, help="End port")
    port_parser.set_defaults(func=port_scan)

    parser.add_argument("-V", "--version", required=True, help=__version__)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()




