import os

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    SCAN_TIMEOUT = 10  # seconds
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///scanner.db')
    
    # Vulnerability scanning settings
    SQL_INJECTION_ENABLED = True
    XSS_ENABLED = True
    CSRF_ENABLED = True
    SSRF_ENABLED = True
    OPEN_REDIRECT_ENABLED = True

    # Add any additional configuration settings as needed
