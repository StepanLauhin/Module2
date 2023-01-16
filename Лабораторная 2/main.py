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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
