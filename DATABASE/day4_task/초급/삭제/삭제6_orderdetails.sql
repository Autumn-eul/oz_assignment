-- 삭제 (6). orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
SELECT * FROM classicmodels.orderdetails;
DELETE FROM orderdetails WHERE orderNumber = '10264';