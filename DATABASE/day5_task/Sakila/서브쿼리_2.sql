-- 문제2 : 평균 대여 요금보다 높은 요금의 영화 조회
SELECT f.title, f.rental_rate
FROM film f
WHERE f.rental_rate > (SELECT AVG(rental_rate) FROM film);