#!/usr/bin/env python3

from random import random
from faker import Faker
from sys import exit
import requests


class Client:
    api = 'http://localhost:5000/api/v1'

    def register(self, first_name: str, last_name: str, email: str, password: str):
        req = requests.post(f'{self.api}/users', json={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password
        })

        if req.status_code != 201:
            print(req.status_code)
            print(req.text)
            raise ValueError("[ REGISTER ] HTTP CODE != 201")

        user = req.json()
        user['password'] = password

        i = ''.join(f"{key.replace('_', ' ').capitalize()}: {val}\n" for key, val in user.items())
        print(f'''
-------------------- NEW ACCOUNT --------------------
{i}
-----------------------------------------------------\n
        ''')

        return user

    def login(self, email: str, password: str):
        req = requests.post(f'{self.api}/login', json={
            'email': email,
            'password': password
        })

        if req.status_code != 200:
            print(req.status_code)
            print(req.text)
            raise ValueError("[ LOGIN ] HTTP CODE != 200")

        jwt = req.json()
        self.JWT = jwt.get('access_token', '')

        i = ''.join(f"{key.replace('_', ' ').capitalize()}: {val}\n" for key, val in jwt.items())
        print(f'''
-------------------- LOGIN (JWT) --------------------
{i}
---------------------------------------------------\n
        ''')

        return jwt

    def create_place(self, title: str, description: str, price: float, lat: float, lon: float, owner: str, amenities: list):
        try:
            self.JWT
        except NameError:
            raise ValueError("No JWT, please login before create place")

        req = requests.post(f'{self.api}/places', headers={
            'Authorization': f'Bearer {self.JWT}'
        }, json={
            'title': title,
            'description': description,
            'price': price,
            'latitude': lat,
            'longitude': lon,
            'owner_id': owner,
            'amenities': amenities
        })

        if req.status_code != 201:
            print(req.status_code)
            print(req.text)
            raise ValueError("[ CREATE PLACE ] HTTP CODE != 201")

        place = req.json()

        i = ''.join(f"{key.replace('_', ' ').capitalize()}: {val}\n" for key, val in user.items())
        print(f'''
-------------------- NEW PLACE --------------------
{i}
---------------------------------------------------\n
        ''')

        return place


client = Client()
faker = Faker()


try:
    user = client.register(faker.first_name(), faker.last_name(), faker.email(), faker.password())
except Exception as e:
    print(e)

try:
    user
except NameError:
    print("\nFAILED TO REGISTER USER :'(")
    exit(0)

try:
    jwt = client.login(user.get('email', ''), user.get('password', ''))
except Exception as e:
    print(e)

try:
    jwt
except NameError:
    print("\nFAILED TO LOGIN :'(")
    exit(0)

faker = Faker()

try:
    place = client.create_place(
        faker.company(),
        'My good place',
        random(),
        random(),
        random(),
        user.get('id', ''),
        []
    )
except Exception as e:
    print(e)

try:
    place
except NameError:
    print("\nFAILED TO CREATE PLACE :'(")
    exit(0)
