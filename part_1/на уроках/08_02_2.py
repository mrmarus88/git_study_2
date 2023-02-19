# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:32:49 2023

@author: lesna
"""

# list1 = [1,5,6,-7,100,-50,8,22,-13]


# min_num = list1 [0]

# for number in list1:
#     if number<min_num:
#         min_num = number
        
# print('Минимальное число в списке:  ', min_num)



# min_num = min(list1)
# print('Минимальное число в списке:  ', min_num)


# list1 = [1,5,6,-7,100,-50,8,22,-13]
# list1.sort()
# print('Минимальное число в списке:  ', list1[0])


# min_num = list1[0]

# for number in list1:
#     if number<min_num:
#         min_num=number
# print('Минимальное число в списке:  ', min_num)


number = str(1234)
summ=0
for item in number:
    if int(item) % 2 ==0:
        summ+=int(item)
print(summ)


