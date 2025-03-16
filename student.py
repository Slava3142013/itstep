import random as r
class Student:

    def __init__(self,name='Slava'):
        self.name=name
        self.happy=r.randint(50,100)
        self.progress=r.randint(1,12)
        self.isStudy=True
     def study(self):
         print('Час для навчання')
        self.happy-=r.randint(10,50)
        self.progress+=r.randint(1,5)
    def chiil(self)
st1=Student()
print(st1.happy)