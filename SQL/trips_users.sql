# Write your MySQL query statement below
select T.Request_at as Day,
round(sum(Status <> 'completed')/count(*),2) as 'Cancellation Rate'
from Trips T
inner join Users U1 on T.Client_Id = U1.Users_Id
inner join Users U2 on T.Driver_Id = U2.Users_Id
where Request_at >='2013-10-01' and  Request_at<='2013-10-03'
and U1.Banned <> 'Yes'
group by Request_at

