-- DDL query to create new table
CREATE TABLE IF NOT EXISTS second_table
(id INT,
	name VARCHAR(256),
	score INT);
-- insert first row into the table
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10);
-- insert second row into the table
INSERT INTO second_table (id, name, score)
VALUES (2, 'Alex', 3);
-- insert third row into the table
INSERT INTO second_table (id, name, score)
VALUES (3, 'Bob', 14);
-- insert forth row into the table
INSERT INTO second_table (id, name, score)
VALUES (4, 'George', 8);
