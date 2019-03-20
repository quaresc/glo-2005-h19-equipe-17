CREATE DATABASE glo_2005;
use glo_2005;

CREATE TABLE users (
    id INT AUTO_INCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INT,
    PRIMARY KEY(id)
);

INSERT INTO users
    (first_name, last_name, age)
VALUES
    ('John', 'Do', 52),
    ('Bernard', 'Dupont', 31),
    ('Clara', 'Bergeron', 19);