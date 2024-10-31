-- 6. 모든 Backend 직책을 가진 직원의 연봉을 5% 인상하세요
UPDATE employees
SET salary = salary * 0.05 + salary
WHERE position = 'Backend';

SELECT * FROM employees WHERE position = 'Backend';