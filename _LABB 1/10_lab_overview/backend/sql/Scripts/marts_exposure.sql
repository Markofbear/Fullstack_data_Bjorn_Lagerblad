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