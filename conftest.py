import pytest
from main import BooksCollector


@pytest.fixture
def create_list_books():
    books_list = BooksCollector()
    for i in range(5):
        books_list.add_new_book('Book ' + str(1 + i))
    books_list.set_book_rating('Book 1', 10)
    books_list.set_book_rating('Book 2', 10)
    return books_list





