document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Send a POST request to the backend with the credentials
    fetch('http://localhost:5000/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email, password})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (data.is_admin) {
                localStorage.setItem('accessToken', data.access_token); // Store access token in local storage
                localStorage.setItem('refreshToken', data.refresh_token); // Store refresh token in local storage
                // Redirect to the admin homepage 
                window.location.href = 'adminhome.html';
            } 
            else if (data.is_vendor) {
                localStorage.setItem('accessToken', data.access_token); // Store access token in local storage
                localStorage.setItem('refreshToken', data.refresh_token); // Store refresh token in local storage
                // Redirect to the vendor homepage 
                window.location.href = 'vendorhome.html';
            } else{
                localStorage.setItem('accessToken', data.access_token); // Store access token in local storage
                localStorage.setItem('refreshToken', data.refresh_token); // Store refresh token in local storage
                // Redirect to the homepage or perform any other action
                window.location.href = 'http://127.0.0.1:5500/frontend/homepage/homepage.html';
            }   
        } else {
            document.getElementById('message').innerText = data.message;
        }
    })
    .catch(error => console.error('Error:', error));
});


// ------------------------handling token-------------------------

function fetchData() {
    const accessToken = localStorage.getItem('accessToken');
    fetch('/protected', {
        method: '',
        headers: {
            'Authorization': 'Bearer ' + accessToken
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else if (response.status === 401) {
            // Access token expired, try refreshing
            return refreshTokenAndRetry('/protected');
        } else {
            throw new Error('Network response was not ok');
        }
    })
    .then(data => {
        // Handle the fetched data
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function refreshTokenAndRetry(url) {
    const refreshToken = localStorage.getItem('refreshToken');
    return fetch('http://localhost:5000/auth/token/refresh', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ refreshToken })
    })
    .then(response => response.json())
    .then(data => {
        if (data.accessToken) {
            localStorage.setItem('accessToken', data.accessToken);
            return fetchData(); // Retry the original request
        } else {
            throw new Error('Failed to refresh access token');
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    fetchData(); // Fetch data when the page loads
});

