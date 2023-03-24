CREATE SCHEMA service_it;
CREATE TABLE service_it.users (id SERIAL NOT NULL, full_name VARCHAR NOT NULL, login VARCHAR NOT NULL UNIQUE, password VARCHAR NOT NULL);
INSERT INTO service_it.users (full_name, login, password) VALUES ('Ivan Ivanov','Ivanov01', '123456'); 
