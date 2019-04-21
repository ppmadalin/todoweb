CREATE DATABASE IF NOT EXISTS todoweb;

CREATE USER IF NOT EXISTS 'todoapp'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON todoweb.* TO 'todoapp'@'localhost';

