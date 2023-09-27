import argparse

from direnumerate.__main__ import DirScan
from direnumerate.__main__ import PortScan
from direnumerate.colors import Color
from direnumerate.version import __version__

def main():
    try:
        parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
        parser.add_argument("-u", "--url", required=True, help="Target URL (including scheme, e.g. http://www.example.com)")
        parser.add_argument("-w", "--wordlist", required=True, help="wordlist file")
        parser.add_argument("-V", "--version", required=True, help=__version__)
        parser.add_argument("-p", "--portscan", required=True, help="port Scan")
        parser.add_argument("-i", "--ip", required=True, help="ipaddress")
        parser.add_argument("-s", "--startport", required=True, help="inicial port")
        parser.add_argument("-e", "--endport", required=True, help="final port")


        args = parser.parse_args()

        if args.portscan:
            ip = args.portstart
            start_port = args.startport
            end_port = args.endport

            scan = PortScan(ip, start_port, end_port)
            scan.open_ports()
            pass
        else:
            pass

        url = args.url
        wordlist_file = args.wordlist

        enum = DirScan(url, wordlist_file)
        enum.dir_enum()
    except TypeError:
        print(Color.GREEN + "-------------------- Scan Finished --------------------" + Color.RESET)
    except KeyboardInterrupt:
        print(Color.GREEN + "-------------- attempt interrupted by user ------------" + Color.RESET)

if __name__ == "__main__":
    main()
