
-- This SQL query retrieves the top 10 customers who have spent the most money on orders. -- 
SELECT reference, customer_name, SUM(order_total) AS total_spent
FROM customers
GROUP BY reference, customer_name
ORDER BY total_spent DESC
LIMIT 10;

