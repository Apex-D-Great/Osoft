document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Send a POST request to the backend with the credentials
    fetch('http://localhost:5000/auth/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email, password, username})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = 'http://127.0.0.1:5500/frontend/index.html';
        } else {
            document.getElementById('message').innerText = data.message;
        }
    })
    .catch(error => console.error('Error:', error));
});

