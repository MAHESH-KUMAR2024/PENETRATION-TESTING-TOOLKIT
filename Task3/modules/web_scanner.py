import requests
from bs4 import BeautifulSoup

def scan_web(target_url):
    print(f"[+] Scanning for vulnerabilities on: {target_url}")

    # Check for SQL Injection vulnerability
    sql_payloads = ["'", "' OR 1=1 --", "\" OR \"\" = \"\"", "' OR 'a'='a"]
    for payload in sql_payloads:
        url = f"{target_url}{payload}"
        response = requests.get(url)
        if "error" in response.text.lower() or "sql" in response.text.lower():
            print(f"[!] Possible SQL Injection vulnerability detected at: {url}")

    # Check for XSS vulnerability
    xss_payloads = ["<script>alert('XSS')</script>", "\" onmouseover=\"alert('XSS')"]
    for payload in xss_payloads:
        params = {"input": payload}
        response = requests.get(target_url, params=params)
        if payload in response.text:
            print(f"[!] Possible XSS vulnerability detected at: {target_url} with payload {payload}")

    print("[+] Scan completed.")
