import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
@pytest.mark.usefixtures('create_list_books')
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверяем, что нельзя добавить две одинаковых книги
    def test_add_new_book_add_repeat_books(self):
        collector = BooksCollector()

        collector.add_new_book('Тестовая книга')
        collector.add_new_book('Тестовая книга')
        assert len(collector.get_books_rating()) == 1

    # проверяем, что можно изменить рейтинг
    def test_set_book_rating_book_available(self):
        collector = BooksCollector()

        collector.add_new_book('Тестовая книга')
        collector.set_book_rating('Тестовая книга', 10)
        assert collector.get_book_rating('Тестовая книга') == 10

    # проверяем, что нельзя добавить рейтинг к несуществующей книге
    def test_set_book_rating_book_unavailable(self):
        collector = BooksCollector()

        collector.set_book_rating('Тестовая книга', 10)
        assert collector.get_book_rating('Тестовая книга') == None

    # проверяем, что нельзя добавить рейтинг больше 10
    def test_set_book_rating_book_rating_more_then_10(self):
        collector = BooksCollector()
        collector.add_new_book('Тестовая книга')
        collector.set_book_rating('Тестовая книга', 11)
        assert collector.get_book_rating('Тестовая книга') == 1

    # проверяем, что получаем рейтинг искомой книги
    def test_get_books_with_specific_rating_return_ratings_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тестовая книга рейтинг 1')
        collector.add_new_book('Тестовая книга рейтинг 10')
        collector.set_book_rating('Тестовая книга рейтинг 10', 10)
        assert collector.get_book_rating('Тестовая книга рейтинг 10') == 10

    # проверяем, что возвращаются книги по определенному рейтингу
    def test_get_books_with_specific_rating_return_books_whit_rating_10(self, create_list_books):

        assert len(create_list_books.get_books_with_specific_rating(10)) == 2

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_one_book_in_favorites(self, create_list_books):

        create_list_books.add_book_in_favorites('Book 1')

        assert len(create_list_books.get_list_of_favorites_books()) == 1

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites_one_book_in_favorites(self, create_list_books):

        create_list_books.add_book_in_favorites('Book 1')
        create_list_books.add_book_in_favorites('Book 2')
        create_list_books.delete_book_from_favorites('Book 1')

        assert create_list_books.get_list_of_favorites_books()[0] == 'Book 2'

    # получаем список Избранных книг (не стал писать проверку, т.к. в предыдущих двух проверках она используется, если бы не работала тест упал бы)

