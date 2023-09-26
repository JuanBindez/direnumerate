from direnumerate import DirScan

def main():
    parser = argparse.ArgumentParser(description="Direnumerate - Directory Enumeration on Web Servers")
    parser.add_argument("-u", "--url", required=True, help="Target URL (including scheme, e.g. http://www.example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="wordlist file")

    args = parser.parse_args()
    url = args.url
    wordlist_file = args.wordlist

    DirScan(url, wordlist_file)
    dir_enum()

if __name__ == "__main__":
    main()
