.. _portscan:

Port Scan
=============================

**If you want to check if specific ports are open on a host, use something like this:**::

        from direnumerate import Scan

        ip = "44.228.249.3"
        list_ports = [22, 80, 443]

        scan = Scan(ip)
        scan.ports(list_ports)
