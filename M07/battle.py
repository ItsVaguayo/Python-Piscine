from ex0 import FlameFactory, AquaFactory
from ex0.factories import CreatureFactory
from ex0.creature import Creature


def fabric_checker(factory: CreatureFactory) -> None:
    print("Testing factory")
    creature: Creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    creature = factory.create_evolved()
    print(creature.describe())
    print(creature.attack(), "\n")


def battle_cheker(
        factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    creature1: Creature = factory1.create_base()
    creature2: Creature = factory1.create_base()
    print("Testing battle")
    print(creature1.describe(), "\nvs.\n", creature2.describe())
    print(" Fight!\n", creature1.attack(), "\n", creature2.attack())


if __name__ == "__main__":
    fabric_checker(FlameFactory())
    fabric_checker(AquaFactory())
    battle_cheker(FlameFactory(), AquaFactory())
