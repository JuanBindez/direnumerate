import argparse
from direnumerate.__main__ import DirScan, PortScan
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
        print(Color.GREEN + "-------------- Attempt interrupted by user ------------" + Color.RESET)

def port_scan(args):
    try:
        host = args.target
        ports = args.ports

        scanner = PortScan(host, ports)
        scanner.scan_ports()
    except KeyboardInterrupt:
        print(Color.GREEN + "-------------- Port scan interrupted by user ------------" + Color.RESET)

def main():
    parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
    subparsers = parser.add_subparsers(title="subcommands")

    # Subcomando Ds com nome "Ds" (sem hífen)
    dir_parser = subparsers.add_parser("Ds", help="Perform directory enumeration")
    dir_parser.add_argument("-u", "--url", required=True, help="Target URL (including scheme, e.g. http://www.example.com)")
    dir_parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    dir_parser.set_defaults(func=dir_scan)

    # Subcomando Ds com nome "-Ds" (com hífen)
    dir_parser_hyphen = subparsers.add_parser("-Ds", help=argparse.SUPPRESS)  # Suprimir a ajuda para evitar duplicações
    dir_parser_hyphen.add_argument("-u", "--url", required=True, help="Target URL (including scheme, e.g. http://www.example.com)")
    dir_parser_hyphen.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    dir_parser_hyphen.set_defaults(func=dir_scan)

    # Subcomando Ps
    port_parser = subparsers.add_parser("Ps", help="Perform port scanning")
    port_parser.add_argument("-t", "--target", required=True, help="Target host")
    port_parser.add_argument("-p", "--ports", nargs='+', type=int, required=True, help="Ports to scan (e.g., 22 80 443)")
    port_parser.set_defaults(func=port_scan)

    args = parser.parse_args()

    # Verifica qual subcomando foi chamado
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()