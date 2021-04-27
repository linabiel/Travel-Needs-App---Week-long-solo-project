DROP TABLE destinations;
DROP TABLE cities;
DROP TABLE countries;
DROP TABLE users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    home_city VARCHAR(255),
    home_country VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    visited BOOLEAN,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);
