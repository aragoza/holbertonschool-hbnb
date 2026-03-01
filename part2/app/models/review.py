#!/usr/bin/env python3

from . import BaseModel

from .user import User
from .place import Place


class Review(BaseModel):
    def __init__(self, text: str, rating: int, place: Place, user: User):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
