class Human:
    count=0
    def __init__(self,name= 'Петя'):
        self.name=name
        Human.count+=1
class Auto:
            def __init__(self,brand):
                self.brand=brand
                self.passenger=[]
            def add(self,*pas):
                for p in pas:
                    self.passenger.append(p)
            def info(self):
                if self.passenger==[]:
                    print('Маршрутка бренду',self.brand,'немає пасажирів')
                else:
                    print('Маршрутка бренду', self.brand, 'має пасажирів')
                    for p in self.passenger:
                        print(p.name)

pas1=Human()
pas2=Human('Таня')
pas3 = Human('Саша')
car=Auto('Богдан')
#car.add(pas1)
#car.add(pas2)
#car.add(pas3)
car.add(pas1,pas2,pas3)
car.info()
print('Кіл пасажирів:',Human.count)