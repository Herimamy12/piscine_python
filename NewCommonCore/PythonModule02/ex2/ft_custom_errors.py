#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for exceptions in the garden module."""
    pass


class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    def __init__(self, message="There was an error with the plant."):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    """Exception raised for errors related to watering."""
    def __init__(self, message="There was an error with watering the plants."):
        self.message = message
        super().__init__(self.message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as pe:
        print(f"Caught PlantError: {pe}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as we:
        print(f"Caught WaterError: {we}\n")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as ge:
        print(f"Caught a garden error: {ge}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as ge:
        print(f"Caught a garden error: {ge}\n")

    print("All custom error types work correctly!")
