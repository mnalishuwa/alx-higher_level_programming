-- displays the max temperature of each state
SELECT state, MAX(value) AS max_value FROM temperatures GROUP BY state ORDER BY state DESC;
