# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union, List


class PipeCatalogue:
    def __init__(self, list_of_nominal_diameters: List[int], list_of_thicknesses: List[Union[int, float]],
                 list_of_outer_diameters: List[int]):
        """
        Создание объекта "Каталог труб"  и занесение в него необходимых параметров

        :param list_of_nominal_diameters: Список условных (номинальных) диаметров
        :param list_of_thicknesses: Список внутренних диаметров
        :param list_of_outer_diameters: Список внешних диаметров

        Пример:
        >>> pipe_catalogue = PipeCatalogue([10, 20, 50],[2.5, 4.5, 10],[16, 28, 76]) # инициализация экземпляра класса
        """
        if not isinstance(list_of_nominal_diameters, list):
            raise TypeError("Список условных диаметров должен быть типа list")
        if not isinstance(list_of_thicknesses, list):
            raise TypeError("Список толщин должен быть типа list")
        if not isinstance(list_of_outer_diameters, list):
            raise TypeError("Список внешних диаметров должен быть типа list")
        if not len(list_of_outer_diameters) == len(list_of_outer_diameters) and \
                len(list_of_outer_diameters) == len(list_of_thicknesses):
            raise ValueError("Входные списки должны иметь одинаковую длину")
        error_indexes = []
        for index, value in enumerate(list_of_nominal_diameters):
            if not isinstance(value, int):
                error_indexes.append(index)
        if not error_indexes == []:
            raise TypeError(f'Значения по индексам {error_indexes} в списке условных (номинальных) диаметров имеют тип,'
                            f' отличный от int')
        error_indexes = []
        for index, value in enumerate(list_of_outer_diameters):
            if not isinstance(value, int):
                error_indexes.append(index)
        if not error_indexes == []:
            raise TypeError(f'Значения по индексам {error_indexes} в списке внешних диаметров имеют тип,'
                            f' отличный от int')
        error_indexes = []
        for index, value in enumerate(list_of_thicknesses):
            if not isinstance(value, int | float):
                error_indexes.append(index)
        if not error_indexes == []:
            raise TypeError(f'Значения по индексам {error_indexes} в списке толщин имеют тип,'
                            f' отличный от int или float')
        error_indexes = []
        for index, value in enumerate(list_of_nominal_diameters):
            if value < 0:
                error_indexes.append(index)
        if not error_indexes == []:
            raise TypeError(f'Значения по индексам {error_indexes} в списке условных (номинальных) диаметров '
                            f'отрицательные')
        error_indexes = []
        for index, value in enumerate(list_of_outer_diameters):
            if value < 0:
                error_indexes.append(index)
        if not error_indexes == []:
            raise TypeError(f'Значения по индексам {error_indexes} в списке внешних диаметров отрицательные')
        error_indexes = []
        for index, value in enumerate(list_of_thicknesses):
            if value < 0:
                error_indexes.append(index)
        if not error_indexes == []:
            raise TypeError(f'Значения по индексам {error_indexes} в списке толщин отрицательные')
        self.list_of_nominal_diameters = list_of_nominal_diameters
        self.list_of_thickness = list_of_thicknesses
        self.list_of_outer_diameters = list_of_outer_diameters
        self.catalogue = None
        self.catalogue = self.create_catalogue()

    def create_catalogue(self) -> List[dict]:
        """
        Функция, которая создает каталог труб, где каждая позиция - словарь с ключами: "Условный диаметр", "Толщина",
        "Внешний диаметр"

        :return: Список словарей, описывающий трубы в каталоге
        """
        ...

    # Если я правильно понимаю, эту функцию можно ещё оформить как
    # def __getitem__(self, pipe_index):
    def get_pipe_by_index(self, pipe_index: int) -> dict:
        """
        Функция, позволяющая получить параметры трубы по её индексу в каталоге

        :param pipe_index: Индекс трубы в каталоге
        :return: Представление трубы в виде словаря с ключами: "Условный диаметр", "Толщина", "Внешний диаметр"

        Пример:
        >>> pipe_catalogue = PipeCatalogue([10, 20, 50],[2.5, 4.5, 10],[16, 28, 76])
        >>> pipe_catalogue.get_pipe_by_index(1)  # Тест ругается, так как сам список не сформирован функцией
        """
        if not isinstance(pipe_index, int):
            raise TypeError("Индекс трубы должен быть типа int")
        if pipe_index > len(self.catalogue) - 1 or abs(pipe_index) > len(self.catalogue):
            # Ругается на эту проверку
            raise ValueError("В каталоге нет трубы под таким индексом")
        ...

    def pipe_append(self, new_nominal_diameter: int, new_thickness: Union[int, float], new_outer_diameter: int) -> None:
        """
        Функция, позволяющая добавить трубу в каталог

        :param new_nominal_diameter: Условный (номинальный) диаметр новой трубы
        :param new_thickness: Толщина новой трубы
        :param new_outer_diameter: Внешний диаметр новой трубы

        Пример:
        >>> pipe_catalogue = PipeCatalogue([10, 20, 50],[2.5, 4.5, 10],[16, 28, 76])
        >>> pipe_catalogue.pipe_append(100,2.5,108)
        """
        if not isinstance(new_nominal_diameter, int):
            raise TypeError("Условный диаметр должен быть типа int")
        if not isinstance(new_thickness, int | float):
            raise TypeError("Толщина должна быть типа int или float")
        if not isinstance(new_outer_diameter, int):
            raise ValueError("Внешний диаметр должен быть типа int")
        if new_nominal_diameter < 0:
            raise ValueError("Условный диаметр должен быть положительным")
        if new_thickness < 0:
            raise ValueError("Толщина должна быть положительным")
        if new_outer_diameter < 0:
            raise ValueError("Внешний диаметр должен быть положительным")
        ...


class PipelineBranch:
    def __init__(self, nominal_diameter: int, angle: int, radius: int):
        """
        Создание объекта "Отвод" и задание его параметров (обычно по определенным стандартам: ГОСТ, ОСТ, СТО и т.д.)

        :param nominal_diameter: условный (номинальный) диаметр
        :param angle: угол поворота
        :param radius: радиус дуги

        Пример:
        >>> branch = PipelineBranch(100,15,435) # инициализация экземпляра класса
        """
        if not isinstance(nominal_diameter, int):
            raise TypeError("Условный диаметр должен быть типа int")
        if not isinstance(angle, int):
            raise TypeError("Угол поворота должен быть типа int")
        if not isinstance(radius, int):
            raise TypeError("Радиус дуги должен быть типа int")
        if nominal_diameter < 0:
            raise ValueError("Условный диаметр не может быть отрицательным числом")
        if angle < 0:
            raise ValueError("Угол поворота не может быть отрицательным числом")
        if radius < 0:
            raise ValueError("Радиус дуги не может быть отрицательным числом")
        self.nominal_diameter = nominal_diameter
        self.angle = angle
        self.radius = radius
        if not self.is_in_ost_34_10_752_97():
            ValueError("Входные параметры не соответствуют ОСТ 34 10.752-97")

    def is_in_ost_34_10_752_97(self) -> bool:
        """
        Функция, проверяющая соответствие входных параметров ОСТ 34 10.752-97

        :return: Соответствует ли отвод ОСТ 34 10.752-97
        """
        ...

    def change_angle(self, new_angle: int) -> None:
        """
        Изменение угла поворота отвода

        :param new_angle: Новый угол поворота

        Пример:
        >>> branch = PipelineBranch(100,15,435)
        >>> branch.change_angle(30)
        """
        ...

    def fit_pipe_from_catalogue(self, catalogue: PipeCatalogue, pipe_index: int) -> None:
        """
        Задает параметры отвода, подходящие трубе из каталога, выбранной по индексу

        :param catalogue: Каталог, трубе из которого нужно соответствовать
        :param pipe_index: Индекс трубы в каталоге, которой нужно соответствовать

        Пример:
        >>> branch = PipelineBranch(100,15,435)
        >>> pipe_catalogue = PipeCatalogue([10, 20, 50],[2.5, 4.5, 10],[16, 28, 76])
        >>> branch.fit_pipe_from_catalogue(pipe_catalogue,0)   # Тест ругается, так как сам список не сформирован функцией
        """
        if not isinstance(catalogue, PipeCatalogue):
            raise TypeError("Каталог труб должен быть объектом класса PipeCatalogue")
        if not isinstance(pipe_index, int):
            raise TypeError("Индекс трубы в каталоге должен быть типа int")
        if pipe_index > len(catalogue.catalogue) - 1 or abs(pipe_index) > len(catalogue.catalogue):
            # Ругается на эту проверку
            raise ValueError("В каталоге нет трубы под таким индексом")
        ...


class PlantProjectSub:
    def __init__(self, project_name: str, list_of_designers_names: List[str], project_scale: str):
        """
        Создание объекта "Подпись для проекта станции"

        :param project_name: Название проекта
        :param list_of_designers_names: Список имен проектировщиков
        :param scale_of_project: Масштаб, в котором проект исполнен

        Пример:
        >>> sub = PlantProjectSub("Большеглушицкая АЭС",["Петров Василий Сидорович","Сидоров Пётр Васильевич"],"1:500")
        """
        if not isinstance(project_name, str):
            raise TypeError("Название проекта должно быть типа str")
        if not isinstance(list_of_designers_names, list):
            raise TypeError("Список имен проектировщиков должен быть типа list")
        error_indexes = []
        for index, value in enumerate(list_of_designers_names):
            if not isinstance(value, str):
                error_indexes.append(index)
        if not error_indexes == []:
            raise TypeError(f'Значения по индексам {error_indexes} в списке имен проектировщиков имеют тип,'
                            f' отличный от str')
        if not isinstance(project_scale, str):
            raise ValueError("Масштаб проекта должен быть типа str")
        self.project_name = project_name
        self.list_of_designers_names = list_of_designers_names
        self.project_scale = project_scale

    def change_project_name(self, new_name: str) -> None:
        """
        Функция, меняющая название проекта

        :param new_name: Новое название проекта

        Пример:
        >>> sub = PlantProjectSub("Большеглушицкая АЭС",["Петров Василий Сидорович","Сидоров Пётр Васильевич"],"1:500")
        >>> sub.change_project_name("ТЭЦ Аркхэма")
        """
        if not isinstance(new_name, str):
            raise ValueError("Новое имя проекта должно быть типа str")
        ...

    def append_designer_name(self, new_designer_name: str) -> None:
        """
        Функция добавляет новое имя проектировщика к списку имён проектировщиков

        :param new_designer_name: Новое имя проектировщика

        Пример:
        >>> sub = PlantProjectSub("Большеглушицкая АЭС",["Петров Василий Сидорович","Сидоров Пётр Васильевич"],"1:500")
        >>> sub.append_designer_name("Васильев Сидор Петрович")
        """
        if not isinstance(new_designer_name, str):
            raise ValueError("Новое имя проектировщика должно быть типа str")
        ...

    def get_project_scale(self) -> str:
        """
        Функция, которая позволяет получить масштаб проекта

        :return: Масштаб проекта

        Пример:
        >>> sub = PlantProjectSub("Большеглушицкая АЭС",["Петров Василий Сидорович","Сидоров Пётр Васильевич"],"1:500")
        >>> sub.get_project_scale()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
