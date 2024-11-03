-- 삭제 (9). customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
SELECT * FROM classicmodels.customers;
DELETE FROM customers WHERE state = 'Tokyo';