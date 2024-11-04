-- 문제3 : 영화 대여 상태 변경
UPDATE rental
SET return_date = NOW()
WHERE rental_id = 200;