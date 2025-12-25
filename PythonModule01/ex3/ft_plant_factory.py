#!/usrc/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Created: {name}: {height}cm {age} days old")

    def blueprint(self) -> None:
        print(f"{self.__name}: {self.__height}cm {self.__age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    tab = []
    tab.append(Plant("Rose", 25, 30))
    tab.append(Plant("Cactus", 200, 365))
    tab.append(Plant("Cactus", 5, 90))
    tab.append(Plant("Sunflower", 80, 45))
    tab.append(Plant("Fern", 15, 120))
    print(f"\nTotal plants created: {tab.__len__()}")
