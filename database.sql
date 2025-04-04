DROP TABLE if exists urls CASCADE;
DROP TABLE if exists url_checks CASCADE;

CREATE TABLE urls(
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at DATE
);

CREATE TABLE url_checks(
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    url_id int REFERENCES urls (id) NOT NULL,
    status_code INT,
    h1 VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    created_at DATE
);