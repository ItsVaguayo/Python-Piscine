def healing_potion() -> str:
    from alchemy.elements import create_earth, create_air

    return (
        f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    from elements import create_fire, create_water

    return (
        f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
    )
