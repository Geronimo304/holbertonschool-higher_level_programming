-- Crea la base de datos si no existe
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crea el usuario user_0d_2 si no existe, con contraseña
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Da permiso de solo lectura (SELECT) sobre esa base de datos
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
