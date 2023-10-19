-- displays the max temperature of each state
WITH temprank AS
     (SELECT *,
     	     RANK()
	     OVER(PARTITION BY state ORDER BY value DESC)
	     AS ranks
     FROM
	hbtn_0c_0.temperatures)

SELECT DISTINCT
       state,
       value
FROM
	temprank
WHERE
	ranks=1
ORDER BY state;
