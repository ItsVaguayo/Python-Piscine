import sys


def ft_inventory_system() -> None:
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {
        item: int(count) for arg in args
        for item, count in [arg.split(':')]
    }
    total_items: int = sum(inventory.values())
    print("Total items in inventory:", total_items)
    print("Unique item types:", len(inventory))
    print("\n=== Current Inventory ===")
    for item, count in inventory.items():
        print(f"{item}: {count} units ({(count / total_items)
              * 100:.2f}%)")
    print("\n=== Inventory Statistics ===")
    for item, value in inventory.items():
        if value == max(inventory.values()):
            print(f"Most abundant: {item} ({value} units)")
        if value == min(inventory.values()):
            print(f"Least abundant: {item} ({value} units)")
    print("\n=== Items categories ===")
    categories: dict[str, dict[str, int]] = {
        "Abundant": {}, "Moderate": {}, "Scarce": {}
    }
    for item, count in inventory.items():
        if count > 10:
            categories["Abundant"][item] = count
        elif count > 3:
            categories["Moderate"][item] = count
        else:
            categories["Scarce"][item] = count
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")
    restock: list[str] = [
        item for item, value in categories["Scarce"].items()
        if value == 1
    ]
    print("\n=== Management Suggestions ===")
    print("Restock needed:", *restock, sep=", ")
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys:", *inventory.keys(), sep=", ")
    print("Dictionary values:", *inventory.values(), sep=", ")
    print("Sample lookup - 'sword' in inventory:",
          bool(inventory.get("sword")))
    #   print(", ".join(restock))


if __name__ == "__main__":
    ft_inventory_system()
