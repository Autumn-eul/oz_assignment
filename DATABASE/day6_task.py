import pymysql
import random
from faker import Faker

# Faker 객체 생성
fake = Faker()

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host='localhost',  # '127.0.0.1'
    user='root',  # 사용자 이름
    password='0000',  # 비밀번호
    database='fish_shaped_bun_shop',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # 더미 사용자 데이터 50명 만들기
        for _ in range(50):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.unique.email()
            password = fake.password()
            address = fake.address()
            contact = fake.phone_number()
            is_active = random.choice([True, False])
            is_staff = random.choice([True, False])
            is_orderable = random.choice([True, False])
            gender = random.choice(["Male", "Female"])

            cursor.execute("""
                INSERT INTO users (first_name, last_name, email, password, address, contact, is_active, is_staff, is_orderable, gender)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, email, password, address, contact, is_active, is_staff, is_orderable, gender))

        # 더미 원재료 데이터 삽입
        raw_materials = [
            ('Flour', 1.76),
            ('Sugar', 2.00),
            ('Yeast', 0.50),
            ('Red Bean Paste', 4.50),
            ('Chocolate', 28.00),
            ('Cream', 4.50),
            ('Corn Cheese', 11.40),
            ('Coffee Cream', 6.50)
        ]
        for name, price in raw_materials:
            cursor.execute("""
                INSERT INTO raw_materials (name, price)
                VALUES (%s, %s)
            """, (name, price))

        # 더미 재고 데이터 삽입
        cursor.execute("SELECT id FROM raw_materials") # 데이터베이스에서 raw_materials 테이블의 id 값을 가져옴
        raw_material_ids = [row['id'] for row in cursor.fetchall()] # raw_materials 테이블의 모든 id 값을 리스트로 저장

        for _ in range(20): # 더미 재고 데이터 20개 만들기
            raw_material_id = random.choice(raw_material_ids) # raw_material_ids 에서 무작위로 하나의 id 를 선택
            quantity = random.randint(50, 200) # quantity 를 50 에서 200 사이의 무작위 값으로 설정
            cursor.execute("""
                INSERT INTO stocks (raw_material_id, quantity)
                VALUES (%s, %s)
            """, (raw_material_id, quantity)) # stock 테이블에 raw_material_id 와 quantity 값을 삽입

        # 더미 제품 데이터 삽입
        products = [ # products 리스트 생성하여 제품 이름과 설명, 가격을 저장
            ('Fish Bun', 'A delicious fish-shaped bun.', 3.00),
            ('Red Bean Bun', 'Sweet bun filled with red bean paste.', 2.50),
            ('Chocolate Bun', 'Decadent chocolate-filled bun.', 3.50),
            ('Corn Cheese Bun', 'Salty and sweet bun.', 3.50),
            ('Coffee Bun', 'Light bread with fragrant and savory coffee cream.', 3.50) # 본인만의 시그니쳐 메뉴 포함
        ]
        for name, description, price in products: # products 리스트에서 이름, 설명, 가격을 하나씩 꺼내는 반복문 실행
            cursor.execute("""
                INSERT INTO products (name, description, price)
                VALUES (%s, %s, %s)
            """, (name, description, price)) # products 테이블에 제품의 이름, 설명, 가격을 삽입하는 SQL 쿼리 실행

        # 더미 판매 기록 데이터 삽입
        cursor.execute("SELECT id FROM users") # 데이터베이스에서 users 테이블의 id 값을 가져옴
        user_ids = [row['id'] for row in cursor.fetchall()] # users 테이블의 모든 id 값을 리스트로 저장

        cursor.execute("SELECT id FROM products") # 데이터베이스에서 products 테이블의 id 값을 가져옴
        product_ids = [row['id'] for row in cursor.fetchall()] # products 테이블의 모든 id 값을 리스트로 저장

        # 각 사용자에 대해 판매 기록을 생성
        for user_id in user_ids: # 리스트에서 user_id 값을 하나씩 꺼내서 반복문 실행
            created_at = fake.date_time_this_year() # 판매 기록의 생성 날짜를 현재 연도의 임의 날짜로 설정
            cursor.execute("""
                INSERT INTO sales_records (user_id, created_at)
                VALUES (%s, %s)
            """, (user_id, created_at)) # sales_records 테이블에 사용자의 id 와 생성 날짜를 삽입하는 SQL 쿼리 실행

            # 삽입된 판매 기록의 id 를 가져옴
            sales_record_id = cursor.lastrowid

            for _ in range(random.randint(1, 3)):  # 각 판매 기록에 대해 1 ~ 3개의 상품을 추가
                product_id = random.choice(product_ids) # product_ids 리스트에서 무작위로 하나의 product_id 를 선택
                quantity = random.randint(1, 5) # quantity 를 1에서 5 사이의 무작위 값으로 설정
                cursor.execute("""
                    INSERT INTO sales_items (sales_record_id, product_id, quantity)
                    VALUES (%s, %s, %s)
                """, (sales_record_id, product_id, quantity)) # sales_items 테이블에 판매 기록 id, 상품 id, 수량을 삽입

        # daily_records 테이블에 더미 데이터 20개 만들기
        cursor.execute("SELECT id FROM stocks") # 데이터베이스에서 stocks 테이블의 id 값을 가져옴
        stock_ids = [row['id'] for row in cursor.fetchall()]

        for _ in range(30):
            stock_id = random.choice(stock_ids) # stock_ids 에서 무작위로 하나의 id 를 선택
            change_quantity = random.randint(10, 200) # change_quantity 를 10 에서 200 사이의 무작위 값으로 설정
            cursor.execute("""
                INSERT INTO daily_records (stock_id, change_quantity)
                VALUES (%s, %s)
            """, (stock_id, change_quantity)) # daily_records 테이블에 stock_id, change_auantiy

        # 변경 사항 커밋
        connection.commit()

finally:
    connection.close()