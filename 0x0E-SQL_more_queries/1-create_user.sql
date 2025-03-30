--creates the MySQL server user user_0d_1.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WITH  BY 'user_0d_1_pwd';
GRANT SELECT ALL ON *.* TO 'user_0d_1'@;'localhost';
