class User():
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def sign_in(self):
        print(f'{self._name} logged in')

    def attack(self):
        print(f'{self._name} has no attack ability')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(name, email)
        self._power = power

    def attack(self):
        print(f"attacking with power of {self._power}")


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(name, email)
        self._num_arrows = num_arrows

    # def attack(self):
    #     print(f"atticking with arrows, number arrows left {self._num_arrows}")


legolas = Archer('Legolas', 40, 'bows@arrows.com')
merlin = Wizard('Merlin', 100, 'staff@magic.com')
merlin.sign_in()

merlin.attack()
legolas.attack()
