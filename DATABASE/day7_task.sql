use fish_shaped_bun_shop;

-- 문제 1번
INSERT INTO 
users(
	first_name,
    last_name,
    email,
    password,
    address,
    contact,
    gender
)
VALUES(
	"BANANA",
    "MILK",
    "banana123@banana.com",
    "ekfjabsgjb1l4",
    "oz-coding-school",
    "010-1234-5678",
    TRUE
);

-- 확인하기
SELECT * FROM users WHERE id = 101;

-- 문제 2번
update users
set address = 'oz2'
where id = 101;

-- 확인하기
SELECT * FROM users WHERE id = 101;

-- 문제 3번
-- 주문 생성
INSERT INTO 
sales_records(
	user_id
)
value(
	101
);

-- 주문 입력
INSERT INTO
sales_items(
	sales_record_id,
    product_id,
    quantity
)
VALUES(
	101,
    (SELECT id FROM products WHERE name='Red Bean Bun'),
    3
);

INSERT INTO
sales_items(
	sales_record_id,
    product_id,
    quantity
)
VALUES(
	101,
    (SELECT id FROM products WHERE name="Fish Bun"),
    2
);

INSERT INTO
sales_items(
	sales_record_id,
    product_id,
    quantity
)
VALUES(
	101,
    (SELECT id FROM products WHERE name="Coffee Bun"),
    5
);

-- 확인하기
SELECT * FROM sales_items WHERE sales_record_id = 101;

-- 문제 4번
INSERT INTO
order_records(
	user_id,
    raw_material_id,
    quantity
)
VALUES(
	101,
    14,
    20
);

INSERT INTO
order_records(
	user_id,
    raw_material_id,
    quantity
)
VALUES(
	101,
    15,
    20
);

INSERT INTO
order_records(
	user_id,
    raw_material_id,
    quantity
)
VALUES(
	101,
    16,
    10
);

-- 확인하기
SELECT * FROM order_records WHERE user_id = 101;

-- 문제 5번
SELECT * FROM stocks;

INSERT INTO
daily_records(
	stock_id,
    change_quantity,
    change_type
)
VALUES(
	14,
    (SELECT quantity FROM stocks WHERE id = 14) + 20,
    "IN"
);

INSERT INTO
daily_records(
	stock_id,
    change_quantity,
    change_type
)
VALUES(
	15,
    (SELECT quantity FROM stocks WHERE id = 14) + 20,
    "IN"
);

INSERT INTO
daily_records(
	stock_id,
    change_quantity,
    change_type
)
VALUES(
	16,
    (SELECT quantity FROM stocks WHERE id = 14) + 20,
    "IN"
);

-- 원재료 사용 이력
INSERT INTO
daily_records(
	stock_id,
    change_quantity,
    change_type
)
VALUES(
	7,
    (SELECT quantity FROM stocks WHERE id = 7) - 3,
    "OUT"
);

INSERT INTO
daily_records(
	stock_id,
    change_quantity,
    change_type
)
VALUES(
	6,
    (SELECT quantity FROM stocks WHERE id = 6) - 2,
    "OUT"
);

INSERT INTO
daily_records(
	stock_id,
    change_quantity,
    change_type
)
VALUES(
	10,
    (SELECT quantity FROM stocks WHERE id = 10) - 5,
    "OUT"
);

-- 추가 이력 반영한 stocks 테이블에 새로운 데이터 생성
UPDATE stocks
SET quantity = quantity + 20
WHERE id = 14;

UPDATE stocks
SET quantity = quantity + 20
WHERE id = 15;

UPDATE stocks
SET quantity = quantity + 10
WHERE id = 16;

-- 문제 6번
SELECT
	sr.id AS saled_record_id,
    sr.created_at,
    u.first_name,
    u.last_name,
    si.product_id,
    SUM(si.quantity) AS total_quantity,
    p.price

FROM sales_items AS si

JOIN sales_records as sr ON si.sales_record_id = sr.id
JOIN users AS u ON sr.user_id = u.id
JOIN products AS p ON si.product_id = p.id
WHERE u.id = 101
GROUP BY si.product_id, sr.id, sr.created_at, u.first_name, u.last_name, p.price
ORDER BY p.price DESC;
    
    