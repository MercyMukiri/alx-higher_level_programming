-- A script that lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.

SELECT t.title, genres.name
       FROM tv_shows AS t
       	    LEFT JOIN tv_show_genres AS shows
	    ON t.id = shows.show_id

	    LEFT JOIN tv_genres AS genres
	    ON shows.genre_id = genres.id
ORDER BY t.title, genres.name;
