from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability
from ex0.factory import CreatureFactory
from ex0.creature import Creature


def factory_checker(factory: CreatureFactory) -> None:
    base: Creature = factory.create_base()
    if isinstance(base, HealCapability):
        print("\nTesting Creature with healing capability")
    elif isinstance(base, TransformCapability):
        print("\nTesting Creature with transform capability")

    print("base:")
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())
    elif isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print("\nevolved:")
    evolved: Creature = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())
    elif isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    factory_checker(HealingCreatureFactory())
    factory_checker(TransformCreatureFactory())
