#!/usr/bin/env python3


def water_plants(plant_list):
    print("Openinng watering system")
    list_plants = ["Fern", "Cactus", "Bamboo",
                   "Orchid", "Tomato", "Lettuce", "Carrot"]
    try:
        for plant in plant_list:
            if plant not in list_plants:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    plants_to_water = ["Tomato", "Lettuce", "Carrot"]
    water_plants(plants_to_water)

    print("Testing with error...")
    plants_to_water_with_error = ["Tomato", "None", "Cactus"]
    water_plants(plants_to_water_with_error)

    print("Cleanup always happens, even with errors.")
