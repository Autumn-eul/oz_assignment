-- 생성 (5). orders 테이블에 새 주문을 추가하세요.
SELECT * FROM classicmodels.orders;
INSERT INTO orders (orderNumber, orderDate, comments, customerNumber) VALUES ('12345', '2024-11-01', 'new', '1001');