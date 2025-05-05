-- Select 20 Product IDs which are recorded the most number of times in the line_items table --
SELECT product_id, COUNT(*) AS occurrences
FROM line_items
GROUP BY product_id
ORDER BY occurrences DESC
LIMIT 20;