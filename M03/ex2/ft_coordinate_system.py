import sys
import math


def calculate_distance(p1: tuple[int, int, int],
                       p2: tuple[int, int, int]) -> float:
    return math.sqrt((p2[0] - p1[0]) ** 2 +
                     (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)


def parse_argv(temp_list: list[str]) -> tuple[int, int, int]:
    parsed_list: list[int] = [int(n) for n in temp_list]
    return tuple(parsed_list)


def ft_coordinate_system() -> None:
    if len(sys.argv) < 2:
        print("This program need 2 arguments.. Try again")
        return
    print("=== Game Coordinate System ===\n")
    tuple0: tuple[int, int, int] = (0, 0, 0)
    tuple1: tuple[int, int, int] = (10, 20, 5)
    print("Position created:", tuple1)
    print(f"Distance between {tuple0} and {tuple1}:",
          f"{calculate_distance(tuple0, tuple1):.2f}")
    print(f"\nParsing coordinates: '{sys.argv[1]}'")
    tuple1 = parse_argv(sys.argv[1].split(","))
    print("Parsed position:", tuple1)
    print(f"Distance between {tuple0} and {tuple1}:",
          f"{calculate_distance(tuple0, tuple1):.1f}")
    print(f"\nParsing invalid coordinates: '{sys.argv[2]}'")
    try:
        tuple1 = parse_argv(sys.argv[2].split(","))
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
    print("Unpacking demonstration:")
    print(f'Player at x={tuple1[0]}, y={tuple1[1]},'
          f' z={tuple1[2]}')
    x: int
    y: int
    z: int
    x, y, z = tuple1
    print(f'Coordinates: X={x}, Y={y}, Z={z}')


if __name__ == "__main__":
    ft_coordinate_system()
