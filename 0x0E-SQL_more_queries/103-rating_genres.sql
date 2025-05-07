SELECT tv_genres.name, SUM(rate) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_ratings 
ON 
GROUP BY rating_sum DESC,
