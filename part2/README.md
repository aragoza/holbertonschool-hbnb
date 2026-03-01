# HBNB part2

## Decription


## Business logic layer

1. **the architcture**
![alt text](<../part1/Diagramme de class.drawio.png>)

2. **pattern façade**
    **a little description of the use of the pattern façade**

It is used to be inherited by the other class models, and it implement general functionnalities to all the class

    - HBNBFacade
        - Attributes
            - id
            - created_at
            - updated_at
        - Methods
            - save()
            - update(data)

3. **models**
    - User
    - Place
    - Review
    - Amenity


## Presentation layer

1. **endpoints**
    - Users
        - POST /api/v1/users
        - Get /api/v1/users/{user_id}
    - Places
        - POST /api/v1/places
        - GET /api/v1/places
        - GET /api/v1/places/{place_id}
        - PUT /api/v1/places/{place_id}
    - Reviews
        - POST /api/v1/reviews
        - GET /api/v1/reviews
        - GET /api/v1/reviews/{review_id}
        - PUT /api/v1/reviews/{review_id}
        - DELETE /api/v1/reviews/{review_id}
    - Amenitys
        - POST /api/v1/amenities
        - GET /api/v1/amenities
        - GET /api/v1/amenities/{amenity_id}
        - PUT /api/v1/amenities/{amenity_id}


### doc swagger

```http://127.0.0.1:5000/api/v1```


## dependencies

1. **requirements.txt**

use the command : ```pip install -r requirments.txt```

2. **list of dependencies**
    - aniso8601==10.0.1
    - attrs==25.4.0
    - blinker==1.9.0
    - click==8.1.8
    - Flask==3.1.3
    - flask-restx==1.3.2
    - importlib_metadata==8.7.1
    - importlib_resources==6.5.2
    - itsdangerous==2.2.0
    - Jinja2==3.1.6
    - jsonschema==4.25.1
    - jsonschema-specifications==2025.9.1
    - MarkupSafe==3.0.3
    - referencing==0.36.2
    - rpds-py==0.27.1
    - typing_extensions==4.15.0
    - Werkzeug==3.1.6
    - zipp==3.23.0


## Authors

Contributors names and contact info

Name : email \n
Elliot CHARLET : _charlet.elliot@gmail.com_ \n
Ilan DEVERSENNE : _ilan.deversenne@holbertonstudents.com_ \n
Robin BOUVIER : _12229@holbertonstudents.com_ \n

## License

This project is licensed under the [ELLIOT CHARLET and ILAN DEVERSENNE and ROBIN BOUVIER] License