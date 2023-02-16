-- creates database hbtn_0d_usa and table cities
-- cities description
-- id INT unique, auto generated, cant be null and is a primary key
-- state_id INT cant be null and must be a foreign key that reference id of states table
-- name VARCHAR cant be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256),
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES states(id)
);
