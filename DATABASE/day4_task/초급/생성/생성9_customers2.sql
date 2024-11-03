-- 생성 (9). customers 테이블에 다른 지역의 고객을 추가하세요.
SELECT * FROM classicmodels.customers;
INSERT INTO customers (customerName, phone, addressLine1, city) VALUES ('new2', '01.23.6789', 'new2', 'new2');