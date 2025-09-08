from bisect import bisect


class calc:
    def __init__(self,a,b,relationship):
        self.a=a
        self.b=b
        self.relationship=relationship

    def summ(self):
        return self.a+self.b
    def subscration(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        if self.a > 0 and self.b > 0:
            return self.a/self.b

test1 = calc(10,5,'+')
test2 = calc(1337,337,'-')
test3 = calc(8,10,'*')
test4 = calc(400,200,'/')
lst = [test1,test2,test3,test4]
for i in lst:
    print(i.summ(),i.subscration(),i.multiplication(),i.division())

