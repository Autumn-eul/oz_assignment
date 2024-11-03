-- 삭제 (7). payments 테이블에서 특정 지불 내역을 삭제하세요.
SELECT * FROM classicmodels.payments;
DELETE FROM payments WHERE checkNumber = 'MN89921';