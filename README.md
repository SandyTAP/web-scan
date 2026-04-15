# 🔍 WebScan

> CLI web security scanner written in Python

---

## 🚀 Features

* 🔎 Fast port scanning (1–999)
* 🔐 SSL certificate analysis
* 🛡 Security headers check
* 🌐 Server detection
* 📡 IP & WHOIS lookup
* 📊 Security score system
* ⚡ Clean & colorful CLI output (rich)

---

## 📦 Installation

```bash
git clone https://github.com/SandyTAP/web-scan.git
cd web-scan
pip install -r requirements.txt
```

---

## ⚡ Usage

```bash
python scan.py example.com
```

---

## 🖥 Example Output

```
Scanning: 999/999 (100%)

╭────────────────────────────── Scan Result ───────────────────────────────╮
│ example.com                                                             │
╰─────────────────────────────────────────────────────────────────────────╯

✔ HTTPS enabled

✔ CSP
✔ X-Frame
✔ HSTS

✔ 80 (HTTP)
✔ 443 (HTTPS)

Server: cloudflare
IP: 8.47.69.0

SSL: ✔ Valid (expires: 2026-07-01)

Security Score: 70/100
```

---

## 📁 Project Structure

```
helpers/
  analyzer.py
  formatter.py
  port_scan.py
  ssl_check.py
  headers_check.py
scan.py
requirements.txt
```

---

## 🧠 How it works

WebScan analyzes a target by combining:

* Port scanning via sockets
* HTTP header inspection
* SSL certificate validation
* WHOIS and IP lookup
* Basic security scoring system

---

## ⚠️ Disclaimer

This tool is created for **educational purposes only**.
Do not scan systems without permission.

---

## ⭐ Support

If you like this project — give it a star ⭐
