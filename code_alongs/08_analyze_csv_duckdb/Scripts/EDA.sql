SELECT * FROM youtube;

SELECT DISTINCT(category) FROM youtube;

SELECT COUNT(*) FROM youtube; 

-- how many in each category top 10?
SELECT
	category,
	COUNT(*) AS Number
FROM
	youtube
GROUP BY
	category
ORDER BY
	number DESC
LIMIT 10;







