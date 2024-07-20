document.addEventListener('DOMContentLoaded', (event) => {
    fetchCounter();
});

const API_BASE_URL = 'http://very-simple-webapp-cloud--alb-1320831811.us-east-1.elb.amazonaws.com'; // Replace with ALB DNS name once provisioned

function fetchCounter() {
    console.log('====> DOM CONTENT LOADED, CALLING fetchCounter FUNCTION.') // logging

    fetch(`${API_BASE_URL}/api/counter`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('counter').innerText = data.counter;
        })
        .catch(error => console.error('Error fetching counter:', error));
}

function incrementCounter() {
    console.log('====> BUTTON CLICKED, CALLING incrementCounter FUNCTION.') // logging

    fetch(`${API_BASE_URL}/api/increment`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('counter').innerText = data.counter;
    })
    .catch(error => console.error('Error incrementing counter:', error));
}