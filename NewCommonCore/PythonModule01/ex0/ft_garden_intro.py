#!/usr/bin/env/ python3

def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    name: str = "Rose"
    height: int = 25
    age: int = 30
    print("Plant:", name, sep=" ")
    print("Height: ", height, "cm", sep="")
    print("Age:", age, "days", sep=" ")


if __name__ == "__main__":
    ft_garden_intro()
    print("=== End of Program ===")
