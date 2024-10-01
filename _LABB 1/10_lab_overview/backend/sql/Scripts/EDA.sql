WITH 
	date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
	STRFTIME('%Y-%m-%d', tot.datum), 
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM date_total as tot
LEFT JOIN date_table as tab 
ON tot.datum = tab.datum;



SELECT Enhetstyp, count(*) total_rows, sum(Visningar) as total_visningar 
from 
enhetstyp.diagramdata group by Enhetstyp ;

select * from enhetstyp.diagramdata d ;

SELECT * EXCLUDE (Innehåll) FROM  innehall.tabelldata ORDER BY "Visningstid (timmar)" DESC OFFSET 1 LIMIT 5;

SELECT * FROM  innehall.diagramdata;-- ORDER BY "Visningstid (timmar)";

SELECT STRFTIME('%Y-%m-%d', Datum), Visningar FROM innehall.totalt;


-- Snabb titt på enhetstyp
SELECT
    Enhetstyp,
    Visningar
FROM
    enhetstyp.diagramdata;

    
-- Sammanslagning av alla visningar till en kolumn (SUM)
SELECT
    Enhetstyp,
    SUM(Visningar) AS Summering_visningar
FROM
    enhetstyp.diagramdata
GROUP BY
    Enhetstyp 
ORDER BY
    Summering_visningar DESC;

   
-- Kollar över geografi data
SELECT * FROM geografi.diagramdata;

SELECT
	Geografi,
	SUM(Visningar)
FROM
	geografi.diagramdata
GROUP BY
	Geografi
ORDER BY
	SUM(Visningar);

-- Innehållstyp

SELECT * FROM innehallstyp.diagramdata;
 
-- Operativsystem
SELECT * FROM operativsystem.diagramdata;


-- Slutsats, Windows är bättre att kolla på youtube än Mac
SELECT
	Operativsystem,
	SUM(Visningar)
FROM
	operativsystem.diagramdata
GROUP BY
	Operativsystem
ORDER BY
	SUM(Visningar);

-- Gör en average på visningar genom enhetstyp
SELECT 
    Enhetstyp, 
    AVG(Visningar)
FROM 
    enhetstyp.diagramdata
GROUP BY 
    Enhetstyp
ORDER BY 
    AVG(Visningar) DESC;

 -- Summering av visningar
SELECT 
    Innehållstyp, 
    SUM(Visningar)
FROM 
    innehallstyp.diagramdata
GROUP BY 
    Innehållstyp
ORDER BY 
    SUM(Visningar) DESC;

-- EDA test och fördjupning
    
SELECT 
    Innehållstyp, 
    SUM(Visningar) AS total_visningar
FROM 
    innehallstyp.diagramdata
GROUP BY 
    Innehållstyp
ORDER BY 
    total_visningar DESC
LIMIT 5;

SELECT DISTINCT Innehållstyp 
FROM innehallstyp.diagramdata;

SELECT 
    STRFTIME('%Y-%m-%d', Datum) AS Date, 
    SUM(Visningar) AS total_visningar
FROM 
    innehall.totalt
GROUP BY 
    Date
ORDER BY 
    total_visningar DESC
LIMIT 5;

SELECT 
    Enhetstyp, 
    SUM(Visningar) AS total_visningar
FROM 
    enhetstyp.diagramdata
GROUP BY 
    Enhetstyp
ORDER BY 
    total_visningar DESC;
   
-- Exponering EDA

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

SELECT 
    SUM(Visningar) AS Total_Visningar,
    SUM(Exponeringar) AS Total_Exponeringar,
    AVG("Klickfrekvens för exponeringar (%)") AS Genomsnittlig_Klickfrekvens
FROM 
    youtube_data.innehall.tabelldata;
   
SELECT 
    Exponeringar, 
    "Klickfrekvens för exponeringar (%)"
FROM 
    youtube_data.innehall.tabelldata
WHERE 
    Exponeringar > 0;  
   





