-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT
	tv_genres.name,
	SUM(tv_show_ratings.rate) as rating
FROM
	tv_shows
LEFT JOIN
	tv_show_ratings
ON
	tv_shows.id = tv_show_ratings.show_id
LEFT JOIN
	tv_show_genres
ON
	tv_shows.id = tv_show_genres.show_id
LEFT JOIN
	tv_genres
ON
	tv_show_genres.genre_id = tv_genres.id
WHERE
	tv_genres.name IS NOT NULL
GROUP BY
	tv_genres.name
ORDER BY rating DESC;
