WITH  basePOS1  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2020-12-10' and '2021-01-11'),
baseNEG1 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2020-12-10' and '2021-01-11'),
basePOS2  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-01-11' and '2021-01-23'),
baseNEG2 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-01-11' and '2021-01-23'),
basePOS3  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-01-27' and '2021-02-23'),
baseNEG3 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-01-27' and '2021-02-23'),
basePOS4 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-02-23' and '2021-03-02'),
baseNEG4 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-02-23' and '2021-03-02'),
basePOS5  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-03-02' and '2021-03-15'),
baseNEG5 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-03-02' and '2021-03-15'),
basePOS6 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-03-15' and '2021-03-27'),
baseNEG6 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-03-15' and '2021-03-27'),
basePOS7  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-05-08' and '2021-05-20'),
baseNEG7 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-05-08' and '2021-05-20'), 
basePOS8  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-09-28' and '2021-10-22'),
baseNEG8 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-09-28' and '2021-10-22'),
basePOS9  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-11-07' and '2021-12-07'),
baseNEG9 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-11-07' and '2021-12-07'),
basePOS10  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2021-12-24' and '2022-01-24'),
baseNEG10 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2021-12-24' and '2022-01-24'),
basePOS11  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2022-05-03' and '2022-05-15'),
baseNEG11 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2022-05-03' and '2022-05-15'),
basePOS12  AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'Y' and time between '2022-06-06' and '2022-06-20'),
baseNEG12 AS
( SELECT * from (
SELECT *, CASE WHEN AmountBTC>0 THEN 'Y' ELSE 'N' END as direction  from all_transactions ) q 
where direction = 'N' and time between '2022-06-06' and '2022-06-20')

SELECT * FROM (
SELECT rnk1+rnk2+rnk3+rnk4+rnk5+rnk6+rnk7+rnk8+rnk9+rnk10+rnk11+rnk12+rnk13+rnk14+rnk15+rnk16+rnk17+rnk18+rnk19+rnk20+rnk21+rnk22+rnk23+rnk24 as score_yep ,* FROM (
SELECT o.Wallet, COALESCE(rnk1, 0) as rnk1, COALESCE(rnk2,0) as rnk2 , COALESCE(rnk3,0) as rnk3, COALESCE(rnk4, 0) as rnk4, COALESCE(rnk5,0) as rnk5 , COALESCE(rnk6,0) as rnk6, COALESCE(rnk7, 0) as rnk7, COALESCE(rnk8,0) as rnk8 , COALESCE(rnk9,0) as rnk9, COALESCE(rnk10, 0) as rnk10, COALESCE(rnk11,0) as rnk11 , COALESCE(rnk12,0) as rnk12, 
COALESCE(rnk13, 0) as rnk13, COALESCE(rnk14,0) as rnk14 , COALESCE(rnk15,0) as rnk15, COALESCE(rnk16, 0) as rnk16, COALESCE(rnk17,0) as rnk17 , COALESCE(rnk18,0) as rnk18, COALESCE(rnk19, 0) as rnk19, COALESCE(rnk20,0) as rnk20 , COALESCE(rnk21,0) as rnk21, COALESCE(rnk22, 0) as rnk22, COALESCE(rnk23,0) as rnk23 , COALESCE(rnk24,0) as rnk24 from 
(SELECT DISTINCT wallet from all_transactions) o

FULL JOIN( 
select wallet, RANK() OVER(order by minprice1 DESC) as rnk1 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS1 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS1 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P1 ON o.wallet = P1.wallet

FULL JOIN(
select wallet, RANK() OVER(order by minprice1) as rnk2 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG1 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG1 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N1 ON o.Wallet = N1.Wallet 


FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk3 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS2
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS2 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P2 ON o.Wallet = P2.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk4 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG2
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG2 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N2 ON o.Wallet = N2.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk5 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS3 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS3 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P3 ON o.Wallet = P3.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk6 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG3
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG3 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N3 ON o.Wallet = N3.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk7 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS4 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS4 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P4 ON o.Wallet = P4.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk8 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG4
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG4 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N4 ON o.Wallet = N4.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk9 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS5 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS5 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P5 ON o.Wallet = P5.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk10 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG5 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG5 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N5 ON o.Wallet = N5.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk11 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS6
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS6 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P6 ON o.Wallet = P6.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk12 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG6 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG6 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N6 ON o.Wallet = N6.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk13 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS7
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS7 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P7 ON o.Wallet = P7.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk14 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG7 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG7 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N7 ON o.Wallet = N7.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk15 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS8
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS8 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P8 ON o.Wallet = P8.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk16 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG8 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG8 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N8 ON o.Wallet = N8.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk17 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS9
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS9 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P9 ON o.Wallet = P9.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk18 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG9 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG9 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N9 ON o.Wallet = N9.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk19 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS10
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS10 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P10 ON o.Wallet = P10.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk20 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG10 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG10 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N10 ON o.Wallet = N10.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk21 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS11
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS11 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P11 ON o.Wallet = P11.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk22 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG11 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG11 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N11 ON o.Wallet = N11.Wallet 

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1 DESC) as rnk23 from (
select wallet, min(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from basePOS12
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from basePOS12 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) P12 ON o.Wallet = P12.Wallet

FULL JOIN(
 select wallet, RANK() OVER(order by minprice1) as rnk24 from (
select wallet, max(price) as minprice1 from (
select wallet, price, avg(balanceBTC) as avgBalance, sum(abs(AmountBTC)) as sumAmount from baseNEG12 
group by wallet, price ) x
where sumAmount > 0.05*(SELECT sum(abs(AmountBTC)) from baseNEG12 y where x.wallet = y.wallet ) or sumAmount> 0.01*avgBalance 
group by wallet ) q ) N12 ON o.Wallet = N12.Wallet   ) isthisonlyone
) isthisonlyone2
WHERE score_yep>0
order by score_yep desc
