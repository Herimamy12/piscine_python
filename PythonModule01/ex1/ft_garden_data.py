#!/usrc/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def blueprint(self) -> None:
        print(f"{self._name}: {self._height}cm {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    tab = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45)]
    tab.append(Plant("Cactus", 15, 120))
    for plant in tab:
        plant.blueprint()
