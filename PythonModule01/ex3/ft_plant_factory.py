#!/usrc/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        print(f"Created: {name}: {height}cm {age} days old")

    def blueprint(self) -> None:
        print(f"{self._name}: {self._height}cm {self._age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    tab = []
    tab.append(Plant("Rose", 25, 30))
    tab.append(Plant("Cactus", 200, 365))
    tab.append(Plant("Cactus", 5, 90))
    tab.append(Plant("Sunflower", 80, 45))
    tab.append(Plant("Fern", 15, 120))
    print(f"\nTotal plants created: {tab.__len__()}")
