-- number of shows by genre
SELECT g.name AS genre, COUNT(n.genre_id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres n
ON g.id = n.genre_id
GROUP BY n.genre_id
ORDER BY number_of_shows DESC;
