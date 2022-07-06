select * from "user"

--

select distinct topic from "post"

--

select * 
from "user"
where age > 30 and os = 'iOS'

--

select * 
from "user"
where country  != 'Russia' and ((exp_group not in (0,3)) or city = 'Minsk')

--

select country, avg(age) 
from "user"
where country = 'Cyprus'
group by country

--

select exp_group, os, count(id) as total_users, max(age) as max_age, min(age) as min_age
from "user"
group by exp_group, os 

--

select topic, MAX(CHAR_LENGTH(text))
from "post"
group by topic

--

select country, count(id) 
from "user"
group by country
having count(id) > 1000
order by count(id)

--

select exp_group, count(id) 
from "user"
where city = 'Moscow'
group by exp_group
having avg(age) > 27.2

--

select topic, count(id)
from "post"
group by topic
order by count(id) desc
limit 3

--

select *
from "user"
where city = 'Voronezh'
order by age desc, exp_group asc

--

select a.post_id, a.time, u.age, u.os
from feed_action as a
join "user" as u on a.user_id = u.id
where a.action = 'like' and u.city = 'Omsk'
order by a.time desc
limit 100

--

select city, count(a.action)
from "user" as u
join feed_action as a on a.user_id = u.id
join post as p on a.post_id = p.id 
where u.age = 36 and a.action = 'view' and date(a.time) = '2021-12-01' and p.topic = 'covid'
group by u.city
order by count(a.action)

--

select p.id, count(a.action), count(distinct u.id), max(a.time)
from feed_action as a
join post as p on a.post_id = p.id
join "user" as u on a.user_id = u.id
where a.action = 'like'
group by p.id
order by count(a.action) desc