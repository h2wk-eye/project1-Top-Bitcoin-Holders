select * from (
SELECT xwallet, ywallet, avg(x1) as avgx1, avg(y1) avgy1, count(*) as num from (
select x.wallet as xwallet, x.AmountBTC as x1, y.wallet as ywallet, y.AmountBTC as y1, x.time as x2, y.time as y2 from all_transactions x 
join all_transactions y on  -x.AmountBTC >= y.AmountBTC and -x.AmountBTC*0.99 < y.AmountBTC 
where x.wallet != y.wallet and CAST(x.time as date) = CAST(y.time as date) and DATEDIFF(minute, x.time, y.time)=0  and x.AmountBTC<0
and x.AmountBTC<-0.1 and x.wallet not in ( select wallet from not_counting) and y.wallet not in (select wallet from not_counting)
) q
group by xwallet, ywallet
) q2 
-- where num >=3  
order by num desc