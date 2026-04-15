import sys
from helpers.https_check import check_https
from helpers.headers_check import check_headers
from helpers.port_scan import scan_ports
from helpers.ssl_check import check_ssl
from helpers.formatter import print_result
from helpers.analyzer import detect_server, get_ip_info, get_whois, calculate_score
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Web Security Scanner")
    parser.add_argument("target", help="Target domain (example.com)")
    parser.add_argument("--mode", choices=["fast", "full"], default="full", help="Scan mode")
    parser.add_argument("--json", action="store_true", help="Output in JSON")
    return parser.parse_args()
def main():
    args = parse_args()
    target = args.target

    https = check_https(target)
    headers = check_headers(target)
    ports = scan_ports(target)
    ssl = check_ssl(target)

    server = detect_server(target)
    ip = get_ip_info(target)
    whois_data = get_whois(target)

    score = calculate_score(https, headers, ssl)

    print_result(target, https, headers, ports, ssl, server, ip, whois_data, score)

if __name__ == "__main__":
    main()