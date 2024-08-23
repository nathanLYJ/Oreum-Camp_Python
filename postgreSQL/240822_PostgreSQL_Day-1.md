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

select (strftime('%s', '23:30:30') - strftime('%s', '10:30:30'))/ 60 
-- SELECT (strftime('%s', '12:30') - strftime('%s', '10:45')) / 60 AS minutes_difference;
-- select julianday('2024-01-31')-julianday('2024-01-01')

SELECT 상품ID, 카테고리ID,
CASE
  WHEN 카테고리ID = 1 THEN '패션의류'
  WHEN 카테고리ID = 2 THEN '뷰티'
  WHEN 카테고리ID = 3 THEN    '식품'
  WHEN 카테고리ID = 4 THEN    '주방용품'
  WHEN 카테고리ID = 5 THEN    '생활용품'
  WHEN 카테고리ID = 6 THEN    '인테리어'
  WHEN 카테고리ID = 7 THEN    '스포츠/레저'
  WHEN 카테고리ID = 8 THEN    '가전'
  WHEN 카테고리ID = 9 THEN    '디지털'
  WHEN 카테고리ID = 10 THEN    '문구/오피스'
  ELSE '헬스/건강식품'
end 
as 카테고리명
from 상품;

-- SELECT 
-- CASE
--   WHEN floor=1 THEN '1층'
--   WHEN floor=2 THEN '2층'
--   WHEN floor=3 THEN '3층'
--   WHEN floor=4 THEN '4층'
--   ELSE '층수가 없어요.'
-- end;

SELECT 고객ID,
CASE
  WHEN COUNT(주문ID) >=2 THEN 'vip'
  ELSE 'normal'
end as 주문레벨,
COUNT(주문ID) as 주문개수
from 주문
GROUP by 고객ID
ORDER BY 고객ID DESC;

SELECT 이름, 주소,
CASE
  WHEN 주소 LIKE '서울%' THEN '서울 거주' 
  WHEN 주소 LIKE '경기%' THEN '경기 거주'
  WHEN 주소 LIKE '제주%' THEN '제주 거주'
  ELSE '그 외 지역'
END AS 거주지역
FROM 고객;

SELECT o.*,u.name, p.name, p.cost
FROM weniv_order AS o
INNER JOIN weniv_product AS p
ON CAST(o.product_id AS INTEGER) = CAST(p.id AS INTEGER)
INNER JOIN weniv_user AS u
ON CAST(o.user_id AS INTEGER) = CAST(u.id AS INTEGER);

-- 주문 테이블 기준으로 유저, 상품 테이블 조인해보세요!
SELECT o.*, u.*, p.*
FROM weniv_order as o
LEFT JOIN weniv_user as u
ON CAST(o.user_id AS INTEGER) = CAST(u.id AS INTEGER)
LEFT JOIN weniv_product AS p
ON CAST(o.product_id AS INTEGER) = CAST(p.id AS INTEGER);

SELECT 가입연도 AS year,
    COUNT(고객ID) AS count_user
FROM 고객
GROUP BY 가입연도
UNION ALL
SELECT 'Total' as year, COUNT(고객ID) as user_cnt
from 고객
order by 가입연도

-- alter table dddd
-- add phone varchar(11);
INSERT INTO dddd('phone')
VALUES ('01000000000');
select *
from dddd;

-- CREATE TABLE dddd(
--   id int PRIMARY KEY,
--   name varchar(12) 
-- );
INSERT INTO dddd
VALUES (1,'ali','01012345678');

-- weniv_product 테이블 추가
-- id, name, cost 컬럼 추가 
-- id : 기본키, name 30자 이내, cost 정수형으로 넣어주세요.
-- CREATE TABLE weniv_product(
--   id INT null PRIMARY KEY, 
--   name varchar(30) null, 
--   cost INT null
-- );

-- 데이터추가
-- INSERT INTO weniv_product -- (id, name, cost)
-- VALUES 
-- (1, 'desk', 200000),
-- (2, 'monitor', 500000),
-- (3, 'calender', 30000),
-- (4, 'pen', 1000),
-- (5, 'chair', 50000),
-- (6, 'bookshelf', 70000),
-- (7, 'wristband', 300),
-- (8, 'laptop case', 30000),
-- (9, 'sticker', 2500),
-- (10, 'key ring', 3500);

-- select 구문으로 데이터가 잘 들어갔는지 확인해주세요. 
SELECT *
FROM weniv_product