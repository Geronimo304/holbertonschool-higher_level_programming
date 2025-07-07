-- Lista cada genero de tv con su numero total de shows
SELECT
    g.name AS genre,
    COUNT(sg.show_id) AS number_of_shows
FROM
    tv_genres AS g
    INNER JOIN tv_show_genres AS sg ON sg.genre_id = g.id
GROUP BY
    g.id
ORDER BY
    number_of_shows DESC;
