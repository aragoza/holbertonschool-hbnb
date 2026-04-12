# HBNB part4

## Description
***The aim of this part is to construct the front end and implement some functionnalities for the front-end to discuss with the back-end***

## Presentation layer

### API
**endpoints**
    - Users
        - POST /api/v1/users
        - GET /api/v1/users
        - GET /api/v1/users/{user_id}
        - GET /api/v1/users/{user_id}
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

### Navigation
    - index.html (need a cookie token)
    - login.html (create a cookie token if login success)
    - add_review.html (need a cookie token)
    - place.html (need a cookie token and a place_id)

## Dependencies

1. **requirements.txt**

use the command : ```pip install -r requirments.txt```

2. **list of dependencies**
    - aniso8601==10.0.1
    - attrs==25.4.0
    - bcrypt==5.0.0
    - blinker==1.9.0
    - certifi==2026.2.25
    - charset-normalizer==3.4.4
    - click==8.1.8
    - Faker==37.12.0
    - Flask==3.1.3
    - Flask-Bcrypt==1.0.1
    - flask-jwt-extended
    - flask-restx==1.3.2
    - Flask-SQLAlchemy==3.1.1
    - greenlet==3.2.5
    - idna==3.11
    - importlib_metadata==8.7.1
    - importlib_resources==6.5.2
    - itsdangerous==2.2.0
    - Jinja2==3.1.6
    - jsonschema==4.25.1
    - jsonschema-specifications==2025.9.1
    - MarkupSafe==3.0.3
    - referencing==0.36.2
    - requests==2.32.5
    - rpds-py==0.27.1
    - SQLAlchemy==2.0.48
    - typing_extensions==4.15.0
    - tzdata==2025.3
    - urllib3==2.6.3
    - Werkzeug==3.1.6
    - zipp==3.23.0

## To test the app front-end

1. First run the server
***first create the database***
```
flask shell
db.create_all()
```
***then create the necessary element***
```
run the part you need in the file ***create_data_in_db.sql***
```
***then launch the server***
```
execute the ***./run.py***
```
***and last***
```
forward a port to test locally the app front-end
```

2. Test the front
-Login with :
    - email: admin@hbnb.com
    - password: admin1234

-Click on View Details button
-Click on the Add_Review in the navigation
-Send a response and submit
-Come back home