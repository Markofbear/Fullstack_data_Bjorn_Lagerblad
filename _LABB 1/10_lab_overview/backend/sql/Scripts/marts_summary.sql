CREATE TABLE marts.summary (
    Total_Visningar BIGINT,
    Total_Exponeringar BIGINT,
    Genomsnittlig_Klickfrekvens DOUBLE
);

INSERT INTO marts.summary
SELECT 
    SUM(Visningar) AS Total_Visningar,
    SUM(Exponeringar) AS Total_Exponeringar,
    AVG("Klickfrekvens för exponeringar (%)") AS Genomsnittlig_Klickfrekvens
FROM 
    youtube_data.innehall.tabelldata;

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

CREATE TABLE marts.exposure (
    Exponeringar BIGINT,
    Klickfrekvens DOUBLE
);

INSERT INTO marts.exposure
SELECT 
    Exponeringar, 
    "Klickfrekvens för exponeringar (%)"
FROM 
    youtube_data.innehall.tabelldata
WHERE 
    Exponeringar > 0;  
    
SELECT *
FROM youtube_data.innehall.tabelldata
LIMIT 5;