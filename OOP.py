class Car:
    count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.count += 1

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


car1 = Car("Toyota", "Camry", 2020)
print(car1.get_info())

make = input("Марка: ")
model = input("Модель: ")
year = int(input("Рік: "))
car2 = Car(make, model, year)
print(car2.get_info())


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Заробітна плата {self.name}: {self.salary}"

    def __bool__(self):
        return self.salary > 0


e1 = Employee("Олег", "Менеджер", 50000)
print(e1)

e2 = Employee("Анна", "Інженер", 60000)
print(str(e2))
print(bool(e1))
print(e2.__bool__())