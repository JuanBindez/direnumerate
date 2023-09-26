from direnumerate import DirScan

url = input("url target here >")
wordlist = "wordlist.txt"

enum = DirScan(url, wordlist)
enum.dir_enum()