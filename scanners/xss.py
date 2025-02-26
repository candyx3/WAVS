from urllib.parse import urlparse, urljoin
import requests

class XSSScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg/onload=alert('XSS')>",
            "';alert(1);//",
            "<iframe src='javascript:alert(1)'></iframe>"
        ]

    def scan(self):
        vulnerabilities = []
        for payload in self.payloads:
            response = self.send_request(payload)
            if self.is_vulnerable(response, payload):
                vulnerabilities.append(payload)
        return vulnerabilities

    def send_request(self, payload):
        parsed_url = urlparse(self.target_url)
        if not parsed_url.scheme:
            self.target_url = 'http://' + self.target_url
        test_url = urljoin(self.target_url, f"?search={payload}")
        try:
            response = requests.get(test_url)
            return response
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def is_vulnerable(self, response, payload):
        if response is None:
            return False
        return payload in response.text

def main():
    target_url = input("Enter the target URL: ")
    scanner = XSSScanner(target_url)
    vulnerabilities = scanner.scan()
    if vulnerabilities:
        print("XSS vulnerabilities found:")
        for v in vulnerabilities:
            print(f" - {v}")
    else:
        print("No XSS vulnerabilities found.")

if __name__ == "__main__":
    main()