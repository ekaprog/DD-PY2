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

class ChristmasToys:
    def __init__(self, color: str, number: int ):
        """
        Создание и подготовка к работе объекта "Ёлочные игрушки"
        :param color: цвет игрушек
        :param number: количество игрушек

        Примеры:
        >>> christmas_toys = ChristmasToys('yellow', 15)
        """

        if not isinstance(color, str):
            raise TypeError("Цвет игрушек должен быть типа str")
        self.color = color

        if not isinstance(number, int):
            raise TypeError("Количество игрушек должно быть типа int")
        if number < 0:
            raise ValueError("Количество игрушек должно быть >= 0")
        self.number = number

    def change_color(self, color: str) -> None:
        """
        Смена цвета игрушек на ёлке

        :param color: новый цвет игрушек
        :raise TypeError: если задан не тип str, возвращается ошибка
        :raise ValueError: Если пользователь задаёт уже существующий цвет игрушек,
                           то возвращается ошибка

        Примеры:
        >>> christmas_toys = ChristmasToys('yellow', 15)
        >>> christmas_toys.change_color('blue')
        """
        ...

    def remove_toys(self, number: int) -> int:
        """
        Убираем игрушки

        :param number: количество игрушек, которые хотим убрать
        :raise TypeError: если количество убираемых игрушек не типа int, возвращается ошибка
        :raise ValueError: количество убираемых игрушек должно быть положительным числом и должно быть
                            меньше или равно ибщему количеству игрушек

        :return: Количество игрушек на ёлке после того, как убрали часть
        """
        ...


class ChristmasGarland:
    def __init__(self, number_of_bulbs: int, length: Union[int, float], number_of_colors: int):
        """
        Создание и подготовка к работе объекта "Новогодняя гирлянда"
        :param number_of_bulbs: количество лампочек
        :param length: длина гирлянды
        :param number_of_colors: количество цветов лампочек

        Пример:
        >>> christmas_garland = ChristmasGarland(200, 2.5, 4)
        """

        if not isinstance(number_of_bulbs, int):
            raise TypeError("Количество лампочек должно быть int")
        if not number_of_bulbs > 0:
            raise ValueError("Количество лампочек должно быть больше нуля")
        self.number_of_bulbs = number_of_bulbs

        if not isinstance(length, (int, float)):
            raise TypeError("Длина гирлянды должна быть типа int или float")
        if not length > 0:
            raise ValueError("Длина гирлянды должна быть больше нуля")
        self.length = length

        if not isinstance(number_of_colors, int):
            raise TypeError("Количество цветов лампочек должно быть типа int")
        if not number_of_colors >= 1:
            raise ValueError("Количество цветов лампочек не может быть меньше 1")
        self.number_of_colors = number_of_colors

    def add_bulbs(self, bulbs: int) -> int:
        """
        Добавить лампочки.

        :param bulbs: количество лампочек
        :raise TypeError: если количество добавляемых лампочек не типа int, возвращается ошибка
        :raise ValueError: количество добавляемых лампочек должно быть положительным числом

        :return: количество лампочек после добавления новых

        Примеры:
        >>> christmas_garland = ChristmasGarland(200, 2.5, 4)
        >>> christmas_garland.add_bulbs(20)
        """
        ...

    def add_colors(self, num_of_colors: int) -> int:
        """
        Добавить новые цвета (лампочки новых цветов) в гирлянду.

        :param num_of_colors: количество новых цветов
        :raise TypeError: если количество добавляемых цветов не типа int, возвращается ошибка
        :raise ValueError: количество добавляемых цветов должно быть положительным числом

        :return: количество цветов после добавления новых

        Примеры:
        >>> christmas_garland = ChristmasGarland(200, 2.5, 4)
        >>> christmas_garland.add_colors(1)
        """
        ...
        
        
if __name__ == "__main__":
    doctest.testmod()
