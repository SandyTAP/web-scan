import requests
import socket
import whois
from rich import print


def detect_server(domain):
    try:
        r = requests.get(f"http://{domain}", timeout=2)
        return r.headers.get("Server", "Unknown")
    except:
        return "Unknown"


def get_ip_info(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return "Unknown"


def get_whois(domain):
    try:
        data = whois.whois(domain)
        return str(data.creation_date)
    except:
        return "Unknown"


def calculate_score(https, headers, ssl):
    score = 0

    if https:
        score += 30

    if ssl and "Valid" in str(ssl):
        score += 30

    missing = sum(1 for v in headers.values() if v == "MISSING")
    score += max(0, 40 - missing * 10)

    return score