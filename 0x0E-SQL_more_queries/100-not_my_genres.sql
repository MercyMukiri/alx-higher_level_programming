-- A script that uses the hbtn_0d_tvshows database
-- to list all genres not linked to the show Dexter

SELECT DISTINCT name
       FROM tv_genres AS genres
       	    INNER JOIN tv_show_genres AS shows
	    ON genres.id = shows.genre_id

	    INNER JOIN tv_shows AS t
	    ON t.id = shows.show_id
      WHERE genres.name NOT IN
       	     (SELECT name
	     	     FROM tv_genres AS genres
		     	  INNER JOIN tv_show_genres AS shows
			  ON genres.id = shows.genre_id

			  INNER JOIN tv_shows AS t
			  ON shows.show_id = t.id
			  WHERE t.title = "Dexter")
ORDER BY genres.name;
