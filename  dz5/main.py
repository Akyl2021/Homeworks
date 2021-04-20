# Создайте массив состоящий из словарей с данными
gara = [{
    'kostum' : 'Armani',
    'rubashka' : 'Gucci'},
{   'tufli' : 3000,
    'galstuk': 1500,
    'remen' : 2000
}]

# Напишите функцию которая принимает ранее созданный массив, фильтрирует
gara = [{
    'kostum' : 'Armani',
    'rubashka' : 'Gucci'},
{   'kostum' : 'VLKSM',
    'rubashka' : 'Fabric'
}]
def noby(vewi):
    for pinf in vewi:
        if pinf['kostum'] == 'Armani':
            print('--------Отличный бренд', pinf['kostum'],'--------')
        else:
            print('--------Так себе бренд.--------')
noby(gara)

# полученный массив и возвращающий не менне двух элементов из массива
array = [ 0, 1, 2, 3, 4, 5, 6, 12, 15, 18]
def funkziya(massiv):
    return massiv

funkziya(array)

first = funkziya(array[3])
second = funkziya(array[6])
third = funkziya(array[9])

print(first)
print(second)
print(third)

# Напишите функцию которая принимает отфильтрованные данные, добавляет
gara = [{
    'kostum' : 'Armani',
    'rubashka' : 'Gucci'},
{   'kostum' : 'VLKSM',
    'rubashka' : 'Fabric'
}]
def filtr(vewi):
    for pinf in vewi:
        if pinf['kostum'] == 'Armani':
            print('--------Отличный бренд', pinf['kostum'],'--------')
            pinf['Качество соответствует!'] = True
        else:
            print('--------Так себе бренд.--------')
filtr(gara)
print(gara)

# новое значение каждому из элементов отфильтрованных данных и возвращает
gara = [{
    'kostum' : 'Boggi',
    'rubashka' : 'Prada'},
{   'kostum' : 'Dior',
    'rubashka' : 'Polo'
}]
def filtr(vewi):
    for pinf in vewi:
        if pinf['kostum'] == 'Boggi':
            print('--------Италия', pinf['kostum'],'--------')
            return pinf
        else:
            print('--------Не италия.--------')

filtr(gara)

pervyi = filtr(gara)
print(pervyi)

# измененные данные с добавленными значениями
# Напишите функцию которая принимает массив ранее измененых данных,
# меняет значение в каждом из элементов и возращает измененные данные
# Напишите функцию которая принимает массив ранее измененых данных,
# и поочередно выводит их в консоль
mass = [{"name": "Jack",
         "age": 24},
        {"name": "Joe", "age": 15},
        {"name": "Don", "age": 60},
        {"name": "JoeDon", "age": 5}]


def filter(arr):
    return arr


filteredMass = filter(mass)


def addElement(arr):
    for i in arr:
        i["live"] = "In Bishkek"
    return arr


newMass = addElement(filteredMass)


def changed(arr):
    for i in arr:
        i["age"] += 1
    return arr


changedMass = changed(newMass)


def printed(arr):
    for i in arr:
        print(i)


printed(changedMass)
