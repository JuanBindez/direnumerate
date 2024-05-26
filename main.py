from direnumerate import Scan

host = 'https://example.com'
wordlist = 'wordlist.txt'

enum = Scan(host)
print(enum.dirs(wordlist_file=wordlist))
