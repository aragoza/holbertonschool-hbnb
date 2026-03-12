#!/usr/bin/env python3

from app.models.baseclass import BaseModel
from app.api.exceptions import BadRequest
from app.models.place import Place, User
from sqlalchemy.orm import validates
from app import db


class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, text: str, rating: int, place: Place, user: User):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @validates("text")
    def validate_text(self, value: str):
        if len(value.strip()) < 8:
            raise BadRequest('Invalid input data')

        return value

    @validates("rating")
    def validate_rating(self, value: int):
        if value < 1 or value > 5:
            raise BadRequest('Invalid input data')

        return value
