#!/usr/bin/env python3

from app.models.baseclass import BaseModel
from app.api.exceptions import BadRequest
from app.models.amenity import Amenity
from sqlalchemy.orm import validates
from app.models.user import User
from app import db


class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner: User):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []
        self.add_place_to_owner()

    @validates("title")
    def validate_title(self, key: str, value: str):
        if not value or len(value.strip()) < 3 or len(value.strip()) > 100:
            raise BadRequest('Invalid input data')

        return value

    @validates("description")
    def validate_description(self, key: str, value: str):
        if not value or len(value) > 500:
            return ""

        return value

    @validates("price")
    def validate_price(self, key: str, value: str):
        if not type(value) in (int, float) or value < 0 or value > 1.0e12:
            raise BadRequest('Invalid input data')

        return value

    @validates("latitude")
    def validate_latitude(self, key: str, value: str):
        if not type(value) in (int, float) or value < -90 or value > 90:
            raise BadRequest('Invalid input data')

        return float(value)

    @validates("longitude")
    def validate_longitude(self, key: str, value: str):
        if not type(value) in (int, float) or value < -180 or value > 180:
            raise BadRequest('Invalid input data')

        return float(value)

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity: Amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_amenities(self, amenities: list[Amenity]):
        for amenity in amenities:
            self.add_amenity(amenity)

    def add_place_to_owner(self):
        self.owner.places_owned.append(self)
