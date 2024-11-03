-- 갱신 (4). offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
UPDATE offices
SET phone = '+12 34 567 8910'
WHERE city = 'new';
SELECT * FROM classicmodels.offices WHERE city = 'new';