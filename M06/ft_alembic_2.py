
def alembic_2() -> None:
    import alchemy.elements
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:", alchemy.elements.create_earth())


if __name__ == "__main__":
    alembic_2()
