CREATE TABLE IF NOT EXISTS marts.geography_summary_new AS 
(
    SELECT 
        Geografi AS country_code,
        SUM(Visningar) AS "Total visningar",
        100.0 * SUM(Visningar) / (SELECT SUM(Visningar) FROM geografi.diagramdata) AS percent_of_total
    FROM geografi.diagramdata
    GROUP BY Geografi
    ORDER BY "Total visningar" DESC
);

SELECT * 
FROM marts.geography_summary;

