with limit(lim) as
(
    select int(1000) from sysibm.sysdummy1
),
numbers(level1,num) as
(
    select 1, int(2) from sysibm.sysdummy1
    union all
    select level1 + 1, num + 1 from numbers
    where level1 < 999
)
select LISTAGG(n1.num,'&') from numbers n1
where not exists
(
    select n2.num from numbers n2
    where n1.num <> n2.num 
    and n2.num <= sqrt(n1.num)
    and mod(n1.num,n2.num) = 0
);