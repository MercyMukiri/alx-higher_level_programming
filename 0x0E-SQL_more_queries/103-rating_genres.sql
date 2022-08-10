-- A script that lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating.

SELECT name, SUM(rate) AS rate
       FROM tv_genres AS genres
       	    INNER JOIN tv_show_genres AS shows
	    ON shows.genre_id = genres.id

	    INNER JOIN tv_show_ratings AS ratings
	    ON ratings.show_id = shows.show_id
	GROUP BY name
ORDER BY rating DESC;
