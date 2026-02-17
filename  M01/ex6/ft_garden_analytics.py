
class Plant:
    """
    A class representing a plant in the garden.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
    """

    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant instance."""
        self.name: str = name
        self.height: int = height


class FloweringPlant(Plant):
    """
    A class representing a flowering plant in the garden.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        color (str): The color of the flowers.
    """

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a FloweringPlant instance."""
        super().__init__(name, height)
        self.color: str = color


class PrizeFlower(FloweringPlant):
    """
    A class representing a prize-winning flower in the garden.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        color (str): The color of the flowers.
        price (int): The prize points awarded for this flower.
    """

    def __init__(self, name: str, height: int,
                 color: str, price: int) -> None:
        """Initialize a PrizeFlower instance."""
        super().__init__(name, height, color)
        self.price: int = price


class Garden:
    """
    A class representing a garden owned by a gardener.

    Attributes:
        owner (str): The name of the garden owner.
        plants (list[Plant]): List of plants in the garden.
        total_grow (int): Total growth accumulated in the garden.
        total_plants (int): Total number of plants added to the garden.
    """

    def __init__(self, name: str) -> None:
        """Initialize a Garden instance."""
        self.owner: str = name
        self.plants: list[Plant] = []
        self.total_grow: int = 0
        self.total_plants: int = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden and update the total plant count."""
        self.plants.append(plant)
        self.total_plants += 1
        if self.owner == "Alice":
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_plants(self, amount: int) -> None:
        """Simulate the growth of all plants in the garden."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.height += amount
            self.total_grow += amount
            print(f"{plant.name} grew {amount}cm")


class GardenManager:
    """
    A class for managing multiple gardens and analyzing their statistics.

    Attributes:
        gardens (dict[str, Garden]): Dictionary mapping owner names to gardens.
    """

    def __init__(self) -> None:
        """Initialize a GardenManager instance with an empty gardens dict."""
        self.gardens: dict[str, Garden] = {}

    class GardenStats:
        """
        A nested class for analyzing and reporting on garden statistics.

        Attributes:
            manager (GardenManager): Reference to the parent GardenManager.
        """

        def __init__(self, manager: GardenManager) -> None:
            """Initialize the GardenStats with a reference to the
            GardenManager."""
            self.manager: GardenManager = manager

        def calculate_score(self) -> dict[str, int]:
            """Calculate scores for all gardens based on plant types
            and growth."""
            scores: dict[str, int] = {}
            for owner, garden in self.manager.gardens.items():
                amount: int = 0
                for plant in garden.plants:
                    amount += plant.height
                    amount += 10
                    if isinstance(plant, PrizeFlower):
                        amount += plant.price
                scores[owner] = amount
            return scores

        def garden_info(self, owner: str) -> None:
            """Print a detailed report of a garden's plants and statistics."""
            garden: Garden = self.manager.gardens[owner]
            print(f"\n=== {garden.owner}'s Garden Report ===")
            print("Plants in garden:")
            types: dict[str, int] = {"regular": 0, "flowering": 0, "prize": 0}
            for flower in garden.plants:
                if isinstance(flower, PrizeFlower):
                    print(
                        f"- {flower.name}: {flower.height}cm,"
                        f" {flower.color} flowers (blooming),"
                        f" Prize points: {flower.price}"
                    )
                    types["prize"] += 1
                elif isinstance(flower, FloweringPlant):
                    print(
                        f"- {flower.name}: {flower.height}cm,"
                        f" {flower.color} flowers (blooming)"
                    )
                    types["flowering"] += 1
                elif isinstance(flower, Plant):
                    print(f"- {flower.name}: {flower.height}cm")
                    types["regular"] += 1
            print(
                f"\nPlants added: {garden.total_plants},"
                f" Total growth: {garden.total_grow}cm"
            )
            print(
                f"Plant types: {types['regular']} regular,"
                f" {types['flowering']} flowering,"
                f" {types['prize']} prize flowers"
            )

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> GardenManager:
        """Factory method that creates a manager with gardens
        for given owners."""
        manager: GardenManager = cls()
        for owner in owners:
            manager.gardens[owner] = Garden(owner)
        return manager

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate that the height of a plant is a positive number."""
        return height > 0

    @staticmethod
    def ft_len(s: str) -> int:
        """Calculate the length of a string without using built-in len()."""
        count: int = 0
        for _ in s:
            count += 1
        return count


def ft_garden_analytics() -> None:
    """
    Demonstrate the Garden Management System functionality.

    Creates a garden network, adds plants, grows them, and displays
    statistics and validation results.
    """
    print("=== Garden Management System Demo ===\n")
    owners: list[str] = ["Alice", "Bob"]
    manager: GardenManager = GardenManager.create_garden_network(owners)
    alice: Garden = manager.gardens["Alice"]
    bob: Garden = manager.gardens["Bob"]
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    bob.add_plant(Plant("Small Oak", 40))
    bob.add_plant(Plant("Mini Rose", 32))
    print()
    alice.grow_plants(1)
    manager.GardenStats(manager).garden_info("Alice")
    print("\nHeight validation test:", manager.validate_height(10))
    score = manager.GardenStats(manager).calculate_score()
    print(f"Garden score - Alice: {score["Alice"]}, Bob: {score["Bob"]}")
    print("Total gardens managed:", manager.ft_len(owners))


if __name__ == "__main__":
    ft_garden_analytics()
