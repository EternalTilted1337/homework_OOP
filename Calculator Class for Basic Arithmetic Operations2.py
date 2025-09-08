
class calc:
    def summ(self,a,b):#+
        return a + b
    def subscration(self,a,b):#-
        return a - b
    def multiplication(self,a,b):#*
        return a * b
    def division(self,a,b):#/
        if a != 0 and b != 0:
            return a / b
        else:
            return ('Division by zero')
    def construction(self,a,b):
        return a ** b

Calculator = calc()
test1 = Calculator.summ(10,10)
test2 = Calculator.subscration(666,333)
test3 = Calculator.multiplication(10,10)
test4 = Calculator.division(666,2)
test5 = Calculator.construction(5,5)


print(f'10 + 10 = {test1}')
print(f'666 - 333 = {test2}')
print(f'10 * 10 = {test3}')
print(f'666 : 2 = {test4}')
print(f'5 ** 5 = {test5}')

