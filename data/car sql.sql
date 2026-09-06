CREATE DATABASE car_market_analysis;
USE car_market_analysis;
CREATE TABLE cars (
    car_name VARCHAR(150),
    brand VARCHAR(50),
    model VARCHAR(100),
    vehicle_age INT,
    km_driven INT,
    seller_type VARCHAR(50),
    fuel_type VARCHAR(50),
    transmission_type VARCHAR(50),
    mileage DECIMAL(10,2),
    engine DECIMAL(10,2),
    max_power DECIMAL(10,2),
    seats INT,
    selling_price DECIMAL(12,2)
);
USE car_market_analysis;

SELECT COUNT(*) AS total_cars
FROM cars;

select * from cars limit 5;

#How many cars are there for each brand?
select brand,count(*) as total_cars from cars
group by brand
order by total_cars desc;

#Question 2 — Average Selling Price by Brand
select brand,avg(selling_price) as average_price
from cars
group by brand
order by average_price desc;

#Question 3 — Top 10 Most Expensive Cars
select brand,car_name,model,selling_price
from cars
order by selling_price desc
limit 10;

#Question 4 — Average Selling Price by Fuel Type
select fuel_type,avg(selling_price) as average_selling_price
from cars
group by fuel_type
order by average_selling_price desc;

#Question 5 — Average Selling Price by Transmission
select transmission_type,avg(selling_price) as average_selling_price
from cars
group by transmission_type
order by average_selling_price desc;

#Question 6 — Average Selling Price by Vehicle Age
select vehicle_age,avg(selling_price) as average_sellingprice
from cars
group by vehicle_age
order by vehicle_age; 

#7 — Using HAVING
#Which car brands have more than 1,000 cars in the dataset?
select brand,count(*) as total_cars
from cars 
group by brand
having count(*) >1000
order by total_cars desc;

#Which car brands have an average selling price greater than ₹5,00,000?
select brand,avg(selling_price) as average_price
from cars
group by brand
having avg(selling_price) > 500000
order by average_price desc;

#Find all cars whose selling price is higher than the average selling price of all cars.
select car_name,brand,model,selling_price
from cars 
where selling_price >(select avg(selling_price) from cars) 
order by selling_price desc;

#Which brands have an average selling price higher than the overall average selling price of all cars?
select brand,avg(selling_price) as average_price
from cars
group by brand
having avg(selling_price) >(select avg(selling_price) from cars)
order by average_price desc;

#Find the most expensive car for each brand.
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

#Divide cars into Budget, Mid-Range, and Premium based on selling price.
select car_name,brand,selling_price,
case
  when selling_price < 300000 then 'budget'
  when selling_price <= 700000 then 'mid-range'
  else 'premimum'
end as price_category
from cars;

#How many cars are Budget, Mid-Range, and Premium?
select 
case
when selling_price < 300000 then 'budget'
when selling_price <= 700000 then 'mid-range'
else 'premimum'
end as price_category,
count(*) as total_cars
from cars
group by price_category
order by total_cars desc;

#Rank cars by selling price from highest to lowest.
select car_name,brand,model,selling_price,
row_number()
over(order by selling_price desc) as price_rank
from cars ;

#Rank cars according to their selling price.
select car_name,brand,selling_price,rank()
over(order by selling_price desc) as price_rank
from cars;

#Find the most expensive cars within each brand and rank them.
select car_name,brand,model,selling_price,row_number()
over(partition by brand order by selling_price desc) as brand_rank
from cars;