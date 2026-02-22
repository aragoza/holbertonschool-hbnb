#!/usr/bin/env python3

from __init__ import BaseModel
from place import Place
from user import User


class Review(BaseModel):
    def __init__(self, text: str, rating: int, place: Place, user: User):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
