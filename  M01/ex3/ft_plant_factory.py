class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory(data_plants):
    my_plants = []
    count = 0
    for flower in data_plants:
        my_plants.append(Plant(*flower))
    print("=== Plant Factory Output ===")
    for x in my_plants:
        x.get_info()
        count += 1
    print("Total plants created:", count)


data_plants = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
    ]

if __name__ == "__main__":
    ft_plant_factory(data_plants)
