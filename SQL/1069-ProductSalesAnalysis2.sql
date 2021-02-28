

-- Test1
/* Write your T-SQL query statement below */
select p.product_id,ISNULL(sum(S.quantity),0) as total_quantity
from Product P left join Sales S on S.product_id=p.product_id
group by p.product_id
-- brings all zero responses too 

--Test2
/* Write your T-SQL query statement below */
select product_id,sum(quantity) as total_quantity
from Sales
group by product_id 
-- Time limit exceeds