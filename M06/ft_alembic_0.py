
def alembic_0() -> None:
    import elements
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print("Testing create_fire:", elements.create_fire(), "\n")


if __name__ == "__main__":
    alembic_0()
