def ft_seed_inventory(vegetable, num, type):
    if type == "packets":
        print(f"{vegetable} seeds: {num} packets available")
    elif type == "grams":
        print(f"{vegetable} seeds: {num} grams total")
    elif type == "area":
        print(f"{vegetable} seeds: covers {num} square meters")
    else:
        print("Unknown unit type")
    