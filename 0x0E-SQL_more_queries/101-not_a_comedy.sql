SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_genres
WHERE (SELECT tv_genres.name 
	FROM tv_genres
	WHERE name = Comedy
) IS NULL
