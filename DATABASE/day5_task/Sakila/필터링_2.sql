-- 문제2 : 모든 카테고리와 해당 카테고리의 영화 수 조회
SELECT c.name, COUNT(fc.film_id) as number_of_films
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.name;