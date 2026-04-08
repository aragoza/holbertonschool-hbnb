/* 
	This is a SAMPLE FILE to get you started.
	Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {

	// Check if we are on the index page and verify the token
	if (window.location.pathname.endsWith('index.html')) {
		const token = getCookie('token');
		console.log('Token:', token); // Debugging line to check the token value to remove on the final version
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

// Event listener for the details buttons on the index page
document.addEventListener('click', (event) => {
	if (event.target.classList.contains('details-button')) {
		const placeId = event.target.getAttribute('data-id');
		window.location.href = `place.html`;
	    return placeId;
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

// Function to fetch and display places on the index page
function displayPlaces(priceFilter = 0) {
	NumberpriceFilter = parseFloat(priceFilter);
	console.log('Price Filter:', NumberpriceFilter); 
	console.log('Type of Price Filter:', typeof NumberpriceFilter); // Debugging line to check the price filter value to remove on the final version
	fetch('http://127.0.0.1:5000/api/v1/places')
		.then(response => response.json())  // Parse JSON response
		.then(places => {
			const placesContainer = document.getElementById('cards');
			placesContainer.innerHTML = '';
			
			// Iterate through the places array
			places.forEach(place => {
				// Create a table cell for each place
				console.log('Place Price:', place.price); // Debugging line to check the place price value to remove on the final version
				console.log('Type of Place Price:', typeof parseFloat(place.price)); // Debugging line to check the place price value to remove on the final version

				if (isNaN(NumberpriceFilter) || parseFloat(place.price) <= NumberpriceFilter) {

					const td = document.createElement('td');
					
					td.className = 'place-card';
					td.innerHTML = `
						<h2>${place.title}</h2>
						<p>Price: ${place.price} \$</p>
						<button class="details-button" data-id="${place.id}">View Details</button>
					`;
					
					// Append a td to container
					placesContainer.appendChild(td);
				}
			});
		})
		.catch(error => {
			console.error('Error fetching places:', error);
		});
}

// Helper function to get a cookie value by name
function getCookie(name) {
    const cookies = document.cookie;
	const cookieArray = cookies.split(';');

	for (let cookie of cookieArray) {
		cookie = cookie.trim();
		if (cookie.startsWith(name + '=')) {
			return cookie.substring(name.length + 1);
		}
	}
	return null;
}

// Load the price to display only the places that are below the value

const list_prices = [10, 50, 100, "All"];
const priceFilter = document.getElementById('price-filter');

list_prices.forEach(price => {
	const option = document.createElement('option');
	option.value = price;
	option.textContent = price;
	priceFilter.appendChild(option);
});

priceFilter.addEventListener('change', () => {
	displayPlaces(priceFilter.value);
});