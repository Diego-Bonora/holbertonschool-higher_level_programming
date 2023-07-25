-- Select with JOIN

SELECT cities.id, cities.name, states.name FROM cities RIGHT JOIN states ON cities.state_id = state_id.id;