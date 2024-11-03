-- 갱신 (5). orders 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders
SET status = 'Shipped'
WHERE orderNumber = '12345';
SELECT * FROM classicmodels.orders WHERE orderNumber = '12345';