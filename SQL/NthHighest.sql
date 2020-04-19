SELECT salary, rank() over (order by salary desc)
from Employee
where Rank = N