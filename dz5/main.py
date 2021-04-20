
# Написать функцию которая принимает числа, выводит сумму чисел. Функцию надо вызвать.

def numbers(x):
    a = 30
    b = 25
    c = 15
    print(x + a + b + c)


numbers(10)


# Написать функцию которая принимает числа, выводит разность чисел. Функцию надо вызвать.

def numbers(x):
    a = 30
    b = 25
    c = 15
    print(x - a - b - c)


numbers(100)


# Написать функцию которая принимает числа, выводит произведение чисел. Функцию надо вызвать.

def numbers(x):
    a = 30
    b = 25
    c = 15
    print(x * a * b * c)


numbers(5)


# Написать функцию которая принимает числа, выводит деление чисел. Функцию надо вызвать.

def numbers(x):
    a = 90
    b = 3

    print(a / b / x)


numbers(2)

# Написать функцию которая принемает массив, проходится по циклом по массиву и печатает объекты массива. Функцию надо вызвать.

arr = ["Tom", "Sam", "Katy", "Jhon", "Hank"]


def a():
    for gab in arr:
        print(gab)


a()

# Напишите приммеры использования всех операций с массивами
#считает по элементам
jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
print(len(jeno))

#добавляет в элемент в конец
jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
jeno.append('Kano')
print(jeno)

#очищает
jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
jeno.clear()
print(jeno)

#считает одинаковые элементы
third = [7, 2, 7, 4, 5, 6, 7, 8, 9, 770]
print(third.count(7))

#копирует
third = [7, 2, 7, 4, 5, 6, 7, 8, 9, 770]
third1 = third.copy()
print(third)
print(third1)

#соединяет
jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
third = [7, 2, 7, 4, 5, 6, 7, 8, 9, 770]
jeno.extend(third)
print(jeno)

#выводит индекс элемента
jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
print(jeno.index('Hank'))

#удаляет указанный элемент
jeno = ["Tom", "Sam", "Katy",'Meder', "Jhon", "Hank"]
jeno.remove('Meder')
print(jeno)

#выводит элементы в обратном порядке
third = [7, 2, 7, 4, 5, 6, 7, 8, 9, 770]
third.reverse()
print(third)

#удаление по индексу
jeno = ["Tom", "Sam", "Katy",'Meder', "Jhon", "Hank"]
jeno.pop(3)
print(jeno)

print('------------------------------------------------')

# Оберните все операции в функции, которые принимают масссив и выполняют над нимм операцию. Функцию надо вызвать.

jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
def kata():
    print(len(jeno))

kata()

jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
jeno.append('Kano')
def kata():
    print(jeno)

kata()

jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
jeno.clear()
def kata():
    print(jeno)

kata()


third = [7, 2, 7, 4, 5, 6, 7, 8, 9, 770]
def kata():
    print(third.count(7))

kata()


third = [7, 2, 7, 4, 5, 6, 7, 8, 9, 770]
third1 = third.copy()
def kata():
    print(third)
    print(third1)

kata()


jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
third = [7, 2, 7, 4, 5, 6, 7, 8, 9, 770]
jeno.extend(third)
def kata():
    print(jeno)

kata()

jeno = ["Tom", "Sam", "Katy", "Jhon", "Hank"]
def kata():
    print(jeno.index('Hank'))
kata()

jeno = ["Tom", "Sam", "Katy",'Meder', "Jhon", "Hank"]
jeno.remove('Meder')
def kata():
    print(jeno)
kata()

third = [7, 2, 7, 4, 5, 6, 7, 8, 9, 770]
third.reverse()
def kata():
    print(third)
kata()

jeno = ["Tom", "Sam", "Katy",'Meder', "Jhon", "Hank"]
jeno.pop(3)
def kata():
    print(jeno)
kata()
