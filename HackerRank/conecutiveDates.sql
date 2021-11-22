--https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true
with temp1(hacker_id,submission_date,consecutiveDates) as (
    select hacker_id,submission_date,
       (
            submission_date - (row_number() over(partition by hacker_id order by submission_date)) days
        )
        from submissions
        where hacker_id in
        (
            select hacker_id from submissions
            where submission_date = '2016-03-01'
        )
        order by hacker_id
),
submissions_temp as (
    select submission_date,temp1.hacker_id,count(*) as submissions_in_a_day
    from temp1
    where consecutiveDates <= '2016-02-29'
    group by temp1.hacker_id,submission_date
    order by submission_date,submissions_in_a_day desc,hacker_id
),
temp2 as (select table1.submission_date,count1, min(hacker_id) as hacker_id from
-- hackers
(
    select submission_date,count(hacker_id) as count1,max(submissions_in_a_day) as maxsubs
    from submissions_temp
    group by submission_date
    
) as table1,
submissions_temp A
where table1.submission_date = A.submission_date
and A.submissions_in_a_day = maxsubs
group by table1.submission_date,count1
-- where table1.hacker_id = hackers.hacker_id
order by submission_Date)
select submission_date,count1,temp2.hacker_id,name
from temp2,hackers
where temp2.hacker_id = hackers.hacker_id
order by submission_date;

---
select 
submission_date ,

( SELECT COUNT(distinct hacker_id)  
 FROM Submissions s2  
 WHERE s2.submission_date = s1.submission_date AND    (SELECT COUNT(distinct s3.submission_date) FROM      Submissions s3 WHERE s3.hacker_id = s2.hacker_id AND s3.submission_date < s1.submission_date) = dateDIFF(s1.submission_date , '2016-03-01')) ,

(select hacker_id  from submissions s2 where s2.submission_date = s1.submission_date 
group by hacker_id order by count(submission_id) desc , hacker_id limit 1) as shit,
(select name from hackers where hacker_id = shit)
from 
(select distinct submission_date from submissions) s1
group by submission_date