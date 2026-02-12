def garden_operations(error: str) -> None:
    if error == "ValueError":
        int("abc")
    elif error == "ZeroDivisionError":
        print(42/0)
    elif error == "FileNotFoundError":
        open("missing.txt")
    elif error == "KeyError":
        plantas = {}
        print(plantas["cactus"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()
    print('Testing FileNotFoundError...')
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    print('Testing FileNotFoundError...')
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e.strerror} '{e.filename}'")
    print()

    print('Testing KeyError...')
    try:
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()
    print('Testing multiple errors together..')
    try:
        garden_operations("ValueError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
