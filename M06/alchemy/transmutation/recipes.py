def lead_to_gold():
    import alchemy
    from elements import create_fire
    return (
        f"Recipe transmuting Lead to gold: brew '{alchemy.create_air()}' "
        f"and '{alchemy.strength_potion()}' mixed with '{create_fire()}' "
    )
