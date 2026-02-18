import sys
def ft_inventory_system():
    args = sys.argv[1:]
    inventory = {item: int(count) for arg in args for item,
                 count in [arg.split(':')]}
    total_items = sum(inventory.values())
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
if __name__ == "__main__":
    ft_inventory_system()