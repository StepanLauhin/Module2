class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Значение количества страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Значение количества страниц должно быть положительным числом")
        self._pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Значение продолжительности должно быть типа float")
        if new_duration <= 0:
            raise ValueError("Значение продолжительности должно быть положительным числом")
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._duration!r})"


if __name__ == "__main__":
    book1 = PaperBook("Азазель", "Б. Акунин", 250)
    print(book1.pages)
    book1.pages = 356
    print(book1.pages)
    book2 = AudioBook("Азазель", "Б. Акунин", 120.0)
    print(book2.duration)
    book2.duration = 147.0
    print(book2.duration)
