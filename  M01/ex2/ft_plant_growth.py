class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self, day):
        print(f"=== Day {day + 1} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, grow_multiplicator, days):
        tempheight = self.height
        self.get_info(0)
        for i in range(1, days + 1):
            self.update_age()
            self.height = self.height + (1 * grow_multiplicator)
        self.get_info(days)
        print(f"Growth this week: +{self.height - tempheight}cm")

    def update_age(self):
        self.age = self.age + 1


def ft_plant_growth(flower, grown_multiplicator):
    simulate_days = 6
    flower.grow(grown_multiplicator, simulate_days)


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    ft_plant_growth(rose, 1)
