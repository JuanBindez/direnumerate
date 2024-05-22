from direnumerate import DirScan

url = "https://paraty.com.br"
wordlist = "wordlist.txt"

enum = DirScan(url)
results = enum.dir_enum(verbose=False, wordlist_file=wordlist)

print(results)