 #Сделать класс fraction тоесть взять из математики дробь и сделать её альтернативу в python, с аттрибутами и методами.
# Методы должны правильно считать дробь к дроби. К примеру
#fraction1.add(fraction2)
#тоесть дробь в методах принимает 1 экземпляр дроби и делает красивый принт результата.
#
class Fraction:

    def __init__(self, num, denum):
        if denum == 0:
            raise ValueError("Denominator can't 0!")
        self.num = num
        self.denum = denum

    def __add__(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

    def __truediv__(self, other):
        num = self.num / other.denum
        denum = self.denum / other.num
        print(num)
        print("-")
        print(denum)

    def __mul__(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

    def __sub__(self, other):
        num = self.num - other.num
        denum = self.denum - other.denum
        print(num)
        print("-")
        print(denum)

    def __len__(self):
        return 1

    def __str__(self):
        return f"{self.num}\n-\n{self.denum}"


fraction1 = Fraction(2, 8)
fraction2 = Fraction(1, 4)
fraction1 + fraction2
print('+++++++++++++')
fraction1 / fraction2
print('/////////////')
fraction1 * fraction2
print('*************')
