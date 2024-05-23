import socket

from direnumerate.colors import Color

class PortScan:
    """
    A class for port scanning.

    Attributes:
        host (str): The host to scan for open ports.
        ports (list): A list of ports to scan.
        open_ports (list): A list to store open ports.
    """
    def __init__(self, host):
        """
        Initializes a PortScan instance.

        Args:
            host (str): The host to scan for open ports.
            ports (list): A list of ports to scan.
        """
        self.host = host.replace("https://", "")
        self.open_ports = []

    def scan_ports(self, ports) -> list:
        """
        Scan the specified ports on the target host.

        This method attempts to establish a TCP connection to each port in the list of ports on the target host.
        If the connection is successful (result == 0), the port is considered open, and it is added to the open_ports list.
        If the connection fails, the port is considered closed.

        The results are printed to the console, indicating whether each port is open or closed.

        Raises:
            socket.gaierror: If an invalid host is provided.
        """
        self.ports = ports
        
        try:
            for port in self.ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)

                result = sock.connect_ex((self.host, port))

                if result == 0:
                    self.open_ports.append(port)
                    results = f"{Color.GREEN} [http://{self.host}] port: {port} is open, {Color.RESET}"
                    print(results)
                   
                else:
                    results = f"{Color.RED} [http://{self.host}] port: {port} is closed, {Color.RESET}"
                    print(results)
                
        except socket.gaierror as sq:
            print(sq)
            print(Color.RED + "[Error]" + Color.RESET)
        sock.close()

        return self.open_ports