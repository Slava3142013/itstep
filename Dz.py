# 1 завдання
#class Tvarina:

 #   def __init__(self, name, age):
#        self.name = name
#        self.age = age

 #   def make_sound(self):
 #       pass

#    def info(self):
 #       return f"Ім'я: {self.name}, Вік: {self.age} років"


#class Sobaka(Tvarina):
#    def make_sound(self):
#        return "Гав-гав!"


#class Kit(Tvarina):
#    def make_sound(self):
#        return "Мяу-мяу!"


#sobaka = Sobaka("Рекс", 3)
#kit = Kit("Мурчик", 2)

#print(sobaka.info(), "-", sobaka.make_sound())
#print(kit.info(), "-", kit.make_sound())


# 2 завдання

class TransportnyiZasib:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Рухається зі швидкістю {self.speed} км/год"


class Avto(TransportnyiZasib):
    def move(self):
        return f"Автомобіль їде зі швидкістю {self.speed} км/год"


class Litak(TransportnyiZasib):
    def move(self):
        return f"Літак летить зі швидкістю {self.speed} км/год"


class Korabel(TransportnyiZasib):
    def move(self):
        return f"Корабель пливе зі швидкістю {self.speed} км/год"


avto = Avto(120)
litak = Litak(800)
korabel = Korabel(40)

print(avto.move())
print(litak.move())
print(korabel.move())
