/* 
	This is a SAMPLE FILE to get you started.
	Please, follow the project instructions to complete the tasks.
*/

// Event listener for when the DOM content is fully loaded

document.addEventListener('DOMContentLoaded', () => {

	// Check if we are on the index page and verify the token
	if (window.location.pathname.search('index.html')) {
		const token = getCookie('token');
		console.log('Token:', token); // Debugging line to check the token value to remove on the final version
		if (!token) {
			window.location.href = 'login.html';
			return;
		}
	}
	if (window.location.pathname.search('index.html')) {
		displayPlaces();
	}
	
	// Check if we are on the login page and set up the login form handler
	if (window.location.pathname.search('login.html')) {
		const loginForm = document.getElementById('login-form');

		if (loginForm) {
			loginfunction(loginForm);
		} else {
			console.error('Login form not found!');
		}
	}
	// No login button if the user is connected
	const loginLink = document.getElementById('login-display')
	if (!getCookie('token')) {
        loginLink.style.display = 'block';
    }

	if (window.location.pathname.search('place.html')) {
		displayPlaceDetails();
	}
});

// LOGIN PAGE

// Event listener for the details buttons on the index page
document.addEventListener('click', (event) => {
	if (event.target.classList.contains('details-button')) {
		const placeId = event.target.getAttribute('data-id');
		navigateToPlaceDetails(placeId);
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


// INDEX PAGE


// Function to fetch and display places on the index page
// Need to be corrected because it doesn't apply the price bound to the place -> I think it is corrected but not tested correctly
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

				if (isNaN(NumberpriceFilter) || (parseFloat(place.price) >= NumberpriceFilter)) {

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


// PLACE DETAILS PAGE


// Function to navigate to the place details page when the "View Details" button is clicked
function navigateToPlaceDetails(placeId) {
	const buttonViewDetails = document.getElementsByClassName('details-button');
	for (let button of buttonViewDetails) {
		button.addEventListener('click', () => {
			const placeId = button.getAttribute('data-id');
			console.log('Navigating to place details for ID:', placeId); // Debugging line to check the place ID value to remove on the final version
			window.location.href = `place.html?id=${placeId}`; // Wrong URL, need to be corrected to pass the place ID as a query parameter
		});
	}
}

// Function to fetch and display place details on the place details page
function getPlaceIdFromURL() {
	const urlParams = new URLSearchParams(window.location.search);
	console.log('URL Parameters:', urlParams.toString()); // Debugging line to check the URL parameters to remove on the final version
	return urlParams.get('id');
}

// Function to fetch and display place details on the place details page
function displayPlaceDetails() {
	const placeId = getPlaceIdFromURL();
	fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`)
		.then(response => response.json())
		.then(place => {
			const td = document.createElement('td');
			console.log('Place Details:', place); // Debugging line to check the place details to remove on the final version
			td.className = 'place-values';
			td.innerHTML = `
				<h2>${place.title}</h2>
				<p>Price: ${place.price} \$</p>
				<p>Description: ${place.description}</p>
				<p>Latitude: ${place.latitude}</p>
				<p>Longitude: ${place.longitude}</p>
				<p>Owner ID: ${place.user_id}</p>
				<p>Reviews: ${place.reviews}</p>
				<p>Amenities: ${place.amenities}</p>
			`;
			document.getElementById('place-details').appendChild(td);
		})
		.catch(error => {
			console.error('Error fetching place details:', error);
		});
}


// ADD REVIEWS TO PLACE DETAILS PAGE


// COOKIES

// Helper function to get a cookie value by name
function getCookie(name) {
    const cookies = document.cookie;
	const cookieArray = cookies.split(';');

// Need a datetime delete of the cookie to be better

	for (let cookie of cookieArray) {
		cookie = cookie.trim();
		if (cookie.startsWith(name + '=')) {
			return cookie.substring(name.length + 1);
		}
	}
	return null;
}