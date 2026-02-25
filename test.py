import requests

url = "http://localhost:5000/api/v1"

try:
    req = requests.post(
        f"{url}/users",
        json={
            'first_name': 'John',
            'last_name': 'Due',
            'email': 'john.due@example.com'
            })
    if req.status_code == 201:
        user = req.json()
    else:
        print("Failed to create user")
except Exception as e:
    print(e)

try:
    req = requests.post(
        f"{url}/amenities",
        json={
            'name': 'Wi-Fi'
        }
    )
    if req.status_code == 201:
        amenity = req.json()
    else:
        print("Failed to create amenity")
except Exception as e:
    print(e)

try:
    req = requests.post(
        f"{url}/places",
        json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": user['id']
        }
    )
    if req.status_code == 201:
        place = req.json()
    else:
        print("Failed to create place")
except Exception as e:
    print(e)

try:
    req = requests.post(
        f"{url}/reviews",
        json={
            'text': 'My test review',
            'rating': 5,
            'place_id': place['id'],
            'user_id': user['id']
        }
    )
    if req.status_code == 201:
        review = req.json()
    else:
        print("Failed to create review")
except Exception as e:
    print(e)

try:
    req = requests.put(
        f"{url}/places/{place['id']}",
        json={
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "amenities": [
                amenity['id']
            ],
            "owner_id": user['id']
        }
    )
    if req.status_code == 200:
        updated_place = req.json()
    else:
        print("Failed to update place")
except Exception as e:
    print(e)

try:
    req = requests.get(
        f"{url}/places/{place['id']}"
    )
    print(req.status_code, req.text)

    if req.status_code == 200:
        fetch_place = req.json()
    else:
        print("Failed to fetch place")
except Exception as e:
    print(e)

print(user)
print("\n------------------------------------\n")
print(amenity)
print("\n------------------------------------\n")
print(place)
print("\n------------------------------------\n")
print(review)
print("\n------------------------------------\n\n")
print(updated_place)
print("\n------------------------------------\n")
print(fetch_place)
