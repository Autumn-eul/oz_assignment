-- 삭제 (5). orders 테이블에서 특정 주문을 삭제하세요.
SELECT * FROM classicmodels.orders;
DELETE FROM orders WHERE orderNumber = '10264';