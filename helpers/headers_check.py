import requests

def check_headers(domain):
    result = {}
    try:
        r = requests.get("https://" + domain, timeout=5)
        headers = r.headers

        result["Content-Security-Policy"] = "Content-Security-Policy" in headers
        result["X-Frame-Options"] = "X-Frame-Options" in headers
        result["Strict-Transport-Security"] = "Strict-Transport-Security" in headers

    except:
        result["error"] = True

    return result