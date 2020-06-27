/*
Find the most common reaction for day 1

Find the most common reaction for day 1 by counting the number of occurrences for each reaction.

Output the reaction alongside its number of occurrences.

Order the result based on the number of occurrences in descending order.

Table: facebook_reactions
*/

select reaction, count(*) as count_val
from facebook_reactions
where date_day =1
group by reaction
order by count_val desc
limit 1;