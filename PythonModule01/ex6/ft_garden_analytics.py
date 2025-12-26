#!/usr/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_info(self) -> str:
        return f"{self._name}: {self._height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

    def set_attribute(self, flowers: str) -> None:
        self._flowers = flowers

    def get_info(self) -> str:
        return super().get_info() + f", {self._flowers} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: int, height: int, age: int) -> None:
        super().__init__(name, height, age)

    def set_attribute(self, flowers: str, prize_points: int) -> None:
        super().set_attribute(flowers)
        self._prize_points = prize_points

    def get_info(self) -> str:
        return super().get_info() + f", Prize points: {self._prize_points}"


class GardenStats:
    _grew: int = 0
    _added: int = 0
    _regular: int = 0
    _flowering: int = 0
    _prize_flowers: int = 0

    def __init__(self):
        pass

    def grew_increment(self, grew: int) -> None:
        self._grew += grew

    def add_plant(self, plant: Plant) -> None:
        self._added += 1
        if type(plant) is PrizeFlower:
            self._prize_flowers += 1
        elif type(plant) is FloweringPlant:
            self._flowering += 1
        else:
            self._regular += 1

    def get_info(self) -> str:
        self.res = f"Plants added: {self._added}, Total growth: {self._grew}cm"
        self.res += f"\nPlant types: {self._regular} regular, "
        self.res += f"{self._flowering} flowering, "
        self.res += f"{self._prize_flowers} prize flowers"
        return self.res


class GardenManager:
    _grew: int = 0
    _plant = []
    _g_stats = GardenStats

    def __init__(self, name: str) -> None:
        self._name = name

    def add(self, plant: Plant) -> None:
        print(f"Added {plant._name} to {self._name}'s garden")
        self._plant.append(plant)
        self._g_stats.add_plant(self._g_stats, plant)

    def growth(self, grew: int) -> None:
        print(f"{self._name} is helping all plants grow...")
        for p in self._plant:
            print(f"{p._name} grew {grew}cm")
            p._height += grew
            self._g_stats.grew_increment(self._g_stats, grew)

    def report(self) -> None:
        print("=== Alice's Garden Report ===")
        print("Plants in garden:")
        for p in self._plant:
            print(f"- {p.get_info()}")
        print(f"\n{self._g_stats.get_info(self._g_stats)}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    oak = Plant("Oak Tree", 100, 100)
    rose = FloweringPlant("Rose", 25, 25)
    rose.set_attribute("red")
    sunflower = PrizeFlower("Sunflower", 50, 50)
    sunflower.set_attribute("yellow", 10)

    alice = GardenManager("Alice")
    alice.add(oak), alice.add(rose), alice.add(sunflower), print()
    alice.growth(1), print()
    alice.report()
