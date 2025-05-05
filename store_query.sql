-- Retreive the top 3 stores with the most occurrences in the stores table --
SELECT store_name, COUNT(*) AS occurrences
FROM stores
GROUP BY store_name
ORDER BY occurrences DESC
LIMIT 3;
