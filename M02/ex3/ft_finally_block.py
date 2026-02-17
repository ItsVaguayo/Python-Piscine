class WrongPlant(Exception):
    pass


def water_plants(plant_list: str) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise WrongPlant(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except WrongPlant as e:
        print(f"Error: {e}")
        return
    finally:
        print("Closing watering system (cleanup)")
    print('Watering completed successfully!')


def test_watering_system() -> None:
    correct_list = ["tomato", "lettuce", "carrots"]
    error_list = ["tomato", None, "onion"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(correct_list)
    print("\nTesting with error...")
    water_plants(error_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
