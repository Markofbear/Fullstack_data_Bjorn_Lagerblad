CREATE TABLE marts.top_5 (
    Videotitel VARCHAR,
    Publiceringstid VARCHAR,
    Visningar BIGINT,
    Visningstid DOUBLE,
    Prenumeranter BIGINT,
    Exponeringar BIGINT,
    Klickfrekvens DOUBLE
);

INSERT INTO marts.top_5
SELECT 
    Videotitel, 
    "Publiceringstid för video" AS Publiceringstid,
    Visningar, 
    "Visningstid (timmar)" AS Visningstid, 
    Prenumeranter, 
    Exponeringar, 
    "Klickfrekvens för exponeringar (%)"
FROM 
    youtube_data.innehall.tabelldata
ORDER BY 
    Exponeringar DESC 
LIMIT 5;