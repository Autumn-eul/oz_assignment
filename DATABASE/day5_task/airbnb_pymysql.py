import pymysql
connection = pymysql.connect (
    host = 'localhost',
    user = 'root',
    password = '0000',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # 문제1 : 새로운 제품 추가
    sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    cursor.execute(sql, ('Python Book', 10000, 10))
    connection.commit()

    # 문제2 : 고객 목록 조회
    cursor.execute("SELECT * FROM Products")
    for book in cursor.fetchall():
        print(book)

    # 문제3 : 제품 재고 업데이트
    sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    cursor.execute(sql, (1, 1))
    connection.commit()

    # 문제4 : 고객별 총 주문 금액
    sql = "SELECT customerId, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID"
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(datas)

    # 문제5 : 고객 이메일 업데이트
    sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    cursor.execute(sql, ('update@update.com', 1))
    connection.commit()

    # 문제6 : 주문 취소
    sql = "DELETE FROM Orders WHERE orderID = %s"
    cursor.execute(sql, (15))
    connection.commit()

    # 문제7 : 특정 제품 검색
    sql = "SELECT * FROM Products WHERE productName LIKE %s"
    cursor.execute(sql, ('%Book%'))
    datas = cursor.fetchall()

    for data in datas:
        print(data['productName'])

    # 문제8 : 특정 고객의 주문 데이터 조회
    sql = "SELECT * FROM Orders WHERE customerID = %s"
    cursor.execute(sql, (1))
    datas = cursor.fetchall()
    
    for data in datas:
        print(datas)

    # 문제9 : 가장 많이 주문한 고객 (주문 횟수가 가장 많은 고객을 조회)
    sql = """
        SELECT customerId, COUNT(*) as orderCount
        FROM Orders GROUP BY customerID
        ORDER BY orderCount DESC LIMIT 1
        """
    cursor.execute(sql)
    datas = cursor.fetchone()
    print(datas)

cursor.close()