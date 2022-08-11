-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT title, SUM(ratings.rate) AS rate
       FROM tv_shows AS shows
       	    INNER JOIN tv_show_ratings AS ratings
	    ON shows.id = ratings.show_id
	GROUP BY title
ORDER BY rate DESC;
