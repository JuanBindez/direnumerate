from direnumerate import Scan

enum = Scan()
print(enum.port_scan(ip='44.228.249.3', ports=[22, 443, 8080, 8280, 80, 25]))
