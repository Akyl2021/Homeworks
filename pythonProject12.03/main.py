# method
# # Напишите приммеры использования всех операций со словарями
# # import copy
# from typing import Dict, List, Union
#
# dannye = {
#     'name': 'Ajara',
#     'zodiak': 'lev',
#     'age': 18}
# # clear()
# result = dannye.clear()
# print(result)
# # copy()
# dannye_2 = dannye.copy()
# dannye_2['name'] = 'Beka'
# #
# print(dannye)
# print(dannye_2)
# # fromkeys()
# new_dict = dannye.fromkeys(['name', 'age'], 'voobshe none')
# print(new_dict)
# # get()
#
# print(dannye.get('zodiak', 'est'))
#
# # items()
# dannye_2 = {
#     'name': 'Ajara',
#     'zodiak': 'lev',
#     'age': 18}
# print(
#     *dannye_2.items(),
#     sep='\n')
# # keys()
# # values()
# print(dannye_2.keys())
# print(dannye_2.values())
#
# # pop()
# print(dannye_2.pop('age'))
# # popitem()
# print(dannye_2.popitem())
# #   my_arr= [1, 2, 3, 4]
# def print_array_values(some_array):
#     def wrapper():
#         for i in some_array
#             print(i)
#
# my_dict_2[]
# my_dict
# print(' ------ second', my_dict['name'], my_dict['age'], 'second_name')

# Оберните все операции в функции, которые принимают словарь и выполняют над ним операцию.
# Функцию надо вызвать.
# granitsa_Kg = [
#     {
#         'sever': 'Kz',
#         'km': 400
#     },
#     {
#         'west': 'Tjk',
#         'km': 300
#     },
#     {
#         'east': 'China',
#         'km': 10
#     }
# ]
# def filter(args):
#     for spornyi in args:
#         if spornyi['km'] < 300:
#             print('---problem net', spornyi['km'])
#         else:
#             print('spornye uchastki', spornyi['km'])
#         result = granitsa_Kg.clear()
#
# print(result)
# clear()
# new_dict = granitsa_Kg.fromkeys(['km', 'yug'], 'voobshe none')
#
# filter(granitsa_Kg)
# #  # copy()
# granitsa_Kg = [{'sever': 'Kz', 'km': 400}, {'west': 'Tjk', 'km': 300}, {'east': 'China', 'km': 10}]
#
# ekzemplyar = granitsa_Kg.copy()
# def dict(state):
#     print(state)
# dict(granitsa_Kg)
# dict(ekzemplyar)

# fromkeys()
# get()
# items()
# keys()
# values()
# pop()
# popitem()

# Задача для гугления и самостоятельной рабооты. Разобрраться как работает метод dict.update()
# и dict.setdefault()
# --- > Здесь опишите решение


# Напишите пример вложенной функции.
# --- > Здесь опишите решение
# def sports():
#     def atletika():
#         kross = 2500
#         print(kross,'km')
#     def tyajelaya_atletika():
#         girya = 30
#         print(girya,'kg')
#
#     atletika()
#     tyajelaya_atletika()
# sports()

# Напишите функцию принимающую массив (состоящий из слов, название файла) и при помощи данных аргументов
# создающую запись в файле
my_array = ['Japan', 'ichiban','koohi','miruku','hanbagu','sutarubakusu','japanglish']
def func(arr):
    print(arr)
file = open('Japan','w')
file.write('Japan')
file.close()
func(my_array)
# Напишите функцию принимающую массив (состоящий из слов, название файла) и при помощи данных аргументов
# дополняющую файл новыми записями

# Напишите функцию считывающую данные из файла

# Напишите функцию записи в файл которая приниммает в себя данные, отфильтровывает их и записывает только
# отфильтрованные данные

#     'age': 15,
#     'gender': m
# }
# clear()
# my_dict_2 = my_dict.copy.deep()
# my_dict_2['name'] = argen
# my_dict_2[]
# my_dict
# print(' ------ second', my_dict['name'], my_dict['age'], 'second_name')
# new_dict = dict.fromkeys(['name','age'])
#
# print(my_dict.get('name', 'est imya'))
#
# my.dict.keys()
# my.dict.values()
# print(
# *my.dict.items(),
# sep='\n')
# my_arr= [1, 2, 3, 4]
# # def print_array_values(some_array):
# #     def wrapper():
# #         for i in some_array
# #             print(i)
# #
# import request
#
# my_string = 'hello world'
# file = open('test.txt', 'w')
#
# file.write('hello w')
# file.close()
#
# country = {
#     'USA' : 'Washington',
#     'England' : 'London',
#     'France' : 'Paris',
#     'Russia' : 'Moscow'
# }
# country.update(Russia = 'Nasha', Rodnoi = 'Bishkek')
# print(country)
#
#
#
# # Напишите пример вложенной функции.
# def outer_func():
#     def inner_func():
#         print("Hello, World!")
#
#     inner_func()
# outer_func()
#
#
#
#
# # Напишите функцию принимающую массив (состоящий из слов, название файла) и при помощи данных аргументов создающую
# # - запись в файле
# array = ['new_work', 'homework']
# def func(x):
#     print(x)
# mass = open('new_work', 'w' )
# mass.write('Hello my friends,  ')
# mass.close()
#
# func(array)
# # Напишите функцию принимающую массив (состоящий из слов, название файла) и при помощи данных аргументов дополняющую
# # - файл новыми записями
# array = ['new_work', 'homework']
# def func(x):
#     print(x)
#
# mass = open('new_work', 'a')
# mass.write('Good luck with your studies!')
# mass.close()
#
# func(array)
#
# # Напишите функцию считывающую данные из файла
# def func(x):
#     print(x)
#
# mass = open('new_work', 'r')
# print(mass.readline())
# mass.close()
#
# func(mass)
#
#
# # Напишите функцию записи в файл которая приниммает в себя данные, отфильтровывает их и записывает
# # - только отфильтрованные данные
#
# array = [{
#     'Toyota' : 'restyling',
#     'age' : 2016,
#     'Toyota' : 'not_restyling ',
#     'age' : 2008
# }]
#
# def filter(x):
#     for file in x:
#         if file['age'] >= 2008:
#             print('restyling')
#         else:
#             print('not restyling ')
#
# mass = open('homework', 'w' )
# mass.write('Vsem privet!')
# mass.close()
#
# filter(array)
#
