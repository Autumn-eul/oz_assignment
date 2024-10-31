-- 5. PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요
UPDATE employees
SET salary = salary * 0.1 + salary
WHERE position = 'PM';

SELECT * FROM employees WHERE position = 'PM';