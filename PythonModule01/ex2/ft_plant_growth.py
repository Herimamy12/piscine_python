#!/usrc/bin/env/ python3

week_growth: int = 6


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def blueprint(self) -> None:
        print(self._name, ": ", self._height, "cm ", sep="", end="")
        print(self._age, " days old", sep="")

    def grow(self) -> None:
        self._height += week_growth

    def age(self) -> None:
        self._age += week_growth

    def get_info(self) -> str:
        return f"{self._name}: {self._height}cm {self._age} days old"


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    tab = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45)]
    tab.append(Plant("Cactus", 15, 120))
    print("=== Day 1 ===")
    for plant in tab:
        plant.blueprint()
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    for p in tab:
        print(p.get_info())
    print(f"Growth this week: +{week_growth}cm")
