-- Creo la base de datos si no existe
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Uso esa base de datos
USE hbtn_0d_usa;

-- Creo la tabla cities si no existe
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
