CREATE DATABASE IF NOT EXISTS demo_securite_BD_quantic;
USE demo_securite_BD_quantic;

-- Création de la table 'users' dans la base classique
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);
select * from users;
