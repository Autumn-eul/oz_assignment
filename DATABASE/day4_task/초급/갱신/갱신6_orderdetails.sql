-- 갱신 (6). orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails
SET quantityOrdered = '100'
WHERE orderNumber = '12345';
SELECT * FROM classicmodels.orderdetails;