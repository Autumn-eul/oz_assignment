-- 갱신 (8). productlines 테이블에서 특정 제품라인의 설명을 갱신하세요.
UPDATE productlines
SET textDescription = 'new_description'
WHERE productLine = 'new';
SELECT * FROM classicmodels.productlines WHERE productLine = 'new';