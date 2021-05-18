# OOP
# Wizard game

class PlayerCharacter:
    # Class Object Attribute (for all instances)
    membership = True

    def __init__(self, name, age) -> None:
        # like JS, convetion is to use _ for private,
        # no builtin private variables
        self._name = name
        self._age = age

    def run(self):
        print(f"{self._name} is running")

    @classmethod
    def adding_things(cls, num1, num2):
        # can create instances of the class using cls
        return cls('default', num1+num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1+num2


player1 = PlayerCharacter('Harry')
player1.run()

print(PlayerCharacter.adding_things(2, 3))
