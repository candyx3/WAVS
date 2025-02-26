// script.js

document.addEventListener('DOMContentLoaded', function() {
    const scanForm = document.getElementById('scan-form');
    const resultsContainer = document.getElementById('results-container');

    scanForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const targetUrl = document.getElementById('target-url').value;

        if (targetUrl) {
            resultsContainer.innerHTML = '<p>Scanning...</p>';
            fetch(`/scan?url=${encodeURIComponent(targetUrl)}`)
                .then(response => response.json())
                .then(data => {
                    displayResults(data);
                })
                .catch(error => {
                    resultsContainer.innerHTML = '<p>Error occurred during scanning.</p>';
                    console.error('Error:', error);
                });
        } else {
            alert('Please enter a target URL.');
        }
    });

    function displayResults(data) {
        resultsContainer.innerHTML = '';
        if (data.vulnerabilities.length === 0) {
            resultsContainer.innerHTML = '<p>No vulnerabilities found.</p>';
        } else {
            const ul = document.createElement('ul');
            data.vulnerabilities.forEach(vulnerability => {
                const li = document.createElement('li');
                li.textContent = vulnerability;
                ul.appendChild(li);
            });
            resultsContainer.appendChild(ul);
        }
    }
});