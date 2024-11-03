-- 갱신 (2). products 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products
SET buyPrice = '999.99'
WHERE productName = 'The Queen Mary';
SELECT * FROM classicmodels.products WHERE productName = 'The Queen Mary';