select m.*, x.numoft, y.numoft from (
select xwallet, ywallet, count(*) as num from (
select x.wallet as xwallet, x.AmountBTC as x1, y.wallet as ywallet, y.AmountBTC as y1, x.time as x2, y.time as y2 from all_transactions x 
join all_transactions y on  CAST(x.time as date) = CAST(y.time as date) and DATEDIFF(minute, x.time, y.time)<2 and DATEDIFF(minute, x.time, y.time)>-2  
--(x.AmountBTC >= y.AmountBTC and x.AmountBTC*0.9 <= y.AmountBTC ) or (y.AmountBTC >= x.AmountBTC and y.AmountBTC*0.9 <= x.AmountBTC ) 
where x.wallet != y.wallet and ((x.AmountBTC>0 and y.AmountBTC>0) or (x.AmountBTC<0 and y.AmountBTC<0)) ) q
group by xwallet, ywallet ) m
--order by num desc  
JOIN (
select wallet, count(*) as numoft from all_transactions
group by wallet ) x on x.wallet = m.xwallet 
JOIN (
select wallet, count(*) as numoft from all_transactions
group by wallet  ) y on y.wallet = m.ywallet
where  num>2 and ((x.numoft+y.numoft)-2*num)/coalesce(num, 1)<=5
order by num desc
