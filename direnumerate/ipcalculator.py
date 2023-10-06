

def is_valid_ip(ip):
        try:
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not 0 <= int(part) <= 255:
                    return False
            return True
        except ValueError:
            return False


def calculate_ip_class(ip):
        """ Funtion to calculate the class of the ipaddress """
        first_octet = int(ip.split('.')[0])
        if 1 <= first_octet <= 126:
            return "A"
        elif 128 <= first_octet <= 191:
            return "B"
        elif 192 <= first_octet <= 223:
            return "C"
        elif 224 <= first_octet <= 239:
            return "D (Multicast)"
        elif 240 <= first_octet <= 255:
            return "E (Experimental)"
        else:
            return "Invalid"


def calculate_subnet_mask(ip):
        """Function to calculate the subnet mask of the a ipadress"""
        if not is_valid_ip(ip):
            return "Invalid IP address."
        
        first_octet = int(ip.split('.')[0])
        
        if 1 <= first_octet <= 126:
            return "255.0.0.0"
        elif 128 <= first_octet <= 191:
            return "255.255.0.0"
        elif 192 <= first_octet <= 223:
            return "255.255.255.0"
        else:
            return "Subnet mask not applicable."
        
def calculate_ip_count(ip):
    first_octet = int(ip.split('.')[0])
    
    if 1 <= first_octet <= 126:
        return 2 ** 24  # Classe A (16.777.214 endereços IP para hosts)
    elif 128 <= first_octet <= 191:
        return 2 ** 16  # Classe B (65.534 endereços IP para hosts)
    elif 192 <= first_octet <= 223:
        return 2 ** 8   # Classe C (254 endereços IP para hosts)
    else:
        return "Não aplicável"
    

def calculate_subnet_notation(subnet_notation):
    try:
        ip, subnet_mask = subnet_notation.split("/")
        ip_parts = ip.split(".")
        subnet_bits = int(subnet_mask)

        if 0 <= subnet_bits <= 32 and len(ip_parts) == 4:
            ip_count = 2 ** (32 - subnet_bits)
            return ip_count
        else:
            return "Notação de sub-rede inválida"
    except ValueError:
        return "Notação de sub-rede inválida"


def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D (Multicast)'
    elif 240 <= first_octet <= 255:
        return 'E (Experimental)'
    else:
        return 'Inválido'

# Função para calcular as notações de sub-rede possíveis com base na classe
def calculate_possible_subnets(ip_class):
    if ip_class == 'A':
        return ['/8', '/16', '/24']
    elif ip_class == 'B':
        return ['/16', '/24']
    elif ip_class == 'C':
        return ['/24']
    else:
        return []
