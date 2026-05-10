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


class SunlightError(GardenError):
    """Exception raised for errors related to sunlight exposure."""
    def __init__(self, message="There was an error with sunlight exposure."):
        self.message = message
        super().__init__(self.message)


class Plant:
    def __init__(self, name, water_level, sunlight_hours):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManagement:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant: Plant):
        """Add a new plant to the garden."""
        try:
            if plant.name == "":
                raise PlantError("Error adding plant: \
Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(e)

    def water_plants(self):
        """Water all plants in the garden."""
        plant_list = ["tomato", "lettuce", "Daisy", "Sunflower", "Lily"]
        print("Opening watering system")
        if self.plants:
            try:
                for plant in self.plants:
                    if plant.name.lower() not in [
                        p.lower() for p in plant_list
                    ]:
                        raise WaterError(
                            f"Cannot water {plant.name} - " "invalid plant!"
                        )
                    print(f"Watering {plant.name} - success")
            except WaterError as e:
                print(f"Error: {e}")
            finally:
                print("Closing watering system (cleanup)\n")
        else:
            print("No plants to water.")

    def check_plant_health(self, plant):
        """Check the health of a specific plant."""
        if (plant in self.plants):
            if (plant.water_level < 0):
                raise WaterError(
                    f"Error checking {plant.name}: Water level \
{plant.water_level} is too low (min 0)"
                )
            if (plant.water_level > 10):
                raise WaterError(
                    f"Error checking {plant.name}: Water level \
{plant.water_level} is too high (max 10)"
                )
            if (plant.sunlight_hours < 2):
                raise SunlightError(
                    f"Error checking {plant.name}: Sunlight hours \
{plant.sunlight_hours} is too low (min 2)"
                )
            if (plant.sunlight_hours > 24):
                raise SunlightError(
                    f"Error checking {plant.name}: Sunlight hours \
{plant.sunlight_hours} is too high (max 24)"
                )
            print(f"{plant.name}: healthy (water: {plant.water_level}, \
sunlight: {plant.sunlight_hours})")
        else:
            print(f"Plant '{plant.name}' not found in the garden.")


def test_garden_management():
    garden = GardenManagement()
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("Lettuce", 15, 6)
    none = Plant("", 10, 5)

    print("Adding plants to garden...")
    garden.add_plant(tomato)
    garden.add_plant(lettuce)
    garden.add_plant(none)

    print("\nWatering plants...")
    garden.water_plants()

    print("Checking plant health...")
    try:
        garden.check_plant_health(tomato)
        garden.check_plant_health(lettuce)
    except GardenError as e:
        print(e)

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")
        print("System recovered and continuing...\n")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
    print("Garden management system test complete!")
