from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    creatures = []
    for factory, strategy in opponents:
        creatures.append((factory.create_base(), strategy))
    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature_a, strategy_a = creatures[i]
            creature_b, strategy_b = creatures[j]
            print("\n* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive),"
          " (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])
