SELECT states.name, cities.name, cities.id
FROM cities
INNER JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC
