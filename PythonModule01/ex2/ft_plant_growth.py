#!/usrc/bin/env/ python3

class Plant:
    def __init__(this, name: str, height: int, age: int) -> None:
        this._name = name
        this._height = height
        this._age = age
        this._growth_info = 0

    def blueprint(this) -> None:
        print(this._name, ": ", this._height, "cm ", sep="", end="")
        print(this._age, " days old", sep="")

    def grow(this, days: int) -> None:
        this._height += days
        this._growth_info += days

    def age(this, days: int) -> None:
        this._age += days

    def get_info(this) -> int:
        return this._growth_info


if __name__ == "__main__":
    days: int = 6
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.blueprint()
    rose.grow(days)
    rose.age(days)
    print("=== Day 7 ===")
    rose.blueprint()
    print("Growth this week: +", rose.get_info(), "cm", sep="")
