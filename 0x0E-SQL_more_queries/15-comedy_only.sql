-- A script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT t.title
       FROM tv_shows AS t
       	    INNER JOIN tv_show_genres AS shows
	    ON t.id = shows.show_id

	    INNER JOIN tv_genres AS genres
       	    ON genres.id = shows.genre_id
      WHERE genres.name = "Comedy"
ORDER BY t.title;
