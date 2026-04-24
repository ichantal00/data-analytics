USE northwind;

-- 1.Create a single query to list the product id, product name, unit price and category 
-- name of all products. Order by category name and within that, by product name.
SELECT productid, productname, unitprice, categoryID 
FROM products 
WHERE unitprice >75
ORDER BY categoryID, productname;

-- 2. Create a single query to list the product id, product name, unit price and supplier name 
-- of all products that cost more than $75. Order by product name.

SELECT productid, productname, unitprice, supplierid 
FROM products 
WHERE unitprice > 75 
ORDER By productname;

-- 3.Create a single query to list the product id, product name, unit price, category name, and 
-- supplier name of every product. Order by product name.

SELECT productID, Productname Unitprice, categoryID, supplierID
FROM products
ORDER BY productname;

-- 4.*Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company 
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to.

SELECT 
    o.OrderID,
    o.ShipName,
    o.ShipAddress,
    s.CompanyName AS ShippingCompany
FROM Orders o
JOIN Shippers s ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany';

-- 5. *Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, 
-- with a count of how many orders were shipped for that ship name.
SELECT 
    o.ShipName,
    o.ShipAddress,
    s.CompanyName AS Shipper
FROM Orders o
JOIN Shippers s ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany';

-- 6.*Create a single query to list the order id, order date, ship name, ship address of all orders 
-- that included Sasquatch Ale.

SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM Orders o
JOIN Orderdetails od ON 
o.OrderID = od.OrderID
JOIN Products p ON 
od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';