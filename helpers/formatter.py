from rich import print
from rich.panel import Panel


def print_ports(ports):
    print("\n[bold cyan]Ports:[/bold cyan]")

    if not ports:
        print("[yellow]⚠ No open ports found[/yellow]")
        return

    for p in ports:
        banner = f" | {p['banner']}" if p['banner'] else ""
        print(f"[green]✔ {p['port']}[/green] ({p['service']}){banner}")


def print_headers(headers):
    print("\n[bold cyan]Security Headers:[/bold cyan]")

    for k, v in headers.items():
        short = k.replace("Content-Security-Policy", "CSP") \
                 .replace("X-Frame-Options", "X-Frame") \
                 .replace("Strict-Transport-Security", "HSTS")

        if v == "MISSING":
            print(f"[red]✖ {short}[/red] [dim](missing)[/dim]")
        else:
            print(f"[green]✔ {short}[/green]")

    if headers.get("Content-Security-Policy") == "MISSING":
        print("[yellow]⚠ No CSP → possible XSS risk[/yellow]")


def print_ssl(ssl):
    print("\n[bold cyan]SSL:[/bold cyan]")

    if isinstance(ssl, dict):
        if ssl.get("valid"):
            print(f"[green]✔ Valid[/green], expires: [yellow]{ssl.get('expires')}[/yellow]")
        else:
            print("[red]✖ Invalid SSL[/red]")
    else:
        print(ssl)


def print_score(score):
    if score >= 80:
        color = "green"
    elif score >= 50:
        color = "yellow"
    else:
        color = "red"

    print(f"\n[bold {color}]Security Score: {score}/100[/bold {color}]\n")


def print_result(target, https, headers, ports, ssl, server, ip, whois_data, score):

    print(Panel(f"[bold magenta]{target}[/bold magenta]", title="Scan Result"))


    print("[bold cyan]HTTPS:[/bold cyan]")
    if https:
        print("[green]✔ HTTPS enabled[/green]")
    else:
        print("[red]✖ HTTPS not available[/red]")


    print_headers(headers)


    print_ports(ports)


    print("\n[bold cyan]Server Info:[/bold cyan]")
    print(f"Server: [yellow]{server}[/yellow]")
    print(f"IP: [yellow]{ip}[/yellow]")


    print("\n[bold cyan]WHOIS:[/bold cyan]")
    print(f"[dim]{whois_data}[/dim]")


    print_ssl(ssl)


    print_score(score)