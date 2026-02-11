class SecurePlant:
    """A class representing a plant with secure height and age attributes."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0

    def get_info(self) -> None:
        """Print the plant's basic information."""
        print(f"Created: {self.name} ({self.__height}cm, {self.__age} days)")

    @property
    def get_height(self) -> int:
        """Get the plant's height."""
        return self.__height

    @property
    def get_age(self) -> int:
        """Get the plant's age."""
        return self.__age

    @get_height.setter
    def set_height(self, height: int) -> None:
        """Set the plant's height with validation."""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    @get_age.setter
    def set_age(self, age: int) -> None:
        """Set the plant's age with validation."""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")


def ft_garden_security() -> None:
    """Demonstrate the garden security system
    with validated plant attributes."""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height = 25
    rose.set_age = 30
    rose.set_height = -5
    print()
    print(
        f"Current plant: {rose.name}"
        f"({rose.get_height}cm, {rose.get_age} days)")


if __name__ == "__main__":
    ft_garden_security()
