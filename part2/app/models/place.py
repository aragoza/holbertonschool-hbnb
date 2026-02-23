#!/usr/bin/env python3

from app.models.__init__ import BaseModel

from app.models.amenity import Amenity
from app.models.user import User


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

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity: Amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

# to add a place to the list of the user place owned
    def add_place_to_owner(self):
        """
        Docstring for add_place

        :param self: Description
        """
        self.owner.places_owned.append(self)
