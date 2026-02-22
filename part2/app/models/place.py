#!/usr/bin/env python3

from __init__ import BaseModel
from amenity import Amenity
from review import Review
from user import User


class Place(BaseModel):
    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner: User):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review: Review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity: Amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
