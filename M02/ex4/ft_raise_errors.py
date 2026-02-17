def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if plant_name is None or plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         f"is too low (min 1)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too low (min 2)")
    else:
        print(f"Plant {plant_name} is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("Tomato", 5, 5)
    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 5, 5)
    except ValueError as e:
        print(e, "\n")
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(e, "\n")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e, "\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
