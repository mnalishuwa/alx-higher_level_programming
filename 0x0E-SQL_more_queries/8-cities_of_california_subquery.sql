-- lists all the cities of California
SELECT id, name
FROM hbtn_0d_usa.cities
WHERE
	state_id in
	(
	SELECT id FROM hbtn_0d_usa.states WHERE name='California'
	);
