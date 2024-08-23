select *
from 고객
WHERE 가입연도 >=2022
and 가입월 ='02'

select *
from 고객
WHERE 가입연도 >=2022
or 가입월 ='02'

select *
from 고객
WHERE not (가입연도=2022) -- != 2022

select *
from 고객
WHERE not (가입연도=2022 or 가입연도=2015)

select *
from 상품
-- WHERE 카테고리ID=10 and (재고 <50 or 재고 >10) : 카테고리 ID가 10인 상품 중 재고가 50미만이거나 10초과인 상품
-- 카테고리 ID가 10이거나 재고가 50미만이거나 10초과인 상품을 조회
WHERE 카테고리ID=10 
and 재고 <50 
or 재고 >10

select *
from 상품
where 재고 between 20 and 40 ;
-- where 재고 >= 20 and 재고 <=40 ;
-- where 재고 >= 20 and 재고 < 40 ;

CREATE TABLE my_table (
    id INTEGER PRIMARY KEY,
    datetime_column TEXT
);

INSERT INTO my_table (datetime_column)
VALUES 
('2024-01-01 00:00:00'),
('2024-01-31 00:00:00'),
('2024-01-31 01:00:00'),
('2024-02-01 00:00:00');

select *
from my_table
where datetime_column>='2024-01-01' and '2024-02-01';
-- 2024-01-01 00:00:00

-- between, in, like, is null
select *
from 상품
-- where 공급업체ID=101 or 공급업체ID=103 or 공급업체ID=105
where 공급업체ID in (101,103,105)

-- 주문월별 총주문금액이 30000 이상인 고객이 3명 이상인 주문월의 데이터를 조회하고, 
-- 그 중 고객 수가 가장 많은 상위 3개의 주문월을 가져오기
SELECT 주문월, count(고객ID) as user_count -- 5. 어떤 값을 출력할건지
FROM 주문-- 1. 테이블 선택
WHERE 총주문금액>=30000 -- 2. 조건을 입력
GROUP BY 주문월 -- 3. 어떤 카테고리?
HAVING count(고객ID)>=3 -- 4. 그룹화 한 값에 대한 조건
ORDER BY user_count desc-- 6. 정렬
LIMIT 3 -- 7. 상위 몇개?`

-- select length('hello world');
select 이메일, length(이메일)
from 고객;
-- select replace('문자열',바꿔야 하는 값,바꿀값)
-- select replace(이메일,'user-','')
-- from 고객
-- select Lower('Abc');
-- select Upper('Abc');

-- select cast(데이터 as 타입명) 
-- TEXT, STRING: 문자열, typeof(): 데이터 타입 출력
-- select typeof(cast(123 as TEXT))
-- select cast(123.123 as TEXT)
-- select cast(true as TEXT)
-- select cast(false as TEXT)
-- select cast(NULL as TEXT)
-- select cast(데이터 as 타입명)

select 123::STRING;
select 123.123::STRING;
select 123.123::STRING;