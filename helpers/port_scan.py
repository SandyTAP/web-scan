import socket
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}


def resolve_target(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        raise Exception("Failed to resolve domain")


def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip, port))

            service = COMMON_PORTS.get(port, "Unknown")

            banner = ""
            try:
                s.sendall(b"\r\n")
                banner = s.recv(1024).decode(errors="ignore").strip()
            except:
                pass

            return {
                "port": port,
                "service": service,
                "banner": banner
            }

    except (socket.timeout, ConnectionRefusedError, OSError):
        return None


def scan_ports(domain, ports=None):
    if ports is None:
        ports = range(1, 1000)

    ip = resolve_target(domain)

    results = []

    workers = min(200, (os.cpu_count() or 1) * 20)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in ports]

        total = len(ports)
        completed = 0

        for future in as_completed(futures):
            completed += 1
            percent = (completed / total) * 100
            print(f"\rScanning: {completed}/{total} ({percent:.1f}%)", end="")

            result = future.result()
            if result:
                results.append(result)

    print()

    return sorted(results, key=lambda x: x["port"])