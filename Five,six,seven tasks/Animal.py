from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def makeNoise(self):#Звук животных
        pass

    @abstractmethod
    def eat(self):#шо жрет
        pass

    @abstractmethod
    def getDescription(self):#описание животного
        pass

class Dog(Animal):
    def makeNoise(self):#Звук животных
        print(f'{self.name} Гав-Гав!')
    def eat(self):#шо жрет
        print(f'{self.name} ест кости и мясо')
    def getDescription(self):#описание животного
        return "Собака верный друг человека"


class Cat(Animal):
    def makeNoise(self):  # Звук животных
        print(f'{self.name} Мяу-Мяу')

    def eat(self):  # шо жрет
        print(f'{self.name} ест рыбу и мясо')

    def getDescription(self):  # описание животного
        return "Кошка ловит мышей"


class Bear(Animal):
    def makeNoise(self):  # Звук животных
        print(f'{self.name} Р-Р-Р')

    def eat(self):  # шо жрет
        print(f'{self.name} ест ягоды, обожает мёд и людей')

    def getDescription(self):  # описание животного
       return "Суровый ми-ми-Мишка"

class Veterinarian:
    def treat_animal(self,animal:Animal) -> None:
        print(f'На прием пришел - {animal.name}')
        print(f'Описание: {animal.getDescription()}')

vet = Veterinarian()
dog = Dog('Шарик')
cat = Cat('Мурка')
bear = Bear('Мишаня')
vet.treat_animal(dog)
vet.treat_animal(dog)
vet.treat_animal(cat)
vet.treat_animal(bear)

