USE sakila;
SELECT *
FROM actor;


SELECT customer_id, SUM(amount) 
FROM payment
GROUP BY customer_id;

SELECT * FROM payment;

-- What is the average value of our purchases under $4.00?
SELECT ROUND(AVG(amount), 2) 
FROM payment WHERE amount < 4.00;

-- What is the highest amount paid between May 25, 2005 and June 15,2005?
SELECT MAX(amount) FROM payment WHERE payment_date BETWEEN '2005-05-25' AND '2005-06-15';


SELECT * FROM inventory;
USE northwind;

select * from orders;
SELECT count(*) FROM orders;

SELECT SUM(freight) AS total_freight FROM orders;
SELECT avg(freight) AS avg_freight FROM orders;
SELECT MIN(freight) AS Minimum_freight FROM orders;
SELECT MAX(freight) AS maximum_freight FROM orders;