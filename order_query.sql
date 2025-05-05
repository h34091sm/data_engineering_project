-- select top 10 orders in GBP --
SELECT * FROM orders WHERE currency = 'GBP' ORDER BY total DESC LIMIT 10; 