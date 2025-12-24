#!/usrc/bin/env/ python3

class Plant:
    def __init__(this, name: str, height: int, age: int) -> None:
        this._name = name
        this._height = height
        this._age = age

    def blueprint(this) -> None:
        print(this._name, ": ", this._height, "cm ", sep="", end="")
        print(this._age, " days old", sep="")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    tab = [Plant("Rose", 25, 30), Plant("Sunflower", 80, 45)]
    tab.append(Plant("Cactus", 15, 120))
    for plant in tab:
        plant.blueprint()
