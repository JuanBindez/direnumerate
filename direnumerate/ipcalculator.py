

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

# Função para calcular a classe de um endereço IP
def calculate_ip_class(ip):
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
            return "Inválido"

# Função para calcular a máscara de sub-rede de um endereço IP
def calculate_subnet_mask(ip):
        if not is_valid_ip(ip):
            return "Endereço IP inválido"
        
        first_octet = int(ip.split('.')[0])
        
        if 1 <= first_octet <= 126:
            return "255.0.0.0"
        elif 128 <= first_octet <= 191:
            return "255.255.0.0"
        elif 192 <= first_octet <= 223:
            return "255.255.255.0"
        else:
            return "Máscara de sub-rede não aplicável"