document.addEventListener('DOMContentLoaded', (event) => {
    fetchCounter();
});

function fetchCounter() {
    console.log('====> DOM CONTENT LOADED, CALLING fetchCounter FUNCTION.') // logging
    fetch('/api/counter')
        .then(response => response.json())
        .then(data => {
            document.getElementById('counter').innerText = data.counter;
        })
        .catch(error => console.error('Error fetching counter:', error));
}

function incrementCounter() {
    console.log('====> BUTTON CLICKED, CALLING incrementCounter FUNCTION.') // logging
    fetch('/api/increment', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('counter').innerText = data.counter;
    })
    .catch(error => console.error('Error incrementing counter:', error));
}