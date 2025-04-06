class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = max(0, health)

    def attack(self):
        pass

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)

    def is_alive(self):
        return self.__health > 0

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150)

    def attack(self):
        return f"{self.get_name()} атакує мечем!"

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80)

    def attack(self):
        return f"{self.get_name()} атакує магією!"