-- DML query to list number of same score in table
SELECT score,COUNT(*) AS 'number' FROM second_table
GROUP BY score
ORDER BY score DESC;
