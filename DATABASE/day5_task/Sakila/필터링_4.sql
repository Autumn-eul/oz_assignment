-- 문제4 : 가장 최근에 추가된 10개의 영화 조회
SELECT title, release_year
FROM film
ORDER BY release_year DESC
LIMIT 10;