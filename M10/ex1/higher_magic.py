from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return cast_all


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)

    def fireball_with_power(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    original_power = 10
    amplified = power_amplifier(fireball_with_power, 3)
    print(f"Original: {original_power}, Amplified: {original_power * 3}")

    print("Testing conditional caster...")
    is_strong = lambda target, power: power >= 20
    conditional = conditional_caster(is_strong, fireball)
    print(conditional("Dragon", 5))
    print(conditional("Dragon", 25))

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    results = sequence("Goblin", 15)
    for r in results:
        print(r)
