from typing import List, Optional
from pydantic import BaseModel, PositiveInt, NonNegativeInt, constr


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book(BaseModel):
    """
    Создание объекта "Книга" и занесение в него необходимых параметров

    :param id_: id книги
    :param name: Название книги
    :param pages: Количество страниц в книге
    """

    id_: PositiveInt
    name: constr(strict=True)
    pages: NonNegativeInt

    def __str__(self) -> str:
        """
        Функция, выдающая текстовое представление объекта
        :return: "Книга <название>"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Функция, позволяющая получить строку кода для создания идентичного экземпляра
        :return: "<строка кода>"
        """
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library(BaseModel):

    """
    Создание объекта "Библиотека" из списка входящих в неё книг в виде объектов "Книга"

    :param books: Список книг в библиотеке
    """
    books: Optional[List[Book]] = []

    def get_next_book_id(self) -> int:
        """
        Функция, позволяющая получить индетификатор для добавления новой книги в библиотеку

        :return: последней книги в библиотеке + 1
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, required_id: int) -> int:
        """
        Функция позволяющая определить индекс книги по её id

        :param required_id: запрашиваемый индетификатор (if)
        :return: индекс
        """

        if not isinstance(required_id, int):
            raise TypeError("Запрашиваемый id должен быть типа int")
        if required_id < 1:
            raise ValueError("id книг могут быть только положительными целыми числами")

        for i, v in enumerate(self.books):
            if v.id_ == required_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
