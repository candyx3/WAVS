# Web App Vulnerability Scanner

This project is a web application vulnerability scanner designed to identify common security vulnerabilities in web applications. It supports scanning for various vulnerabilities including SQL Injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), Server-Side Request Forgery (SSRF), and Open Redirects.

## Features

- **User-Friendly Interface**: An elegant and stylish UI for easy navigation and interaction.
- **Multiple Vulnerability Scanners**: Implements various scanners to detect different types of vulnerabilities.
- **Detailed Reporting**: Provides comprehensive reports on detected vulnerabilities.

## Project Structure

```
web-app-vulnerability-scanner
├── main.py                # Entry point of the application
├── requirements.txt       # Project dependencies
├── templates              # HTML templates for the web application
│   ├── base.html          # Base template
│   ├── index.html         # Landing page for input
│   └── results.html       # Results page for displaying scan results
├── static                 # Static files (CSS, JS)
│   ├── css
│   │   └── style.css      # Styles for the web application
│   └── js
│       └── script.js      # Client-side JavaScript
├── utils                  # Utility functions
│   ├── scanner_utils.py   # Functions for scanning
│   └── report_utils.py    # Functions for report generation
├── scanners               # Vulnerability scanners
│   ├── sql_injection.py   # SQL Injection scanner
│   ├── xss.py             # XSS scanner
│   ├── csrf.py            # CSRF scanner
│   ├── ssrf.py            # SSRF scanner
│   └── open_redirect.py    # Open Redirect scanner
├── config.py              # Configuration settings
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/candyx3/WAVS.git
   cd web-app-vulnerability-scanner
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter the target URL you wish to scan and submit the form.

4. Review the results displayed on the results page.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
