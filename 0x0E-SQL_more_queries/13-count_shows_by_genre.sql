--  lists all genres from hbtn_0d_tvshows and displays the number of shows
SELECT
	name,
	count(id) as number_of_shows
FROM
	tv_genres
LEFT JOIN
	tv_show_genres
ON
	id = genre_id
GROUP BY
	name
ORDER BY number_of_shows desc;
