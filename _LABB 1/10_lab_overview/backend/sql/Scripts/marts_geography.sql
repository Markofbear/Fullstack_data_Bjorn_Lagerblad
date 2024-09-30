CREATE TABLE IF NOT EXISTS marts.geography_summary AS 
(
    SELECT 
        Geografi,
        SUM(Visningar) AS total_visningar,
        COUNT(*) AS total_rows,
        100.0 * SUM(Visningar) / (SELECT SUM(Visningar) FROM geografi.diagramdata) AS percent_of_total
    FROM geografi.diagramdata
    GROUP BY Geografi
    ORDER BY total_visningar DESC
);

ALTER TABLE marts.geography_summary RENAME COLUMN Geografi TO country_code;

SELECT * 
FROM marts.geography_summary;