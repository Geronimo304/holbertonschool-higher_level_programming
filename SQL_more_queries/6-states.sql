-- creo la base de datos
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- usa la base de datos
USE hbtn_0d_usa;

-- creo la tabla state si no existe
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);