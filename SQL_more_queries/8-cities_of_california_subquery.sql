-- lists all cities from california

SELECT * FROM cities WHERE states.id = cities.state_id ORDER BY id DESC;