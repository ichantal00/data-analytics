-- Chantal Lee
-- April 20, 2026
-- SHOW DATABASES;
USE northwind;
SHOW TABLES;
SELECT ProductName, UnitPrice FROM Products;
SELECT * FROM Products;
-- SELECT column_name AS alias_name;
-- SELECT ProductName AS 'products', UnitPrice AS 'Price(USD)', FROM Products;
SELECT CompanyName, Country
FROM customers 
WHERE not Country = 'USA';
SELECT ProductName, Discontinued FROM products WHERE discontinued= 1;
-- SELECT  Country, CompanyName FROM customers WHERE supplier NOT in 'France' 