DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS light_bulb;
DROP TABLE IF EXISTS current_consumption;

CREATE TABLE users (
    name TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    country FLOAT NOT NULL
);

CREATE TABLE light (
    id_lb INTEGER PRIMARY KEY AUTOINCREMENT,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    color CHAR NOT NULL,
    light_level REAL NOT NULL
);

CREATE TABLE current_usage (
    id_cc INTEGER PRIMARY KEY AUTOINCREMENT,
    data TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    kw FLOAT NOT NULL
);

CREATE TABLE weather (
    id_w INTEGER PRIMARY KEY AUTOINCREMENT,
    time1 TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    meteo CHAR NOT NULL
);

CREATE TABLE routine (
    id_r INTEGER PRIMARY KEY AUTOINCREMENT,
    time1 TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    start TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    color CHAR NOT NULL,
    light_level REAL NOT NULL
);