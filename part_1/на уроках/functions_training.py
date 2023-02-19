# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:39:47 2023

@author: Администратор
"""
x = 0
# функция, возводящая параметр в степень и сравнивающая с 5000
# параметры: num - число, основание степени, powr - число, показатель степени
# возвращает: логическое значение, True, если результат больше 5000, иначе False
# def function_exp (num, powr):
#     result = num**powr
#     # z = x+1
#     # print(z)
#     if result>5000:
#         return result, True
#     else:
#         return result, False  

# p = function_exp (500,3)
# print(p)

# print(function_exp (2,3/2))
# print(num) -переменные живут внутри функции. За ее пределами они не видны и не выполняются. 
# За ее пределами это уже другая перемення.
# x=5
# y=2
# function_exp (x,y)

# проверка, попадает ли число в отрезок,
# параметры: num - исходное число, num_floor - число, нижняя граница отрезка, 
# num_ceil - число, верхняя граница отрезка
# возвращает False, если число снаружи отрезка, True - если внутри
# def comparison (num_floor, num, num_ceil):
#     #if num_floor <= num and num<= num_ceil:
#     if num_floor<= num<= num_ceil:
#         return True
#     else:
#         return False
# print(comparison (2, 6, 4))

# x = False
# y = 1 > 2
# print(x and y)

# def true_name (my_name, your_name):
#     if my_name == your_name:
#         return True
#     else:
#         return False

# print(true_name("Oleg", "Egor"))
# print(true_name("Oleg", "Oleg"))

# def my_sum(a, b):
#     return a + b

# print(my_sum(int(input('Введите первое число: ')),int(input('Введите второе число: '))))

# пример функции с противоречием
# def my_func(a, b):
#     if a < b and b < a:
#         return True
#     else:
#         return False
    
# print(my_func(-3,2))

# а вот в этой функции противоречия нет
# она для большей части значений параметров возвращает True,
# но при a == b она возвращает False
# def my_func2(a, b):
#     if a < b or b < a:
#         return True
#     else:
#         return False
    
# print(my_func2(-3,2))
# print(my_func2(5,10))
# print(my_func2(2,2))

# def movie(rating):
#     if rating <= 5:
#         print("Избегайте любой ценой!")
#     elif rating < 9:
#         print("Это было весело")
#     else:
#         print("Отлично!")

# rating = int(input("Введите рейинг: "))
# movie(rating)

# def rating (ball):
#     if ball <= 5:
#         return ('Избегать любой ценой!')
#     elif 5 < ball <= 9:
#         return ("Это было весело")
#     else:
#         return ('Отлично')
    
# print ('Фильм: Аватар 2 - ' + rating (6))

# как написать функцию?
# 1. напишите то, что вы хотите сделать в функции, в виде программы

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))

# if num1 > num2 and num1 > num3:
#     print('Наибольшее число - ' + str(num1))
# elif num2 > num1 and num2 > num3:
#     print('Наибольшее число - ' + str(num2))
# elif num3 > num1 and num3 > num2:
#     print('Наибольшее число - ' + str(num3))
# else:
#     print('Ничья!')

# 2. все строки, в которых есть input(), не трогаем
# 3. остальные строки помещаем внутрь тела функции,
# все переменные, которые вводили при помощи input() будут параметрами
# везде, где в коде был print(), делаем return
# внимательно продумайте, что именно возвращает return,
# особенно в исключительных случаях
# def compare_3_nums(num1, num2, num3):

#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     elif num3 > num1 and num3 > num2:
#         return num3
#     else:
#         return None

# result = compare_3_nums(num1, num2, num3)

# print(result)

# if result is None:
#     print('Ничья!')
# else:
#     print('Наибольшее число - ' + str(result))

def power(num, powr):
    return num ** powr

def tenth_power(num):
    return power(num, 10)

def square_root(num):
    return power(num, 0.5)

print(square_root(9))
print(power(3,5))