#!/usr/bin/env python3


class Inventory:
    def __init__(self):
        self.items = {
            "potion": 5,
            "armor": 3,
            "shield": 2,
            "sword": 1,
            "helmet": 1
        }

    def most_abundant(self):
        if not self.items:
            return None
        return max(self.items, key=self.items.get)

    def least_abundant(self):
        if not self.items:
            return None
        return min(self.items, key=self.items.get)

    def total_items(self):
        return sum(self.items.values())

    def total_item_types(self):
        return len(self.items)

    def printInventory(self):
        for item, value in self.items.items():
            print(f"{item}: {value}", end=" ")
            print("units" if value > 1 else "unit", end=" ")
            print(f"({(value / self.total_items()) * 100:.1f}%)")

    def moderate_items(self):
        return {item: qty for item, qty in self.items.items() if qty > 4}

    def scarce_items(self):
        return {item: qty for item, qty in self.items.items() if qty < 5}

    def restock_suggestions(self):
        suggestions = {}
        for item, qty in self.items.items():
            if qty < 2:
                suggestions[item] = "Restock needed"
            elif qty < 4:
                suggestions[item] = "Consider restocking"
            else:
                suggestions[item] = "Sufficient stock"
        return suggestions

    def get_restock_list(self):
        return [item for item, qty in self.items.items() if qty < 2]


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    i = Inventory()
    print("Total items in inventory:", i.total_items())
    print("Unique item types:", i.total_item_types())
    print()

    print("=== Current Inventory ===")
    i.printInventory()
    print()

    print("=== Inventory Statistics ===")
    most = i.most_abundant()
    least = i.least_abundant()
    print("Most abundant:", most, f"({i.items[most]} units)")
    print("Least abundant:", least, f"({i.items[least]} unit)")
    print()

    print("=== Item Categories ===")
    print(f"Moderate: {i.moderate_items()}")
    print(f"Scarce: {i.scarce_items()}")
    print()

    print("=== Management Suggestions ===")
    print(f"Restock needed: {i.get_restock_list()}")
    print()

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(i.items.keys())}")
    print(f"Dictionary values: {list(i.items.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in i.items}")
