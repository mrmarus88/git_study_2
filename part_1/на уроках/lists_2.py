# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 18:47:07 2023

@author: Администратор
"""

# first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак' ]
# print(first_names)

# age = []
# age.append(42)
# print(age)

# all_ages = [32, 41, 29] + age
# print(all_ages)


# name_and_age = zip(first_names,all_ages)
# print(list(name_and_age))

# ids = range(0,4)
# print(list(ids))

# table = list(zip(ids,first_names,all_ages))
# print(table)

#fruits = ['яблоко', 'банан', 'вишня', 'дыня']
# print(fruits[0:3])
# print(fruits[:3])
# print(fruits[2:])
# print(fruits[:])
# print(fruits[-3:])

# print(fruits[::2])
# print(fruits[::-1])

# print(fruits[3:1:-1])

# letters = ['м', 'и', 'с', 'с', 'и', 'с', 'и', 'п', 'и']
# print(letters.count('и'))

# votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'L aurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
# jake_votes = votes.count('Jake')
# print(jake_votes)

# names = ['Xander', 'buffy', 'Angel', 'Willow', 'Giles', '[jgdfkjg']
# result = names.sort(reverse = True)

# print(names)
# print(result)

# names_sort = sorted(names, reverse = True)
# print(names_sort)
# print(names)


# 312 = 3 * 10^2 + 1 * 10^1 + 2* 10^0
# 1101 = 1 * 2^0 + 0 * 2^1 + 1 * 2^2 + 1 * 2^3 = 1 *1 + 1 * 4 + 1 * 8 = 13

# a = 1000
# b = 1000
# c = 1
# print(id(a))
# print(id(b))
# print(id(c))

# 221 # int
# 221. # float
# '221' # float

# addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace' , '1600 Pennsylvania Ave', '10 Downing St.'] 
# addresses.sort()
# print(addresses)

# addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
# print(addresses.sort())
# print(addresses)

# print(sum(1,2))

# s = [1,2,3]
# print(id(s))
# s.append(4)
# print(id(s))
# s += [5,6] # s = s + [5,6]
# print(id(s))
# s = [1,2,3,4,5,6]
# print(id(s))
# s.insert(0,3)
# print(id(s))

# строка - неизменяемый тип
# s = 'abc'
# print(id(s))
# s += '4' # s = s + '4'
# print(id(s))
# print(s[1])
# s[1] = 'c'

# целое число - неизменяемый тип
# a = 1000
# print(id(a))
# a += 2 # a = a + 2
# print(id(a))

# def sum(a, b):
#     a = a + b
#     print('В функции а равно ', a)

# параметр - список
# def reverse(lst):
#     lst.reverse()

# a = 4
# b = 5
# c = sum(a,b)
# print(c)
# print('А в программе а равно', a)
#print(result)

# my_lst = [1,2,3]

# lst1 = reverse(my_lst)
# print(lst1)
# print(my_lst)

inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье', 'двуспальная кровать',
'двуспальная кровать', 'комод', 'комод', 'стол', 'стол', 'тумбочка', 'тумбочка'
,'королевский кровать', 'двуспальная кровать', 'две односпальные кровати'
,'две односпальные кровати', 'простыни', 'простыни', 'подушка', 'подушка']


# inventory_len = len(inventory) #19
# first = inventory[0] # двухспальная кровать
# last = inventory[-1] # подушка
# inventory_2_6 = inventory[2:6] #изголовье....комод
# first_3 = inventory[:3] #первые 3 предмета
# #??? так то в списке две записи, а в инвентаре их получается 4 ?
# twin_beds = inventory.count('две односпальные кровати')*2
# inventory.sort()

# print(inventory)

# first = inventory[0]
# print(first)
# last = print(inventory[-1])
# print(last)
# inv_2_6 = print(inventory[2:6])
# first_3 = print(inventory[:4])
# twin_beds = print(inventory.count('две односпальные кровати'))

# inventory.sort()
# print(inventory)



#sorted_inventory = print(sorted(inventory))

# first = inventory[0]
# inventory.sort()
# print(first)

# to_do_list = ['приготовить завтрак', 'поставить стирку', 'позвонить клиенту', 'приготовить ужин', 'помыть посуду']
# to_do_list[len(to_do_list):]=['повесить белье']
# print(to_do_list[len(to_do_list)-1:])

# # print(to_do_list)

# # to_do_list = ['приготовить завтрак', 'поставить стирку', 'позвонить клиенту', 'приготовить ужин', 'помыть посуду']
# to_do_list.extend(['повесить белье'])
# # print(to_do_list)

# to_do_list = ['приготовить завтрак', 'поставить стирку', 'позвонить клиенту',
# 'приготовить ужин', 'помыть посуду']
# to_do_list.insert(1, 'помыть посуду')
#print(to_do_list)

# order = ['паста', 'пицца', "салат капрезе"]
# order.extend(['салат цезарь','кофе'])
# # print(order)
# order.insert(0, "закуска из овощей")
# order[len(order):]=(['красное сухое вино'])
# print(order)

# print(to_do_list.pop(-1))
# print(to_do_list)

# numbers = [1, 2, 3, 5, 6, 8, 3]
# del numbers[2:5]
# print(numbers)

# x = 2
# y = x
# x = 3
# print(y)

# lst = [1,2,3]
# # lst1 = lst
# # lst[0] = 3
# # print(lst1)

# lst1 = lst.copy()
# lst[1] = 5
# print(lst1)
# print(lst)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(1))
print(id(my_tuple))
my_tuple += (6,7)
print(id(my_tuple))
print(min(my_tuple))

print(2 in my_tuple)
print(0 in my_tuple)

print(sorted(my_tuple))

print(list(my_tuple))