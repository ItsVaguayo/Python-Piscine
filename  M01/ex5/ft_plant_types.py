class Plant:
    """A base class representing a plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        """Print the plant's basic information."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


class Flower(Plant):
    """A class representing a flowering plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Display a message indicating the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """A class representing a tree."""

    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and display the shade area provided by the tree."""
        print(f"{self.name} provides {int(self.diameter * 1.56)} square"
              " meters of shade")


class Vegetable(Plant):
    """A class representing a vegetable plant."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutricional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutricional: str = nutricional_value


def ft_plant_types() -> None:
    """Demonstrate different plant types and their behaviors."""
    data_plants: list[Plant] = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 45, "white"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 700, 1950, 100),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Cucumber", 80, 90, "fall", "magnesium"),
    ]
    print("=== Garden Plant Types ===")

    for plant in data_plants:
        print(
            f"\n{plant.name} ({plant.__class__.__name__}): "
            f"{plant.height}cm, {plant.age} days", end="")
        if plant.__class__.__name__ == "Flower":
            print(f", {plant.color} color")
            plant.bloom()
        elif plant.__class__.__name__ == "Tree":
            print(f", {plant.diameter}cm diameter")
            plant.produce_shade()
        elif plant.__class__.__name__ == "Vegetable":
            print(f", {plant.harvest_season} harvest")
            print(f"{plant.name} is rich in {plant.nutricional}")


if __name__ == "__main__":
    ft_plant_types()
