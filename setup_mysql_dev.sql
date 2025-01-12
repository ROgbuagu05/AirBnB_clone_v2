-- A script that prepares a MySQL server for the project
-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user if not exists
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant privileges to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
-- Flush privileges
FLUSH PRIVILEGES;
