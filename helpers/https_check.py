import requests

def check_https(domain):
    try:
        r = requests.get("https://" + domain, timeout=5)
        return True
    except:
        return False