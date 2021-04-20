# Вставляйте решение под задачей

# Создайте массив состоящий из 5ти словарей
massa = [{
    'penal': 50,
    'pen' : 25},
    {'butter': 45},
    {'table' : 2000,
     'chair' : 500},
    {'book': 150,
     'album' : 180},
    {'toy' : 600,
     'car' : 1700}]



# Создайте массив состоящий из 5ти массивов с любыми значениями
han1 = [6, 4, 8, [5, "Nora", "Ben", ["liya", 26, 85, [45, [54, 97], "Den"]],[135, 69, 880]]]


# Замените в ранее созданном массиве несколько значений
han2 = [6, 4, 5, [5, "Nora", "Katy", ["liya", 26, 85, [45, [54, 97], "Den"]],[777, 69, 880]]]


# Создайте цикл для первого масссива
for lava in han1:
    result = lava
    print(result)


# Создайте цикл для второго масссива
for mava in han2:
    result = mava
    print(result)


# Создайте массив состоящий из 10 цифр от 0 и до 20
array = [ 0, 1, 2, 3, 4, 5, 6, 12, 15, 18]

# Пройдитесь циклоом по вышесозданному муссиву и выведите все чита которые больше 10ти
for haha in array:
    result = haha
    print(result)
print(array[7], array[8], array[9])




# Создайте словарь который содержит в себе все типы данных которые мы проходили (ключи на ваше усморение)
slovar = {
    'name': 'Kamil',
    'watch' : 5.3,
    'price' : 550,
    'true' : 'false'}


# Создайте словарь который содержит в себе 5 разных массивов
slovar2 = {'ds' :['a'],
          'hg' :['b'],
          'lk' :[8, 9],
          'jf' :[55],
          'zx' :['Tom', 'Jary']}


# Создайте условия if / else
sifra1 = 10
sifra2 = 8
if sifra1 >= sifra2:
    print('Правильный ответ')
else:
    print('Неверный ответ!')


# Создайте условия if / elif / else
flight = {
    'from': 'Tashkent',
    'to' : 'Bishkek',
    'flight time' : 2 ,
    'business class': 5000,
    'Economy class' : 3000
}

if flight['business class'] >= 9000:
    print('Отличного полета!')
elif flight['Economy class'] >= 3000:
    print('Мягкой посадки!')
else:
    print('Рейс отменен!')



# Создайте условия if / elif / elif / else
age =20
if age < 5:
    print('Малыш')
elif age > 5 and age < 12:
    print('Подросток')
elif age > 12 and age < 18:
    print('Юноша')
else:
    print("Мужчина  'Мужик'  -)")



# Создайте условия цикл который проходится по массиву в который содержит в себе условия if / elif / else

gara = [{
    'kostum' : 'Armani',
    'rubashka' : 'Gucci',
    'tufli' : 3000
},
    {'kostum' : 'ВЛКСМ',
    'rubashka' : 2000,
    'tufli' : 3000
}]
for band in gara:
    if band['kostum'] == 'Armani':
        print('Отличное качество!')
    elif band['kostum'] == 'ВЛКСМ':
        print('Качество ссср!')
    else:
        print('Китайская фигня!')
