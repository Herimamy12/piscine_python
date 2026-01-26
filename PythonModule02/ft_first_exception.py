#!/usr/bin/env python3

def check_temperature(temp_str):
    try:
        temperature = int(temp_str)
        if temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temperature}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


if __name__ == "__main__":
    # Test cases
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")    # Valid temperature
    print("\nTesting temperature: abc")
    check_temperature("abc")    # Valid temperature
    print("\nTesting temperature: 100")
    check_temperature("100")    # Too cold
    print("\nTesting temperature: -50")
    check_temperature("-50")    # Too hot
    print("\nAll tests completed - program didn't crash!")
