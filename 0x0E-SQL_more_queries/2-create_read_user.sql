-- creates the database hbtn_0d_2 and the user user_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if they don't exist and set the password
CREATE USER IF NOT EXISTS'user_0d_2'@'localhost' INDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
