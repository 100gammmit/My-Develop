DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS (
    userId varchar(255) Not NULL,
    password varchar(255) Not NULL,
    name varchar(255) Not NULL,
    email varchar(255),

    PRIMARY KEY (userId)
);