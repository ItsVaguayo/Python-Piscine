class GardenError(Exception):
    pass


class SunError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:

    def __init__(self, name: str, water: int, sunlight_hours: int) -> None:
        self.name: str = name
        self.water: int = water
        self.sunlight_hours: int = sunlight_hours


class GardenManager:

    def __init__(self, name: str) -> None:
        """Initialize a Garden instance."""
        self.owner: str = name
        self.plants: list[Plant] = []
        self.total_grow: int = 0
        self.total_plants: int = 0

    def add_plant(self, plant: Plant) -> None:
        if plant.name is None:
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        self.plants.append(plant)
        self.total_plants += 1
        print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        for plant in self.plants:
            print(f"Watering {plant.name} - success")
            plant.water += 1
        print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        for plant in self.plants:
            if plant.water > 10:
                raise WaterError(f"Error checking {plant.name}: "
                                 f"Water level {plant.water} is too high "
                                 f"(max 10)")
            elif plant.water < 1:
                raise WaterError(f"Error checking {plant.name}: "
                                 f"water level {plant.water} is too low "
                                 f"(min 1)")
            elif plant.sunlight_hours > 12:
                raise SunError(f"Error: Sunlight hours "
                               f"{plant.sunlight_hours} is too high "
                               f"(max 12)")
            elif plant.sunlight_hours < 2:
                raise SunError(f"Error: Sunlight hours "
                               f"{plant.sunlight_hours} is too low (min 2)")
            else:
                print(f"Plant {plant.name}: healthy "
                      f"(water: {plant.water}, sun: {plant.sunlight_hours})")

    @staticmethod
    def check_tank(tank_status):
        if tank_status == "empty":
            raise WaterError("Caught GardenError: "
                             "Not enough water in the tank")


def test_garden_management():
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    garden = GardenManager("Victor")
    try:
        garden.add_plant(Plant("tomato", 4, 8))
        garden.add_plant(Plant("lettuce", 14, 8))
        garden.add_plant(Plant(None, 5, 5))
    except ValueError as e:
        print(e)
    print("\nwatering plants...")
    garden.water_plants()
    print("\nTesting plant health...")
    try:
        garden.check_plant_health()
    except (WaterError, SunError) as e:
        print(e)
    print("\nTesting error recovery...")
    try:
        garden.check_tank("empty")
    except WaterError as e:
        print(e)
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
