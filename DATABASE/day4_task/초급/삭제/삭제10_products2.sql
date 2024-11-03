-- 삭제 (10). products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
SELECT * FROM classicmodels.products;
DELETE FROM products WHERE productLine = 'Motorcycles';