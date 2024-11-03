-- 생성 (7). payments 테이블에 새 지불 정보를 추가하세요.
SELECT * FROM classicmodels.payments;
INSERT INTO payments (customerNumber, checkNumber) VALUES ('1001', 'new');