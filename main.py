from direnumerate import Scan

host = 'https://paraty.com'
wordlist = 'wordlist.txt'

enum = Scan(host)
print(enum.ports(log=True, ports=[22, 80, 443, 8080]))
