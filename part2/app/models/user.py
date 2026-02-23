#!/usr/bin/env python3

from . import BaseModel


class User(BaseModel):
    """
    Docstring for User
    """
    # we will have to import an email validator (maybe regex)
    def __init__(self, first_name: str, last_name: str, email, is_admin=False):
        """
        Docstring for __init__

        :param self: instance of the class
        :param first_name: e.g Elliot
        :param last_name: e.g CHARLET
        :param email: email that respect the email validator
        :param is_admin: bool that is set to false by default
        """
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
