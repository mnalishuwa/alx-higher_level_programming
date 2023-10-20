-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT
	title,
	genre_id
FROM
	tv_shows
LEFT JOIN
	tv_show_genres
ON
	id = show_id
WHERE
	genre_id IS NOT NULL
ORDER BY title, genre_id;
