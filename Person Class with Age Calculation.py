from datetime import date

class person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

first = person('Misha','Russia',date(2001,12,16))
second = person('Alice','USA',date(1987,1,30))
third = person('Bob','Germany',date(1999,5,17))

people = [first, second, third]
for person in people:
    print(person.name, person.country, person.age())

