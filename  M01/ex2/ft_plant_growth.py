class Plant:
    """A class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self, day: int) -> None:
        """Print the current information of the plant."""
        print(f"=== Day {day + 1} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, grow_multiplicator: int, days: int) -> None:
        """Simulate the growth of the plant over a given number of days."""
        tempheight: int = self.height
        self.get_info(0)
        for _ in range(1, days + 1):
            self.update_age()
            self.height = self.height + (1 * grow_multiplicator)
        self.get_info(days)
        print(f"Growth this week: +{self.height - tempheight}cm")

    def update_age(self) -> None:
        """Increment the age of the plant by one day."""
        self.age = self.age + 1


def ft_plant_growth(flower: Plant, grown_multiplicator: int) -> None:
    """This function simulates the growth of a plant over a week."""
    simulate_days: int = 6
    flower.grow(grown_multiplicator, simulate_days)


rose: Plant = Plant("Rose", 25, 30)
sunflower: Plant = Plant("Sunflower", 80, 45)
cactus: Plant = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    ft_plant_growth(rose, 1)
