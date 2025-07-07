-- Lista todos los shows de genero Comedy
SELECT
    s.title
FROM
    tv_shows        AS s
    INNER JOIN tv_show_genres AS sg ON sg.show_id = s.id
    INNER JOIN tv_genres      AS g  ON g.id       = sg.genre_id
WHERE
    g.name = 'Comedy'
ORDER BY
    s.title ASC;
