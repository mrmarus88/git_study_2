# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:32:49 2023

@author: lesna
"""

number = 1234
summ=0
# for item in number:
#     if int(item) % 2 ==0:
#         summ+=int(item)
# print(summ)

# while number>0:
#     n = number % 10
#     if n%2==0:
#         summ+=n
  
#     number = number // 10
    
# print(summ)


list1 = [1,3,4,5,3,2,4,5,6]

# def mean_count (number_list):
#     summ = sum(number_list)
#     q = len(number_list)
#     mean = summ/q
#     return mean

# result = mean_count(list1)
# print(result)
# summ = 0
# for item in list1:
#     summ += item

# avg_items = sum/len(list1)
# print(avg_items)


# def max_min (number_list):
#     return max(number_list) - min(number_list)

# print(max_min(list1))

# list1 = [1,5,6,-7,100,-50,8,22,-13]
# sum =0

# for item in list1:
#     if item>0:
#         sum +=item
# print(sum)

# Вариант с continue:
# list1 = [1,5,6,-7,100,-50,8,22,-13]

# def sum_number (number_list):
#     summ =0
#     for item in number_list:
#         if item<0:
#             continue
#         summ +=item
#     return summ
# print(sum_number(list1))

list1 = [-1,-5,-6,-7,100,-50,8,22,-13]


# for number in list1:
#     if number>0:
#         print(number, list1.index(number))
#         break
    
    
# for index in range(len(list1)): #[0,1,2,3,4,5,6,7,8]
#     if list1[index]>0:
#         print(index, list1[index])
#         break
     

# def number_check (number_list):
#     for index, number in enumerate(number_list): 
#         if number>0:
#             return index, number
#         print(number)

# a = number_check (list1)
# print(a)

list1 = [1,2,3,4,7]

for number in list1:
    if number%2!=0:
        print(number)



