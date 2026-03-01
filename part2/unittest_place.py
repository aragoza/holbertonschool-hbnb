#!/usr/bin/env python3

import unittest
from app.__init__ import create_app
from math import nan

class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # Create a valid user for owner_id
        response = self.client.post("/api/v1/users/", json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.user_id = response.json["id"]

# ------------------------------
# POST /api/v1/places/ — success
# ------------------------------
    def test_create_place_success(self):
        payload = {
            "title": "Lovely House",
            "description": "Cozy and clean",
            "price": 120.0,
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": self.user_id,
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 201)
        self.assertIn("id", data)
        self.assertEqual(data.get("title"), "Lovely House")
        self.assertEqual(data.get("owner_id"), self.user_id)

# --------------------
# POST — Invalid title
# --------------------
    def test_create_place_invalid_title_less_than_3(self):
        payload = {
            "title": "A",
            "description": "Invalid title too short",
            "price": 100.0,
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": self.user_id,
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")
    
    def test_create_place_invalid_title_more_tahn_50(self):
        payload = {
            "title": "Hello, this is a very good place you should buy a night in this good place even if it has a long name it is really good trust me!!!!",
            "description": "Invalid title too long",
            "price": 100.0,
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": self.user_id,
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# --------------------------
# POST — Invalid description
# --------------------------

    def test_create_place_invalid_description(self):
        payload = {
            "title": "Invalid description / empty description",
            "description": "",
            "price": 100.0,
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": self.user_id,
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# -----------------------------
# POST — Invalid price alphabet
# -----------------------------

    def test_create_place_invalid_price_alphabet(self):
        payload = {
            "title": "Nice House",
            "description": "Valid description",
            "price": "Invalid price",
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": "nonexistent-user",
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# -------------------------
# POST — Invalid price bool
# -------------------------

    def test_create_place_invalid_price_bool(self):
        payload = {
            "title": "Nice House",
            "description": "Valid description",
            "price": True,
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": "nonexistent-user",
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# -----------------------------
# POST — Invalid price negative
# -----------------------------

    def test_create_place_invalid_price_negative(self):
        payload = {
            "title": "Nice House",
            "description": "Valid description",
            "price": -1,
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": "nonexistent-user",
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# ------------------------
# POST — Invalid price NaN
# ------------------------

    def test_create_place_invalid_price_NaN(self):
        payload = {
            "title": "Nice House",
            "description": "Valid description",
            "price": "NaN",
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": "nonexistent-user",
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# ------------------------------
# POST — Invalid price too much
# ------------------------------

    def test_create_place_invalid_price_more_than_billion(self):
        payload = {
            "title": "Nice House",
            "description": "Valid description",
            "price": 1.0e12,
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": "nonexistent-user",
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# ------------------------------
# Latitude Invalid Tests too low
# ------------------------------
    def test_create_place_latitude_too_low(self):
        payload = {
            "title": "Bad Latitude Low",
            "description": "Latitude < -90",
            "price": 100.0,
            "latitude": -91.0,
            "longitude": 0.0,
            "owner_id": self.user_id,
            "amenities": []
        }
        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# -------------------------------
# Latitude Invalid Tests too high
# -------------------------------

    def test_create_place_latitude_too_high(self):
        payload = {
            "title": "Bad Latitude High",
            "description": "Latitude > 90",
            "price": 100.0,
            "latitude": 91.0,
            "longitude": 0.0,
            "owner_id": self.user_id,
            "amenities": []
        }
        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# -------------------------------
# Longitude Invalid Tests too low
# -------------------------------
    def test_create_place_longitude_too_low(self):
        payload = {
            "title": "Bad Longitude Low",
            "description": "Longitude < -180",
            "price": 100.0,
            "latitude": 0.0,
            "longitude": -181.0,
            "owner_id": self.user_id,
            "amenities": []
        }
        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# --------------------------------
# Longitude Invalid Tests too high
# --------------------------------

    def test_create_place_longitude_too_high(self):
        payload = {
            "title": "Bad Longitude High",
            "description": "Longitude > 180",
            "price": 100.0,
            "latitude": 0.0,
            "longitude": 181.0,
            "owner_id": self.user_id,
            "amenities": []
        }
        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# --------------------
# POST — Invalid owner
# --------------------
    def test_create_place_invalid_owner(self):
        payload = {
            "title": "Nice House",
            "description": "Valid description",
            "price": 100.0,
            "latitude": 45.0,
            "longitude": 10.0,
            "owner_id": "nonexistent-user",
            "amenities": []
        }

        response = self.client.post("/api/v1/places/", json=payload)
        data = response.json

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Invalid input data")

# -------------------------------
# GET /api/v1/places/ — list
# -------------------------------
    def test_get_all_places(self):
        # Create a place first
        self.client.post("/api/v1/places/", json={
            "title": "Test House",
            "description": "Description",
            "price": 50.0,
            "latitude": 10.0,
            "longitude": 20.0,
            "owner_id": self.user_id,
            "amenities": []
        })

        response = self.client.get("/api/v1/places/")
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) >= 1)
        self.assertIn("id", data[0])
        self.assertEqual(data[0].get("title"), "Test House")

# -------------------------------
# GET /api/v1/places/<id> — single
# -------------------------------
    def test_get_place_by_id(self):
        # Create a place first
        response = self.client.post("/api/v1/places/", json={
            "title": "Single Place",
            "description": "Description",
            "price": 100.0,
            "latitude": 10.0,
            "longitude": 20.0,
            "owner_id": self.user_id,
            "amenities": []
        })
        place_id = response.json["id"]

        response = self.client.get("/api/v1/places/{}".format(place_id))
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("id"), place_id)
        self.assertEqual(data.get("title"), "Single Place")
        self.assertEqual(data.get("owner")["id"], self.user_id)

# -------------------------------
# PUT /api/v1/places/<id> — update
# -------------------------------
    def test_update_place_success(self):
        # Create a place first
        response = self.client.post("/api/v1/places/", json={
            "title": "Old Title",
            "description": "Old Desc",
            "price": 50.0,
            "latitude": 10.0,
            "longitude": 20.0,
            "owner_id": self.user_id,
            "amenities": []
        })
        place_id = response.json["id"]

        update_payload = {
            "title": "New Title",
            "description": "Updated Desc",
            "price": 200.0,
            "latitude": 15.0,
            "longitude": 25.0,
            "owner_id": self.user_id,
            "amenities": []
        }

        response = self.client.put("/api/v1/places/{}".format(place_id), json=update_payload)
        data = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("message"), "Place updated successfully")


if __name__ == "__main__":
    unittest.main(verbosity=2)