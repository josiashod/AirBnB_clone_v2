-- prepares a MySQL dev server for the AirBnb clone V2
-- creates a database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a user on the database hbnb_dev_db
CREATE USER 
    IF NOT EXISTS 'hbnb_dev'@'localhost' 
    IDENTIFIED BY 'hbnb_dev_pwd';

-- grant privileges on hbnb_dev_db
GRANT ALL PRIVILEGES
    ON `hbnb_dev_db`.*
    TO 'hbnb_dev'@'localhost'
    WITH GRANT OPTION;

-- grant SELECT privileges on the database performance_schema
GRANT SELECT
   ON `performance_schema`.*
   TO 'hbnb_dev'@'localhost';