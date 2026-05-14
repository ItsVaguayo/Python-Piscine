def method_1():
    import alchemy.elements
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire():"
          f"{alchemy.elements.create_fire()}\n")


def method_2():
    from alchemy.elements import create_water
    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}\n")


def method_3():
    from alchemy.potions import healing_potion as heal
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}\n")


def method_4():
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}\n")


def ft_import_transmutation():
    print("=== Import Transmutation Mastery ===")
    method_1()
    method_2()
    method_3()
    method_4()
    print("All import transmutation methods mastered!  ·")
if __name__ == "__main__":
    ft_import_transmutation()