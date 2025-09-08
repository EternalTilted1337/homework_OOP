class Car:
    def __init__(self,marka,class_auto,ves,driver,engine):
        self.marka=marka
        self.class_auto=class_auto
        self.ves=ves
        self.driver=driver
        self.engine=engine

    def start(self):
        print('Поехали')

    def stop(self):
        print('Останавливаемся')

    def turnRight(self):
        print('Поворот направо')

    def turnLeft(self):
        print('Поворот налево')

    def toString(self):
        return f'''
               Характеристики Автомобиля:
               Марка = {self.marka}
               Класс авто = {self.class_auto}
               Вес автомобиля = {self.ves}
               
               Характеристики мотора:
               Сила = {self.engine.power}
               Производитель = {self.engine.proizvoditel}
               
               Информация о водителе:
               ФИО : {self.driver.FIO}
               Стаж вождения = {self.driver.staj}'''


class Person:#Человек
    def __init__(self,FIO):
        self.FIO = FIO

class Driver(Person):#Человек <- Водитель
    def __init__(self,FIO,staj):
        super().__init__(FIO)#Что бы достучаться везде. Бот посоветовал так, но я изначально написал self
        self.staj = staj


class Engine:
    def __init__(self,power,proizvoditel):
        self.power=power
        self.proizvoditel=proizvoditel


class Lorry(Car):
    def __init__(self, marka, class_auto, ves, driver, engine, carrying_capacity):
        super().__init__(marka,class_auto,ves,driver,engine)
        self.carrying_capacity=carrying_capacity

    def toString(self):
        return super().toString() + f'Грузоподъёмность = {self.carrying_capacity}'

class SportCar(Car):
    def __init__(self,marka,class_auto,ves,driver,engine,max_speed):
        super().__init__(marka,class_auto,ves,driver,engine)
        self.max_speed=max_speed

    def toString(self):
        return super().toString() + f'Предельная скорость = {self.max_speed}'

#Тест тоже бот прописал :)
# if __name__ == "__main__":
#     driver = Driver("Иван Иванов", 5)
#     engine = Engine(200, "Toyota")
#     car = Car("Toyota", "Седан", 1500, driver, engine)
#     lorry = Lorry("Volvo", "Грузовик", 5000, driver, engine, 10000)
#     sportcar = SportCar("Ferrari", "Спорткар", 1200, driver, engine, 300)
#
#     print(car.toString())
#     print("\n" + "="*20 + "\n")
#     print(lorry.toString())
#     print("\n" + "="*20 + "\n")
#     print(sportcar.toString())


