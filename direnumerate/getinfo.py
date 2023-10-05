import requests

def get_info_ip(ip):
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()
        return data