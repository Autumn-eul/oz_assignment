-- 갱신 (1). customers 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers
SET addressLine1 = 'new_address'
WHERE customerName = 'new';
SELECT * FROM customers WHERE customerName = 'new';