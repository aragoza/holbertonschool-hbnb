#!/usr/bin/env python3

from app.models.__init__ import BaseModel


class Amenity(BaseModel):
    """
    Docstring: Class Amenity
    """
    def __init__(self, name: str):
        """
        Methode __init__

        :param name: Name
        """
        super().__init__()
        self.name = name
