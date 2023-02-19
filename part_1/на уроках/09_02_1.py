# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:19:48 2023

@author: lesna
"""

# ill= [3.9, 4.4, 4.3, 4.6, 4.7]
# deth=[900, 997, 1001, 1003, 987]

# deth_part = []
# ill_new = []
# for man in ill:
#     ill_new.append(man*1000)
    
# for index in  range(len(ill_new)):
#     deth_part.append(round(deth[index]/ill_new[index], 2))

    
# # ill_new2 = [man*1000 for man in ill]
# deth_part2  = [round(deth[index]/ill_new[index], 2) for index in  range(len(ill_new))]
# print(len(ill_new), len(deth))
# print(deth_part2)

# mean_ill = sum(ill_new)/len(ill_new)
# mean_death = sum(deth)/len(deth)
# print(mean_ill, mean_death)


emploee_list = ['Ганеев','Крутов','Свердлов','Ватсон','Цой']

ill_list = ['Иванов','Ганеев']


# for person in ill_list:
#     for emploee in emploee_list:
#         if person == emploee:
#             print(len(emploee_list))
#             print('сотрудники присутствовали')
#             break
    
# for emploee in ill_list:
#     if emploee in emploee_list:
#         print(len(emploee_list))
#         print('сотрудники присутствовали')
#         break

# def analytic (input_list):
#     mean = sum(input_list) / len(input_list)
#     maximum = max(input_list)
#     minimum = min(input_list)
    
#     return round(mean, 1), maximum, minimum

# price = [300, 500, 124, 750, 567, 320]
# quantity = [10, 6, 12, 4, 5, 20]
# revenue=[]

# for index in range(len(price)):
#     revenue.append(price[index]*quantity[index])

# revenue2 = [price[index]*quantity[index] for index in range(len(price))]

# print(revenue2)

# print('аналитика по ценам', analytic(price))
# print('аналитика по продажам', analytic(quantity))
# print('аналитика по выручке', analytic(revenue))


def sales_check (price_list, limit):
    summ=0
    for index in range(len(price_list)):
        summ+=price_list[index]
        if summ>limit:
            summ-=price_list[index]
            break
     
    return summ
    
print(sales_check([200, 300, 200], 600))    
    
    
    
    
    
    

