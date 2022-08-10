-- A script that uses the hbtn_0d_tvshows database
-- to lists all genres of the show Dexter.

SELECT genres.name
       FROM tv_genres AS genres
       	    INNER JOIN tv_show_genres AS shows
	    ON genres.id = shows.genre_id

	    INNER JOIN tv_shows AS t
	    ON t.id = shows.show_id
      WHERE t.title = "Dexter"
ORDER BY genres.name;
