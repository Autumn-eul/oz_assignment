from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = []

@book_blp.route('/')
class BookList(MethodView): # 여러개의 데이터를 가져올 때 사용
    @book_blp.response(200, BookSchema(many=True)) # many = True books 에 저장된 모든 데이터를 보여준다
    def get(self):
        return books
    
    @book_blp.arguments(BookSchema)
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = len(books) + 1 # id 값이 1씩 증가하고 알아서 처리하게 만듬
        books.append(new_data)
        return new_data
    
@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = "Book not found.")
        return book
    
    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = "Book not found.")
        book.update(new_data)
        return book

    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message = "Book not found.")
        books = [book for book in books if book['id'] != book_id]
        return ''