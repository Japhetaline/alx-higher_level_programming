-- lists all genres of the show Dexter
SELECT tv_genres.name AS genre,
-- COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.tv_genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
