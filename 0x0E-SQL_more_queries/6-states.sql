--creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

--creates the table states
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
	);

