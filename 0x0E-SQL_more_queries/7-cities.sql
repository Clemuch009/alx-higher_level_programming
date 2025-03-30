--creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

--creates the table cities
CREATE TABLE IF NOT EXISTS cities(
	id INT PRIMARY KEY AUTO_INTREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
