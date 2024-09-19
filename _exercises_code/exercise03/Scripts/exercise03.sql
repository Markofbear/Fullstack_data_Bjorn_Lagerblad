SELECT opening_name, COUNT(*) AS count
FROM chess
GROUP BY opening_name
ORDER BY count DESC
LIMIT 10;
