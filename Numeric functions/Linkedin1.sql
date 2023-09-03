-- Get the count of values in a column
SELECT count(OrderID),count(ProductID),count(Product), count(Quantity),count(UnitPrice), count(Discount) FROM sales_data.sales;
-- Get the sum of values in a numeric column
SELECT sum(Quantity),sum(UnitPrice), sum(Discount) FROM sales_data.sales;
-- Get the maximum values in a numeric column
SELECT max(Quantity),max(UnitPrice), max(Discount) FROM sales_data.sales;
-- Get the minimum values in a numeric column
SELECT min(Quantity),min(UnitPrice), min(Discount) FROM sales_data.sales;
-- Get the average values in a numeric column
SELECT avg(Quantity),avg(UnitPrice), avg(Discount) FROM sales_data.sales;
