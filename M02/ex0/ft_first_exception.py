def check_temperature(temp_str: str) -> None:
    print("Testing temperature:", temp_str)
    try:
        num: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if num > 40:
        print(f"Error: {num}°C is too hot for plants (max 40°C)\n")
    elif num < 0:
        print(f"Error: {num}°C is too cold for plants (min 0°C)\n")
    else:
        print(f"Temperature {num}°C is perfect for plants!\n")


def ft_first_exception() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature(25)
    check_temperature("abc")
    check_temperature(100)
    check_temperature(-50)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
