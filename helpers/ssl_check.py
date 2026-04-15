import ssl
import socket
from datetime import datetime

def check_ssl(domain):
    ctx = ssl.create_default_context()
    try:
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(5)
            s.connect((domain, 443))
            cert = s.getpeercert()
            expiry = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            return {"valid": True, "expires": expiry.strftime("%Y-%m-%d")}
    except:
        return {"valid": False}