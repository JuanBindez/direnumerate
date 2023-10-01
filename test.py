from direnumerate import PortScan

ip = "www.exemple.com"
list_ports = [22, 80, 443]

scan = PortScan(ip, list_ports)
scan.scan_ports()