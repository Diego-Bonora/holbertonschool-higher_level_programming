-- lists all cities from california

SELECT * FROM cities WHERE (SELECT id FROM states WHERE name = "California") = state_id ORDER BY id ASC;