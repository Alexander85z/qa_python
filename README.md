# qa_python 1
- add_new_book_add_two_books (по умолчанию)

- add_new_book_add_repeat_books:  
проверяем, что нельзя добавить две одинаковых книги

- set_book_rating_book_available:  
проверяем, что можно изменить рейтинг

- set_book_rating_book_unavailable:  
проверяем, что нельзя добавить рейтинг к несуществующей книге

- set_book_rating_book_rating_more_then_10:  
проверяем, что нельзя добавить рейтинг больше 10

- get_books_with_specific_rating_return_ratings_book(self):  
проверяем, что получаем рейтинг искомой книги

- get_books_with_specific_rating_return_books_whit_rating_10:  
проверяем, что возвращаются книги по определенному рейтингу

- test_add_book_in_favorites_one_book_in_favorites:  
добавляем книгу в Избранное

- test_delete_book_from_favorites_one_book_in_favorites:  
удаляем книгу из Избранного

- получаем список Избранных книг (не стал писать проверку, т.к. в предыдущих двух проверках она используется, если бы не работала тест упал бы)