import requests

def detect_open_redirect(url):
    """
    Function to detect open redirect vulnerabilities in a given URL.
    It checks if the URL redirects to an external site when accessed.
    """
    # List of test URLs to check for open redirects
    test_urls = [
        "http://example.com",
        "https://example.com",
        "http://malicious.com",
        "https://malicious.com"
    ]
    
    results = []
    
    for test_url in test_urls:
        # Simulate a request to the target URL with a redirect
        try:
            response = requests.get(url + "?redirect=" + test_url, allow_redirects=True, timeout=5)
        
            # Check if the response URL is the same as the test URL
            if response.url == test_url:
                results.append(f"Open redirect detected: {test_url}")
        except requests.exceptions.RequestException:
            continue
    
    return results