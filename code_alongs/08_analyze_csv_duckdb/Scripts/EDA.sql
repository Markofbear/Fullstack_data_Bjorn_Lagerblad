SELECT * FROM youtube;

SELECT DISTINCT(category) FROM youtube;

SELECT count(*) FROM youtube;

	-- how many in each category

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
