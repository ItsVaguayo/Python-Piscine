class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0

    def get_info(self):
        print(f"Created: {self.name} ({self.__height}cm, {self.__age} days)")

    @property
    def get_height(self):
        return self.__height

    @property
    def get_age(self):
        return self.__age

    @get_height.setter
    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    @get_age.setter
    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")


def ft_garden_security():
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
