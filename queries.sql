-- Table structure
-- transactions(
--     user_id INT,
--     amount INT,
--     transaction_date DATE
-- )

-- Total amount per user for transactions in 2024 only
SELECT
    user_id,
    SUM(amount) AS total_amount
FROM transactions
WHERE YEAR(transaction_date) = 2024
GROUP BY user_id
ORDER BY user_id;




-- find top 5 customers by total spending
SELECT customer_id, SUM(amount) as total
FROM transactions
GROUP BY customer_id
ORDER BY total DESC
LIMIT 5;
