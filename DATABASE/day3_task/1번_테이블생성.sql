-- 1. employees 테이블을 생성해주세요
CREATE TABLE employees (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);