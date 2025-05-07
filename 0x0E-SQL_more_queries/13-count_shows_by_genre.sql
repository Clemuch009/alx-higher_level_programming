-- lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_genres.name
