CREATE TABLE IF NOT EXISTS users (
    id CHAR(36),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    is_admin BOOLEAN DEFAULT FALSE,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS places (
    id CHAR(36),
    title VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    latitude FLOAT,
    longitude FLOAT,
    user_id CHAR(36),
    PRIMARY KEY(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS review (
    id CHAR(36),
    text TEXT,
    rating INT(1, 5),
    user_id CHAR(36),
    place_id CHAR(36),
    PRIMARY KEY(id),
    CONSTRAINT there_s_place_and_user_id
    FOREIGN KEY (user_id) REFERENCES users(id)
    FOREIGN KEY (place_id) REFERENCES places(id)
);

CREATE TABLE IF NOT EXISTS amenities (
    id CHAR(36),
    name VARCHAR(255) UNIQUE
);

INSERT INTO users (
    `id`,
    `email`,
    `first_name`,
    `last_name`,
    `password`,
    `is_admin`
)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'admin@hbnb.com',
    'Admin',
    'HBnB',
    '$2a$12$iIY0XSc0TztcyhkfttsGtO/gUTorunCzu/YE8CpwxwD2wvHimahZ6',
    TRUE
);

INSERT INTO amenities (
    id,
    name
)
VALUES (
    '95a2224b-4b5c-40b3-a727-f32d309575fd',
    'Wifi'
);

INSERT INTO amenities (
    id,
    name
)
VALUES (
    '90db30b4-08b0-43bc-8cc8-c8148924653f',
    'Swimming Pool'
);

INSERT INTO amenities (
    id,
    name
)
VALUES (
    '462cf7f9-c53e-4bf6-bf96-3c990a5c78a4',
    'Air Conditioning'
);

INSERT INTO places (
    id,
    title,
    description,
    price,
    latitude,
    longitude,
    user_id,
    created_at,
    updated_at
)
VALUES (
    'd1c9e5b8-8c3a-4f08-9c1e-2b5a1f0e6c3a',
    'Cozy Cottage',
    'A cozy cottage in the countryside with beautiful views.',
    120.00,
    34.0522,
    -118.2437,
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    '2024-06-01 12:00:00',
    '2024-06-01 12:00:00'
);

INSERT INTO places (
    id,
    title,
    description,
    price,
    latitude,
    longitude,
    user_id,
    created_at,
    updated_at
)
VALUES (
    'a2b3c4d5-e6f7-8901-2345-67890abcdef1',
    'Modern Apartment',
    'A modern apartment in the city center with all amenities.',
    200.00,
    40.7128,
    -74.0060,
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    '2024-06-01 12:00:00',
    '2024-06-01 12:00:00'
);

INSERT INTO places (
    id,
    title,
    description,
    price,
    latitude,
    longitude,
    user_id,
    created_at,
    updated_at
)
VALUES (
    'f1e2d3c4-b5a6-7890-1234-56789abcdef2',
    'Beachfront Villa',
    'A luxurious beachfront villa with stunning ocean views.',
    350.00,
    25.7617,
    -80.1918,
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    '2024-06-01 12:00:00',
    '2024-06-01 12:00:00'
);
