USE northwind;
-- Write a query to list the product id, product name, and unit price of every product that Northwind sells. 
-- (Hint: To help set up your query, look at the schema preview to see what column names belong to each table. 
-- Or use SELECT * to query all columns first, then refine your query to just the columns you want.)
SELECT Unitprice, productid, productname FROM products;


SELECT productName, unitPrice
FROM products
WHERE unitprice <= 7.50;

SELECT *
FROM products
WHERE unitsinstock = 0
AND unitsonorder >= 1;
-- unit type categoryid 4
-- list of categories in field types

SELECT 
