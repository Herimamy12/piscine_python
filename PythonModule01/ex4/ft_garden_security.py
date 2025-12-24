#!/usr/bin/env/ python3

class SecurePlant:
    __age: int = 0
    __height: int = 0

    def __init__(self, name: str) -> None:
        self.__name = name.capitalize()
        print(f"Plant created: {self.__name}")

    def invalid_checker(self, value: int, ref: str) -> bool:
        if value < 0:
            print(f"\nInvalid operation attempted: {ref} {value} [REJECTED]")
            print(f"Security: Negative {ref} rejected")
            return True
        return False

    def set_height(self, height: int) -> None:
        if self.invalid_checker(height, "height"):
            return
        print(f"Height updated: {height}cm [OK]")
        self.__height = height

    def set_age(self, age: int) -> None:
        if self.invalid_checker(age, "age"):
            return
        print(f"Age updated: {age} days [OK]")
        self.__age = age

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> str:
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.get_info()}")
