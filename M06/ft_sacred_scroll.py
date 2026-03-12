import alchemy
import alchemy.elements


def ft_sacred_scroll() -> None:
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): ", alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): ", alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): ", alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): ", alchemy.elements.create_air())
    print("\nTesting package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): ", alchemy.create_fire())
    print("alchemy.create_water(): ", alchemy.create_water())
    try:
        print("alchemy.create_earth(): ", alchemy.create_earth())
        print("alchemy.create_air(): ", alchemy.create_air())
    except AttributeError as e:
        print("alchemy.create_earth(): ", e)
        print("alchemy.create_air(): ", e)
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    ft_sacred_scroll()
