# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:51:08 2023

@author: Администратор
"""

# from datetime import datetime

# def get_force(train_mass, train_acceleration):
#     train_force = train_mass * train_acceleration
#     return train_force

# # str(1) -> '1'
# # str(10.5) -> '10.5'
# # int('1.') -> 1
# # float('1.') -> 1.
# # float('4.12e+1') -> 41.2

# # x = float(input())
# # print(x)

# def summing(a, b):
#     result = a+b
#     print(result)
    
# def subtraction (a, b):
#     result = a-b
#     print(result)
    
# # 2 + 3 - 1

# summing(2,3)

# # никак не могу применить функцию вычитания к результату суммы!

# def summing(a, b):
#     result = a+b
#     return result
    
# def subtraction (a, b):
#     result = a-b
#     return result

# print(subtraction(summing(2,3), 1))

# def calc_age (current_year, birth_year):
#     return current_year-birth_year

# my_age = calc_age(2023, 1983)

# current_dateTime = datetime.now()

# print(current_dateTime)

# my_age = calc_age(current_dateTime.year, 1983)
# print(my_age)

# def my_age(birth_year):
#     return (datetime.now().year - birth_year)

# def square_point(x_value, y_value):
#     x_2 = x_value * x_value
#     y_2 = y_value * y_value
#     return x_2, y_2

# x_2, y_2 = square_point(2,5)
# print(x_2, y_2)

# print(my_age(1986))

# def get_boundaries (target, margin):
#     low_limit = target - margin
#     high_limit = target + margin
#     return (low_limit, high_limit)

# print(get_boundaries (100, 20))

# def repeat_stuff(stuff, num_repeats = 10):
#     #if type(stuff) == ty
#     return str(stuff) * num_repeats

# lyrics = repeat_stuff('row ', 3) + 'your boat'
# print(lyrics)

# print(repeat_stuff(datetime.now(),4))

# f_temp = 100
# c_temp = 100

# def get_force(mass, acceleration):
#     force = mass* acceleration
#     return force

# def f_to_c (f_temp):
#     c_temp = (f_temp - 32) * 5/9
#     return c_temp

# print(f_to_c (f_temp))

# def c_to_f (c_temp):
#     f_temp = c_temp  * (9/5) + 32
#     return f_temp

# print(c_to_f (c_temp))

# c0_in_fahrenheit = c_to_f(0)
# print(c0_in_fahrenheit)

# f_temp = 100
# c_temp = 100    
 
# def c_to_f(c_temp ):
#     f_temp = c_temp * 9/5 + 32
#     #print (c_temp )
#     return f_temp

# f_to_c(100)

# def f_to_c (f_temp):
#     c_temp = (f_temp - 32)*5/9
#     return round(c_temp, 5) 

# t = 100

# # чтобы обрезать десятичную часть до определенного числа знаков,
# # используем либо round(), либо форматированный вывод
# #print(f"{f_to_c(t):.4f}")
# print(f_to_c(t))

# def get_force (mass, acceleration):
#     force = mass * acceleration
#     return force

# train_mass = 40000
# train_acc = 20

# print(get_force(train_mass, train_acc))



# result = get_force(100, 50)

# print(result)

# print(get_force(100, 50))

# train_mass = 50
# train_acceleration = 400

# print(get_force(train_mass, train_acceleration))

# x = 100
# y = pow(x, 2)



# train_mass = 22680
# train_acceleration = 10
# train_force = get_force(train_mass, train_acceleration)
# print (f'Поезд GE поставляет {train_force} ньютонов силы')

# def get_energy (mass, c=3*10**8):
#     energy = mass*c**2
#     return energy

# bomb_mass = 1
# bomb_energy = get_energy(bomb_mass)

# print (f' 1 кг боибы составляет {bomb_energy} Джоулей')

# def get_work(mass, acceleration, distance):
#     work = get_force(mass, acceleration)*distance
#     return work

# train_distance = 100

# train_work = get_work(train_mass, train_acceleration, train_distance)
# print (f'Поезд выполняет {train_work} Джоулей за {train_distance} метров')

# def clothes_by_time(time, clothes):
#     print(time + ' лучше всего подходит ' + clothes)

# clothes = 'домашняя одежда'

# print('У меня большой гардероб')
# clothes_by_time('Утром', clothes)
# clothes_by_time('Днем', clothes)
# clothes_by_time('Вечером', clothes)
# clothes_by_time('Ночью', clothes)

# def food_pref(meal = 'мясная пища'):
#     return meal
    
# phrase = str(input('Введите время еды (завтрак, обед, ужин):  '))

# print(f'''Я люблю покушать.
# На {phrase} мне лучше всего подходит {food_pref(meal = 1)}.''')

# meal1 ='каша'
# meal2 ='суп'

# def eat (time, meal):
#     phrase = (f' {time} мои предпочтения в еде {meal}')
#     return phrase

# d = 'Днем'
# e = 'Вечером'
# f ='Ночью'
# print(eat(d, meal1))
# print(eat(e, meal2))

# a = None
# print(a)


# Дмитрий номер АРМ 1
# Ангелина номер АРМ 2
# Василий номер АРМ 3
# Екатерина номер АРМ 4 

# функция проверки пары пользователь - арм
# параметры: user_name - строка, имя пользователя,
# arm - целое число, номер АРМ,
# возвращает: строка, сообщение для пользователя
# def check_user_arm(user_name, arm):
    
#     Dmitriy_check = ''' Дмитрий, твое рабочее место находится в другой комнате.
#      Отойди от чужого компьютера и займись работой!'''
#     greeting = "welcome"
    
#     if (user_name ==  'Дмитрий' and arm == 1) or \
#         (user_name ==  'Ангелина' and arm == 2) or \
#         (user_name ==  'Василий' and arm == 3) or \
#         (user_name ==  'Екатерина' and arm == 4): 
#          return greeting
#     elif user_name ==  'Дмитрий' and arm != 1 : 
#          return Dmitriy_check
#     elif (user_name ==  'Ангелина' and arm != 2) or \
#         (user_name ==  'Василий' and arm != 3) or \
#         (user_name ==  'Екатерина' and arm != 4): 
         
#         return "Логин или пароль неверный, попробуйте еще "
#     else:
#         return "Имя не опознано"
    
# user_name = input('Введите имя: ')
# arm = int (input("Введите арм: "))    
    
# print(check_user_arm(user_name, arm))

# def stud_grades (grade):
#     if  4.0 <= float(grade):
#         return "A"
#     elif 3.0 <= float(grade) < 4.0:
#         return "B"
#     elif 2.0 <= float(grade)< 3.0:
#         return "C"
#     elif 1.0 <= float(grade) < 2.0:
#         return "D"
#     elif 0.0 <= float(grade) < 1.0:
#         return "F"
#     else:
#         return "Неверный балл!"

# print(stud_grades(-1))

# def apru(num_polz, rev):
#     apru_1 = rev/num_polz
#     return apru_1

# arpu_spb = apru(4900, 63000)
# arpu_moscow = apru(3500, 48000)

# print(arpu_spb)
# print(arpu_moscow)

# def arpu (revenue_msk, user_msk, revenue_spb, user_spb):
#     arpu_msk = revenue_msk / user_msk
#     arpu_spb = revenue_spb / user_spb
#     return arpu_msk, arpu_spb

# num_users_msk = 4900
# rev_msk = 63000

# num_users_spb = 3500
# rev_spb = 48000

# def apru(num_polz, rev):
#     apru_1 = rev/num_polz
#     return apru_1

# msk = apru(num_users_msk, rev_msk)
# spb = apru(num_users_spb, rev_spb)

# source = 'Яндекс'

# def trafic_by_source(source):

#     if source == 'инфопартнер' or source == 'прямой заход':
#             return "Это бесплатный переход"
#     elif source == 'яндекс' or source == 'инстаграм':
#             return "Это платный переход"
#     else:
#             return "Неопознанный переход"
        
# print(source.lower())
# print(trafic_by_source(source.lower()))

# def my_sort (num1, num2, num3, ascending = True):
#     if num1>=num2 and num1>=num3:
#         max = num1
#         if num2>=num3:
#             mid = num2
#             min = num3
#         else:
#             mid = num3
#             min = num2
            
#     elif num2>=num1 and num2>=num3:
#         max = num2
#         if num1 >=num3:
#             mid = num1
#             min = num3
#         else:
#             mid = num3
#             min = num1
#     elif num3>=num1 and num3>=num2:
#         max = num3
#         if num1 >= num2:
#             mid = num1
#             min = num2
#         else:
#             mid = num2
#             min = num1    
            
#     if ascending == True:
#         return min, mid, max
#     else:
#         return max, mid, min
    
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# #answer = input('Сортировка по возрастанию? (y/n) ')
# # if answer == 'Y' or answer == 'y':
# #     ascending = True
# # else:
# #     ascending = False
    
# #ascending = True if input('Сортировка по возрастанию? (y/n) ').lower() == 'y' else False
    
# print(my_sort(num1,num2,num3,ascending))
        
num1 = int (input("Введите первое число "))
num2 = int (input("Введите второе число "))
num3 = int (input("Введите третье число "))

answer  = input(" сортировка по возрастанию?  (y/n)")

# if anser == "Y" or anser == "y":
#     ascending = True
# else:
#     ascending = False
    
    
ascending = True if answer =="Y" or answer == "y" else False
    
#print (my_sort(num1, num2, num3, ascending))
