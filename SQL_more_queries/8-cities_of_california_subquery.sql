-- lists all cities from california

SELECT * FROM cities, states WHERE cities.state_id = states.id ORDER BY cities.id ASC;