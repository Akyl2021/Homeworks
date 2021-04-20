
#Complex
# 1) magic method (+, -, /, *)
# 2) return Complex ->
# complex2 = Complex(2, 5)
# complex3 = complex1 + complex2
# 3) __str__

class Complex:

    def __init__(self, real = 0, in = 0):
           self.real = real
           self.in = 
#
#     def __add__(self, other):
#             num = self.num * other.denum + other.num * self.denum
#             denum = self.denum * other.denum
def comp(self):
#       return self.
#             print(num)
#             print("-")
#             print(denum)
#
#
x = complex(1, 2)
print(x)

#z = x + y
#print(z)





















# class Fraction:
#
#     def __init__(self, num, denum):
#         if denum == 0:
#             raise ValueError('Denominator cant 0!')
#         self.num = num
#         self.denum = denum
#
#     def add(self, other):
#             num = self.num * other.denum + other.num * self.denum
#             denum = self.denum * other.denum
#             print(num)
#             print("-")
#             print(denum)
#
#
# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(1, 8)
# fraction1.add(fraction2)

# class Human:
#
#    def __init__ (self, name, weight, height):
#       self.name = name
#       self.height = height
#       self.weight = weight
#
#    def run(self):
#       return self.height / 10
#
#    def eat(self):
#       return self.weight / 10
#
# human = Human('Manas', 61, 175)
#
# print(human.name)
# print(human.weight)
# print(human.height)
# print(human.run())
# print(human.eat())
#
# human2 = Human('Adilet', 110, 150)
# print()
# print(human2.name)
# print(human2.weight)
# print(human2.height)
# print(human2.run())
# print(human2.eat())
#






#
# class Human:
#     def __init__(self, skin_color, name, language):
#         self.skin_color = skin_color
#         self.name = name
#         self.language = language
#
#     def eat(self):
#         return f"{self.name},im eating"
#
# class Russian(Human):
#     def __init__(self, skin_color, name, language, bath):
#         super(Russian, self).__init__(skin_color,name,language)
#         self.bath = bath
# class Kyrgyz:
#     def __init__(self, skin_color, name, language, revolution):
#         self.skin_color = skin_color
#         self.name = name
#         self.language = language
#         self.revolution = revolution
#
# class American:
#     def __init__(self, skin_color, name, language, food):
#         self.skin_color = skin_color
#         self.name = name
#         self.language = language
#         self.food = food
#
#
# russian = Russian('white', "wanya", "rus", 'wooden')
# print(russian.name)
# print(russian.eat())
#
#
# class Animal:
#
#     def __init__(self, eyes, tongue, ears):
#         self.eyes = eyes
#         self.tongue = tongue
#         self.ears = ears

    # def run(self):
    #     return f"Run ->"
#
#     def eat(self):
#         return "Eat"
#
#
# class Donkey(Animal):
#
#     def __init__(self, eyes, tongue, ears, tail):
#         super(Donkey, self).__init__(eyes, tongue, ears)
#         self.tail = tail
#
#     def run(self):
#         return "Run <- Donkey"
#
#     def eat(self):
#         return "Eat Grass"
#
#
# class Eshek(Donkey):
#
#     def __init__(self, eyes, tongue, ears, tail, stamina):
#         super(Eshek, self).__init__(eyes, tongue, ears, tail)
#         self.stamina = stamina
#
#     # def run(self):
#     #     return "Run gallop Eshek"
#
#
# class Osyol(Donkey):
#
#     def __init__(self, eyes, tongue, ears, tail, stubborn):
#         super(Osyol, self).__init__(eyes, tongue, ears, tail)
#         self.stubborn = stubborn
#
#     def run(self):
#         return "Run zigzag Osyol"
#
#     def scream(self):
#         return "Scream"
#
#
# donkey = Donkey("big", "long", "big", "short")
# print(donkey.run())
# print(donkey.eat())
#
# osyol = Osyol("big", "long", "big", "short", True)
# print(osyol.run())
# print(osyol.eat())