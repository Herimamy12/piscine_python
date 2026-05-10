#!/usr/bin/env python3


def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None or plant_name.strip() == "":
        raise ValueError("Error: Plant name cannot be empty!\n")
    if water_level < 0:
        raise ValueError(f"Error: Water level {water_level} \
is too low (min 0)\n")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} \
is too high (max 10)\n")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} \
is too low (min 2)\n")
    if sunlight_hours > 24:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} \
is too high (max 24)\n")
    print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    print("Testing good values...")
    check_plant_health("tomato", 5, 6)

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(e)

    print("Testing bad water level...")
    try:
        check_plant_health("cucumber", 15, 6)
    except ValueError as e:
        print(e)

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("lettuce", 5, 0)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")
