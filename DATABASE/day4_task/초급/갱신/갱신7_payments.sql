-- 갱신 (7). payments 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments
SET amount = '123456.78'
WHERE customerNumber = '1001';
SELECT * FROM classicmodels.payments WHERE customerNumber = '1001';