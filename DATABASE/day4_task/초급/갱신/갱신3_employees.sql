-- 갱신 (3). employees 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees
SET jobTitle = 'Sales Rep'
WHERE lastName = 'new';
SELECT * FROM classicmodels.employees WHERE lastName = 'new';