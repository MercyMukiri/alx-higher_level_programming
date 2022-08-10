-- A script that lists all shows without the genre Comedy
-- in the database hbtn_0d_tvshows.

SELECT DISTINCT title
       FROM tv_shows AS t
       	    LEFT JOIN tv_show_genres AS shows
	    ON t.id = shows.show_id

	    LEFT JOIN tv_genres AS genres
       	    ON genres.id = shows.genre_id
      WHERE t.title NOT IN
	    	  (SELECT title
		  	  FROM tv_shows AS t
			       INNER JOIN tv_show_genres AS shows
			       ON shows.show_id = t.id

			       INNER JOIN tv_genres AS genres
			       ON genres.id = shows.genre_id
			       WHERE genres.name = "comedy")
ORDER BY title;
