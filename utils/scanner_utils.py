from scanners.sql_injection import SQLInjectionScanner
from scanners.xss import XSSScanner
from scanners.csrf import detect_csrf
from scanners.ssrf import is_vulnerable as ssrf_is_vulnerable
from scanners.open_redirect import detect_open_redirect

def scan_vulnerabilities(target_url):
    """
    Orchestrates the vulnerability scans.
    """
    vulnerabilities = []

    # SQL Injection
    sql_scanner = SQLInjectionScanner(target_url)
    sql_scanner.scan()
    sql_results = sql_scanner.get_results()
    print(f"SQL Injection results: {sql_results}")  # Add this line
    if sql_results and sql_results != ["No SQL Injection vulnerabilities found."]:
        for payload in sql_results:
            vulnerabilities.append({
                "type": "SQL Injection",
                "description": f"SQL Injection vulnerability found with payload: {payload}",
                "severity": "High",
                "url": target_url
            })

    # XSS
    xss_scanner = XSSScanner(target_url)
    xss_vulnerabilities = xss_scanner.scan()
    print(f"XSS vulnerabilities: {xss_vulnerabilities}")  # Add this line
    if xss_vulnerabilities:
        for payload in xss_vulnerabilities:
            vulnerabilities.append({
                "type": "XSS",
                "description": f"XSS vulnerability found with payload: {payload}",
                "severity": "Medium",
                "url": target_url
            })

    # CSRF
    csrf_results = detect_csrf(target_url)
    print(f"CSRF results: {csrf_results}")  # Add this line
    if csrf_results["csrf_vulnerable"]:
        vulnerabilities.append({
            "type": "CSRF",
            "description": "CSRF vulnerability detected",
            "severity": "Medium",
            "url": target_url
        })
    
    # SSRF
    ssrf_vulnerable, ssrf_results = ssrf_is_vulnerable(target_url)
    print(f"SSRF vulnerable: {ssrf_vulnerable}, results: {ssrf_results}")  # Add this line
    if ssrf_vulnerable:
         vulnerabilities.append({
            "type": "SSRF",
            "description": f"SSRF vulnerability detected",
            "severity": "High",
            "url": target_url
        })

    # Open Redirect
    open_redirect_results = detect_open_redirect(target_url)
    print(f"Open Redirect results: {open_redirect_results}")  # Add this line
    if open_redirect_results:
        for result in open_redirect_results:
            vulnerabilities.append({
                "type": "Open Redirect",
                "description": result,
                "severity": "Low",
                "url": target_url
            })

    return vulnerabilities