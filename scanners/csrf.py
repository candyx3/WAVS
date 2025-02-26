from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def detect_csrf(url):
    """
    Detects potential CSRF vulnerabilities in the given URL.
    
    Args:
        url (str): The target URL to scan for CSRF vulnerabilities.
    
    Returns:
        dict: A dictionary containing the results of the CSRF scan.
    """
    results = {
        "url": url,
        "csrf_vulnerable": False,
        "csrf_token_found": False,
        "csrf_token_name": None,
        "csrf_token_value": None,
    }

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        forms = soup.find_all('form')

        for form in forms:
            csrf_token_found = False
            for input_tag in form.find_all('input'):
                if input_tag.get('name') in ['csrf_token', 'authenticity_token']:
                    csrf_token_found = True
                    results["csrf_token_found"] = True
                    results["csrf_token_name"] = input_tag.get('name')
                    results["csrf_token_value"] = input_tag.get('value')
                    break
            if not csrf_token_found:
                results["csrf_vulnerable"] = True
                break #If one form is vulnerable, mark it as vulnerable

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        results["error"] = str(e)
    except Exception as e:
        print(f"Error: {e}")
        results["error"] = str(e)

    return results