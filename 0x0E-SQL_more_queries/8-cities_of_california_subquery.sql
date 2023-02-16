-- lists all the cities of california that can be found in the databse hbtn_0d_usa
SELECT states.id, cities.name
FROM cities, states
WHERE states.name = 'california' and states.id = cities.state_id
ORDER BY cities.id;
