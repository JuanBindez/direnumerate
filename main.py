from direnumerate import Scan

host = 'https://paraty.com.br'
wordlist = 'wordlist.txt'

enum = Scan(host)
print(enum.dirs(log=True, wordlist_file=wordlist))
