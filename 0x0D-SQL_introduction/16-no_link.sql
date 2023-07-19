-- DML query to list all records in DB, sorted by score and filter
SELECT score,name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
