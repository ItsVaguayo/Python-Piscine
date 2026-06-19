def distillation_1():
    from alchemy import strength_potion, healing_potion as heal
    print("=== Distillation 1 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion:", strength_potion())
    print("Testing heal alias:", heal())


if __name__ == "__main__":
    distillation_1()
