#!/usr/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def blueprint(self) -> None:
        print(f"{self.__name}: {self.__height}cm {self.__age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

    def set_color(self, color: str) -> None:
        self._color = color

    def blueprint(self) -> None:
        print(f"{self._name} (Flower): {self._height}cm, ", end="")
        print(f"{self._age} days, {self._color} color")

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

    def set_attribute(self, diameter: int, shade: int) -> None:
        self._diameter = diameter
        self._shade = shade

    def blueprint(self) -> None:
        print(f"{self._name} (Tree): {self._height}cm, ", end="")
        print(f"{self._age} days, {self._diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self._name} provides {self._shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

    def set_attribute(self, harvest: str, nutritional: str) -> None:
        self._harvest = harvest
        self._nutritional = nutritional

    def blueprint(self) -> None:
        print(f"{self._name} (Vegetable): {self._height}cm, ", end="")
        print(f"{self._age} days, {self._harvest} harvest")

    def describe(self) -> None:
        print(f"{self._name} is rich in vitamin {self._nutritional}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("rose", 25, 30)
    rose.set_color("red")
    rose.blueprint(), rose.bloom(), print()

    oak = Tree("oak", 500, 1825)
    oak.set_attribute(50, 78)
    oak.blueprint(), oak.produce_shade(), print()

    tomato = Vegetable("tomato", 80, 90)
    tomato.set_attribute("summer", "C")
    tomato.blueprint(), tomato.describe()
