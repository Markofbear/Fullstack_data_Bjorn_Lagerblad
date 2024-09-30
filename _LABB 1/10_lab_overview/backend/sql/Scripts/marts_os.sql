CREATE TABLE IF NOT EXISTS marts.os AS 
(
    SELECT 
        Operativsystem,
        SUM(Visningar) AS "Genomsnitt visningar",
        AVG(Visningar) AS "Genomsnittliga visningar",
        100.0 * SUM(Visningar) / (SELECT SUM(Visningar) FROM operativsystem.diagramdata) AS "Procent av totalt"
    FROM operativsystem.diagramdata
    GROUP BY Operativsystem
    ORDER BY SUM(Visningar) DESC
);

DROP TABLE IF EXISTS marts.os;

SELECT * 
FROM marts.os;
