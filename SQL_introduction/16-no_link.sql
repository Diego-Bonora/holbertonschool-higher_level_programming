-- Lists all from a table that has columng name not null

SELECT score,name FROM second_table WHERE name is not null ORDER BY score DESC;