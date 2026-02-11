class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        """Print the information of the plant."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory(data_plants: tuple) -> None:
    """This function creates Plant instances from a list of
    plant data and prints their information."""
    my_plants = []
    count = 0
    for flower in data_plants:
        my_plants.append(Plant(*flower))
    print("=== Plant Factory Output ===")
    for x in my_plants:
        x.get_info()
        count += 1
    print("Total plants created:", count)


data_plants: tuple = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
    ]

if __name__ == "__main__":
    ft_plant_factory(data_plants)
