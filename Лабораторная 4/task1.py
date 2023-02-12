class Conifers:
    """Базовый класс Хвойные деревья"""

    def __init__(self,  height: float, age: int, country: str):
        self.height = height
        self.age = age
        self.country = country

    def __str__(self) -> str:
        return f"Хвойное дерево возрастом {self.age}, имеющее высоту {self.height} метров," \
               f" произрастает в {self.country}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(height={self.height!r}, age={self.age!r}," \
               f" country={self.country!r})"

    def display_ages(self) -> str:
        """
        Метод возвращает возраст растения
        """
        print(f"The age of this tree is {self.age} years.")

    def display_country(self) -> str:
        """
        Метод возвращает страну, в которой растёт дерево
        """
        print(f"{self.country}")


class Spruce(Conifers):
    """ Дочерний класс Еловые"""

    def __init__(self, height: float, age: int, country: str, part_of_country: str):
        super().__init__(height, age, country)
        self.part_of_country = part_of_country

    def __str__(self) -> str:
        return f"Хвойное дерево возрастом {self.age}, имеющее высоту {self.height} метров," \
               f" произрастает в {self.country}, а именно в {self.part_of_country} части."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(height={self.height!r}, age={self.age!r}," \
               f" country={self.country!r}, colour={self.part_of_country!r})"

    def display_ages(self) -> int:
        """
        Метод наследуется от Базового класса
        """

        return super().display_ages()

    def display_country(self) -> str:
        """
        Метод базового класса перегружается, добавляется вывод той части страны, в которой
        растёт дерево (например, южная/восточная часть)
        """
        super().display_country()
        print(f"{self.part_of_country} часть страны")



if __name__ == "__main__":

    pine_A = Conifers(1.7, 5, "Russia")
    spruce_B = Spruce(5.0, 40, "Russia", "west")

    pine_A.display_country()
    spruce_B.display_ages()
