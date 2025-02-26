def generate_report(scan_results):
    report = "Vulnerability Scan Report\n"
    report += "=" * 30 + "\n\n"
    
    for vulnerability, details in scan_results.items():
        report += f"Vulnerability: {vulnerability}\n"
        report += f"Description: {details['description']}\n"
        report += f"Severity: {details['severity']}\n"
        report += f"URL: {details['url']}\n"
        report += "-" * 30 + "\n"
    
    return report

def save_report_to_file(report, filename):
    with open(filename, 'w') as file:
        file.write(report)

def format_results_for_display(scan_results):
    formatted_results = []
    
    for vulnerability, details in scan_results.items():
        formatted_results.append({
            "vulnerability": vulnerability,
            "description": details['description'],
            "severity": details['severity'],
            "url": details['url']
        })
    
    return formatted_results