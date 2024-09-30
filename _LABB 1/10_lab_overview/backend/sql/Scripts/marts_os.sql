CREATE TABLE IF NOT EXISTS marts.os AS 
(
    SELECT 
        Operativsystem,
        SUM(Visningar) AS sum_visningar,
        AVG(Visningar) AS avg_visningar,
        COUNT(*) AS total_rows,
        100.0 * SUM(Visningar) / (SELECT SUM(Visningar) FROM operativsystem.diagramdata) AS percent_of_total
    FROM operativsystem.diagramdata
    GROUP BY Operativsystem
    ORDER BY sum_visningar DESC
);

ALTER TABLE marts.os RENAME COLUMN total_visningar TO sum_visningar;

SELECT * 
FROM marts.os;
