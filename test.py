from direnumerate import DirScan

url = "testphp.vulnweb.com"
wordlist = "wordlist.txt"

enum = DirScan(url, wordlist)
enum.dir_enum()