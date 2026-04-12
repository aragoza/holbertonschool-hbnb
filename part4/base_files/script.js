/* 
	This is a SAMPLE FILE to get you started.
	Please, follow the project instructions to complete the tasks.
*/

// Event listener for when the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', () => {

	// Check if we are on the index page and verify the token
	// To test the login you can write :
	// email: admin@hbnb.com
	// password: admin1234
	if (window.location.pathname.includes('index.html') || window.location.pathname.endsWith('/')) { // We will need to check the root path better later
		const token = getCookie('token');
		console.log('Token:', token); // Debugging line to check the token value to remove on the final version
		if (token) {
			loadPriceFilter();
			displayPlaces();
		}
	}
	// Check if we are on the login page and set up the login form handler
	if (window.location.pathname.includes('login.html')) {
		const loginForm = document.getElementById('login-form');

		if (loginForm) {
			loginfunction(loginForm);
		} else {
			console.error('Login form not found!');
		}
	}
	// No login button if the user is connected
	// To test the login you can write :
	// email: admin@hbnb.com
	// password: admin1234
	const loginLink = document.getElementById('login-button');
	if (loginLink) {
		if (!getCookie('token')) {
			loginLink.style.display = 'block';
		} else {
			loginLink.style.display = 'none';
		}
	}

	if (window.location.pathname.includes('index.html')) {
		const token = getCookie('token');
		console.log('Token:', token); // Debugging line to check the token value to remove on the final version
		if (!token) {
			window.location.href = 'login.html';
			return;
		} else {
			console.log('Token found.');
		}
	}

	if (window.location.pathname.includes('place.html')) {
		if (getCookie('token')) {
			navigateToAddReviewPage(getPlaceIdFromURL());
		}
		displayPlaceDetails();
		displayReviews();
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

// Event listener for the price filter dropdown on the index page
document.addEventListener('click', (event) => {
	if (event.target.classList.contains('price-filter')) {
		const priceFilter = event.target.value;
		displayPlaces(priceFilter);
	}
});

document.addEventListener('submit', (event) => {
	if (event.target.id === 'review-form') {
		event.preventDefault();
		const placeId = getPlaceIdFromURL();
		const reviewText = document.getElementById('review-text').value;
		const reviewRating = document.getElementById('review-rating').value;
		addReview(placeId, reviewText, reviewRating);
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
function displayPlaces(priceFilter = 'All') {
	console.log('Price Filter:', priceFilter); // Debugging line to check the price filter value to remove on the final version
	console.log('Type of Price Filter:', typeof priceFilter); // Debugging line to check the price filter value to remove on the final version
	fetch('http://127.0.0.1:5000/api/v1/places')
		.then(response => response.json())  // Parse JSON response
		.then(places => {
			const placesContainer = document.getElementById('places-cards'); // Get the ul element inside the places-list section
			placesContainer.innerHTML = '';
			places.forEach(place => {
				// Create a table cell for each place
				console.log('Place Price:', place.price); // Debugging line to check the place price value to remove on the final version
				console.log('Type of Place Price:', typeof parseFloat(place.price)); // Debugging line to check the place price value to remove on the final version

				if (priceFilter === 'All' || (parseFloat(place.price) <= parseFloat(priceFilter))) {

					const li = document.createElement('li');
					
					li.className = 'cards';
					li.innerHTML = `
						<h2>${place.title}</h2>
						<p>Price: ${place.price} \$</p>
						<button class="details-button" data-id="${place.id}">View Details</button>
					`;
					
					// Append a td to container
					placesContainer.appendChild(li);
				}
			});
		})
		.catch(error => {
			console.error('Error fetching places:', error);
		});
}

// Load the price to display only the places that are below the value
function loadPriceFilter() {
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
}


// PLACE DETAILS PAGE

function navigateToAddReviewPage(placeId) {
	const nav = document.getElementById('navigation');
	const addReviewLink = document.createElement('a');
	addReviewLink.href = `add_review.html?place_id=${placeId}`;
	addReviewLink.textContent = 'Add Review';
	addReviewLink.className = 'review-link';

	nav.appendChild(addReviewLink);
}


// Function to navigate to the place details page when the "View Details" button is clicked
function navigateToPlaceDetails(placeId) {
	window.location.href = `place.html?id=${placeId}`;
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
			const li = document.createElement('li');
			console.log('Place Details:', place); // Debugging line to check the place details to remove on the final version
			li.className = 'place-values';
			li.innerHTML = `
				<h2>${place.title}</h2>
				<p>Price: ${place.price} \$</p>
				<p>Description: ${place.description}</p>
				<p>Latitude: ${place.latitude}</p>
				<p>Longitude: ${place.longitude}</p>
				<p>Owner ID: ${place.user.first_name} ${place.user.last_name}</p>
				<p>Amenities: ${place.amenities.id}</p>
			`;
			document.getElementById('place-info').appendChild(li);
		})
		.catch(error => {
			console.error('Error fetching place details:', error);
		});
}

// Function to display the reviews for the place on the place details page
async function displayReviews() {
	const placeId = getPlaceIdFromURL();
	try {
		const response = await fetch(`http://127.0.0.1:5000/api/v1/reviews` , {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${getCookie('token')}`
			}
		});
		if (!response.ok) {
			throw new Error('Failed to fetch reviews');
		}
		const reviews = await response.json();
		const reviewsContainer = document.getElementById('review-card'); // Get the ul element inside the reviews section
		reviewsContainer.innerHTML = '';
		reviews.forEach(review => {
			if (review.place_id === placeId) {
				const li = document.createElement('li');
				li.className = 'cards';
				li.innerHTML = `
					<p>Comment: ${review.text}</p>
					<p>Author: ${review.user.first_name}</p>
					<p>Rating: ${review.rating}</p>
				`;
				reviewsContainer.appendChild(li);
			}

		});
	} catch (error) {
		console.error('Error fetching reviews:', error);
	}
}

// ADD REVIEWS PAGE


async function addReview(placeId, reviewText, reviewRating) {
	const token = getCookie('token');
	try {
		const response = await fetch(`http://127.0.0.1:5000/api/v1/reviews/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${token}`
			},
			body: JSON.stringify({
				place_id: placeId,
				text: reviewText,
				rating: reviewRating
			})
		});

		if (!response.ok) {
			throw new Error('Failed to add review');
		}

		return await response.json();
	} catch (error) {
		console.error('Error adding review:', error);
	}
}


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