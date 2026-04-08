/* 
	This is a SAMPLE FILE to get you started.
	Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
	
	// Check if we are on the index page and verify the token
	if (window.location.pathname.endsWith('index.html')) {
		const token = getCookie('token');
		// If no token is found, redirect to the login page
		if (!token) {
			window.location.href = 'login.html';
			return;
		}
	}
	if (window.location.pathname.endsWith('index.html')) {
		displayPlaces();
	}
	
	// Check if we are on the login page and set up the login form handler
	if (window.location.pathname.endsWith('login.html')) {
		const loginForm = document.getElementById('login-form');

		if (loginForm) {
			loginfunction(loginForm);
		} else {
			console.error('Login form not found!');
		}
	}
});

// Function to handle login form submission
function loginfunction(loginForm) {
	loginForm.addEventListener('submit', async (event) => {
		event.preventDefault();
		const email = document.getElementById('email').value;
		const password = document.getElementById('password').value;
		async function loginUser(email, password) {
		    const response = await fetch('http://127.0.0.1:5000/api/v1/login', {
		        method: 'POST',
		        headers: {
		            'Content-Type': 'application/json'
		        },
		        body: JSON.stringify({ email, password })
		    });
			if (response.ok) {
			    const data = await response.json();
			    document.cookie = `token=${data.access_token}; path=/`;
			    window.location.href = 'index.html';
			} else {
			    alert('Login failed: ' + response.statusText);
			}
		}
		loginUser(email, password);
	});
}

// Helper function to get a cookie value by name
function getCookie(name) {
    const cookies = document.cookie;
	const cookieArray = cookies.split(';');
	// Loop through the cookies to find the one with the specified name
	for (let i = 0; i < cookieArray.length; i++) {
		const cookie = cookieArray[i].trim();
		if (cookie.startsWith(name + '=')) {
			return cookie.substring(name.length + 1);
		}
	}
	window.location.href = 'login.html';
	return null;

}


function displayPlaces() {
	fetch('http://127.0.0.1:5000/api/v1/places')
		.then(response => response.json())  // Parse JSON response
		.then(places => {
			const placesContainer = document.getElementById('cards');
			placesContainer.innerHTML = '';
			
			// Iterate through the places array
			places.forEach(place => {
				// Create a table cell
				const td = document.createElement('td');
				
				td.className = 'place-card';
				td.innerHTML = `
					<h2>${place.title}</h2>
					<p>Price: ${place.price} \$</p>
					<button class="details-button" data-id="${place.id}">View Details</button>
				`;
				
				// Append card to td, then td to container
				placesContainer.appendChild(td);
			});
		})
		.catch(error => {
			console.error('Error fetching places:', error);
		});
}