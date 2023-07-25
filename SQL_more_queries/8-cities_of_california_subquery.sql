-- lists all cities from california

SELECT * FROM cities,states WHERE states.id=cities.state_id ORDER BY cities.id DESC;