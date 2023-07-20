-- DDL query to create a  MyQSL user with password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'
-- add a privileges to user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
