from direnumerate import PortScan

ip = "44.228.249.3"
list_ports = [22, 80, 443]

scan = PortScan(ip, list_ports)
scan.scan_ports()