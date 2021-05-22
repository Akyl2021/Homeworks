 # Сделать класс Fraction который будет имитировать дробь и ее атрибутами и методоми add, divide, multiply,
# substract которые принимают объект такого же класса Fraction
# (Что бы использовать атрибуты класса)

class Fraction:

    def __init__(self, num, denum):
        self.num = num
        if denum == 0:
            raise ValueError("denumenator can't 0")
        self.denum = denum

    def __add__(self, other):
        num = self.num * other.denum + self.denum * other.num
        denum = self. denum * other.denum

        print(num)
        print("-")
        print(denum)


    def multiply(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum

        print(num)
        print("-")
        print(denum)


    def divide(self, other):
        num = self.num * other.denum
        denum = self.denum * other.num

        print(num)
        print("-")
        print(denum)

    def substract(self, other):
        num = self.num - other.denum
        denum = self.denum
        if denum != other.denum:
            print("Ошибка: привести к общему знаминателью")
        print(num)
        print("-")
        print(denum)
f1 = Fraction(6, 8)
f2 = Fraction(5, 7)
f1 + f2
print("-------------")
f1.multiply(f2)
print("-------------------")
f1.divide(f2)
print("-----------")
f1.substract(f2)

