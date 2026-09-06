USE car_market_analysis;

-- Q1. Count cars by brand
SELECT
    brand,
    COUNT(*) AS total_cars
FROM cars
GROUP BY brand
ORDER BY total_cars DESC;


-- Q2. Average selling price by brand
SELECT
    brand,
    AVG(selling_price) AS average_price
FROM cars
GROUP BY brand
ORDER BY average_price DESC;


-- Q3. Top 10 most expensive cars
SELECT
    car_name,
    brand,
    model,
    selling_price
FROM cars
ORDER BY selling_price DESC
LIMIT 10;


-- Q4. Average selling price by fuel type
SELECT
    fuel_type,
    AVG(selling_price) AS average_price
FROM cars
GROUP BY fuel_type
ORDER BY average_price DESC;


-- Q5. Average selling price by transmission type
SELECT
    transmission_type,
    AVG(selling_price) AS average_price
FROM cars
GROUP BY transmission_type
ORDER BY average_price DESC;


-- Q6. Average selling price by vehicle age
SELECT
    vehicle_age,
    AVG(selling_price) AS average_price
FROM cars
GROUP BY vehicle_age
ORDER BY vehicle_age;


-- Q7. Brands having more than 1000 cars
SELECT
    brand,
    COUNT(*) AS total_cars
FROM cars
GROUP BY brand
HAVING COUNT(*) > 1000
ORDER BY total_cars DESC;


-- Q8. Brands with average price above ₹5,00,000
SELECT
    brand,
    AVG(selling_price) AS average_price
FROM cars
GROUP BY brand
HAVING AVG(selling_price) > 500000
ORDER BY average_price DESC;


-- Q9. Cars above the overall average selling price
SELECT
    car_name,
    brand,
    model,
    selling_price
FROM cars
WHERE selling_price > (
    SELECT AVG(selling_price)
    FROM cars
)
ORDER BY selling_price DESC;


-- Q10. Brands above the overall average price
SELECT
    brand,
    AVG(selling_price) AS average_price
FROM cars
GROUP BY brand
HAVING AVG(selling_price) > (
    SELECT AVG(selling_price)
    FROM cars
)
ORDER BY average_price DESC;


-- Q11. Most expensive car for each brand
SELECT
    c.car_name,
    c.brand,
    c.model,
    c.selling_price
FROM cars c
JOIN (
    SELECT
        brand,
        MAX(selling_price) AS max_price
    FROM cars
    GROUP BY brand
) m
ON c.brand = m.brand
AND c.selling_price = m.max_price
ORDER BY c.brand;


-- Q12. Categorize cars by selling price
SELECT
    car_name,
    brand,
    selling_price,
    CASE
        WHEN selling_price < 300000 THEN 'Budget'
        WHEN selling_price <= 700000 THEN 'Mid-Range'
        ELSE 'Premium'
    END AS price_category
FROM cars;


-- Q13. Count cars by price category
SELECT
    CASE
        WHEN selling_price < 300000 THEN 'Budget'
        WHEN selling_price <= 700000 THEN 'Mid-Range'
        ELSE 'Premium'
    END AS price_category,
    COUNT(*) AS total_cars
FROM cars
GROUP BY price_category
ORDER BY total_cars DESC;


-- Q14. Rank all cars by selling price
SELECT
    car_name,
    brand,
    model,
    selling_price,
    ROW_NUMBER() OVER (
        ORDER BY selling_price DESC
    ) AS price_rank
FROM cars;


-- Q15. Rank cars within each brand
SELECT
    car_name,
    brand,
    model,
    selling_price,
    ROW_NUMBER() OVER (
        PARTITION BY brand
        ORDER BY selling_price DESC
    ) AS brand_rank
FROM cars;


-- Q16. Most expensive car from each brand using ROW_NUMBER
SELECT *
FROM (
    SELECT
        car_name,
        brand,
        model,
        selling_price,
        ROW_NUMBER() OVER (
            PARTITION BY brand
            ORDER BY selling_price DESC
        ) AS brand_rank
    FROM cars
) ranked_cars
WHERE brand_rank = 1;