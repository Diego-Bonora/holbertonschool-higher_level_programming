-- Select with JOIN

SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = state_id.id;