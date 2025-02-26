from flask import Flask, render_template, request, redirect, url_for
from utils import scanner_utils

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target_url = request.form['url']
    vulnerabilities = scanner_utils.scan_vulnerabilities(target_url)
    return render_template('results.html', vulnerabilities=vulnerabilities)

@app.route('/results')
def results():
    # You'll need to figure out how to pass the vulnerabilities to this route
    # For example, you could store them in a session or a database
    return render_template('results.html', vulnerabilities=[])  # Replace [] with actual data

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)