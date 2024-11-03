-- 갱신 (9). customers 테이블에서 특정 고객의 이메일을 갱신하세요. 이메일이 없으니 주소를 갱신하겠습니다.
UPDATE customers
SET addressLine1 = 'new_address2'
WHERE customerName = 'new2';
SELECT * FROM classicmodels.customers WHERE customerName = 'new2';