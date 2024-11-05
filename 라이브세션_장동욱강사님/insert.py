import json
import pymysql

def insert_books_to_mysql(json_file):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password = '0000',
        database='amazon',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()

    with open(json_file, 'r', encoding='utf-8') as f:
        books = json.load(f)

    insert_query = """
    INSERT INTO books (
        title, published_at
    ) VALUES (
        %s, %s
    )
    """

    # Insert each book entry
    for book in books:
        cursor.execute(insert_query, (
            book.get('title'),
            book.get('first_publish_year'),
        ))

    connection.commit()
    cursor.close()
    connection.close()
    print("Data inserted successfully")

json_file = 'amazon_books.json'
insert_books_to_mysql(json_file)