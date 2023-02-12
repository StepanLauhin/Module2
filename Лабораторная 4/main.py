if __name__ == "__main__":
    # Write your solution here
    class SchoolBoy:
        def __init__(self, name: str, surname: str, backpack: list, marks: list, pocket_money: float):
            """
            Функция, создающая сущность в виде школьника

            :param name: Имя школьника
            :param surname: Фамилия его
            :param backpack: Список вещей в рюкзаке
            :param marks: Список оценок уважаемого школьника
            :param pocket_money: Количество денег на карманные расходы
            """

            self.name = name
            self.surname = surname
            self.backpack = backpack
            self.marks = marks
            self.pocket_money = pocket_money

        def __str__(self) -> str:
            """
            Функция, определяющая строковое представление объекта

            :return: строка
            """
            return f"Школьник {self.name} {self.surname}"

        def __repr__(self)->str:
            """
            Функция, создающая строку кода для создания идентичного экзмпляра класса

            :return: строка кода
            """
            return f"{self.__class__.__name__}(name={self.name!r}, surname={self.surname!r}, backpack={self.backpack}" \
                   f", marks={self.marks})"

        def buy_drink(self) -> None:
            """
            Функция, позволяющая приобрести напиток

            :return: Ничего
            """
            self.pocket_money -= 100
            self.backpack.append("Добрый Кола")

        def get_mark(self, new_mark) -> None:
            """
            Функция, позволяющая записать новую оценку

            :param new_mark: новая оценка
            :return: Ничего
            """
            self.marks.append(new_mark)

    class Student(SchoolBoy):
        # Вопрос по поводу наследования метода __init__. Если мне не требуется расширять функционал, но документация
        # явно требует изменений (например, здесь уже будет "сущность в виде студента") требуется ли перегружать метод?
        # Или нужно сделать документацию более обобщенной (например, "сущность в виде обучающегося")?
        def __str__(self) -> str:
            """
            Функция, определяющая строковое представление объекта

            :return: строка
            """
            return f"Студент {self.name} {self.surname}"

        def buy_drink(self) -> None:
            """
            Метод, позволяющий приобрести напиток, но уже другой.
            Метод перегружен по причине стереотипного предположения о том, что студенту ранее предложенный напиток уже
            не приносит прежней радости и требуется что-то покрепче (не осуждаю, но и не поддерживаю; сделано с целью
            демонстрации логики перегрузки)

            :return: Ничего
            """
            self.pocket_money -= 300
            self.backpack.append("Портвейн")

    pass
