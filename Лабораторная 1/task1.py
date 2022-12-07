from typing import Union
import doctest


class ChristmasTree:
    def __init__(self, height: Union[int, float], number_of_toys: int, is_garland: bool):
        """
        Создание и подготовка к работе объекта "Новогодняя ёлка"
        :param height: высота ёлки
        :param number_of_toys: количество игрушек на ёлке
        :param is_garland: развешена ли на ёлке гирлянда

        Примеры:
        >>> christmas_tree = ChristmasTree(1.5, 50, False)
        """

        if not isinstance(height, (int, float)):
            raise TypeError("Высота ёлки должна быть типа int или float")
        if not height > 0:
            raise ValueError("Высота ёлки должна быть больше нуля")
        self.height = height

        if not isinstance(number_of_toys, int):
            raise TypeError("Количество игрушек должно быть типа int")
        if number_of_toys < 0:
            raise ValueError("Количество игрушек должно быть >= 0")
        self.number_of_toys = number_of_toys

        if not isinstance(is_garland, bool):
            raise TypeError("Наличие гирлянды на ёлке должно быть типа bool")
        self.is_garland = is_garland

        def hang_toy(self, toys: int) -> int:
            """
            Добавление новых игрушек на ёлку.

            :param toys: количество добавляемых игрушек
            :raise TypeError: если количество добавляемых игрушек не типа int, возвращается ошибка
            :raise ValueError: количество добавляемых игрушек должно быть положительным числом

            :return: Количество игрушек на ёлке после добавления новых

            Примеры:
            >>> christmas_tree = ChristmasTree(1.5, 50, False)
            >>> christmas_tree.hang_toy(5)
            """
            ...

        def hang_garland(self) -> None:
            """
            Добавление гирлянды на ёлку (True), если её не было (False)

            :raise ValueError: Если на ёлке уже есть гирлянда, то возвращается ошибка

            Примеры:
            >>> christmas_tree = ChristmasTree(1.5, 50, False)
            >>> christmas_tree.hang_garland()
            """
            ...


if __name__ == "__main__":
    doctest.testmod()
