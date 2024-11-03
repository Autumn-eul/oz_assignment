-- 갱신 (10). products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products
SET buyPrice = '111.11'
WHERE buyPrice > 40 and buyPrice < 50;
SELECT * FROM classicmodels.products WHERE buyPrice = 111.11;