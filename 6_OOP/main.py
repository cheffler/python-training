class User():
    def sign_in(self):
        print(f'{self._name} logged in')


class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f"atticking with power of {self._power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        print(f"atticking with arrows, number arrows left {self._num_arrows}")


wizard1 = Wizard('Merlin', 100)
wizard1.sign_in()

print(isinstance(wizard1, object))
