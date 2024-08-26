-- Script that creates a table users

CREATE TABLE IF NOT EXISTS users (
  id int NOT NULL AUTO_INCREMENT,
  email varchar(255) NOT NULL,
  name varchar(255),
  PRIMARY KEY (id),
  CONSTRAINT user_email UNIQUE(email)
);
