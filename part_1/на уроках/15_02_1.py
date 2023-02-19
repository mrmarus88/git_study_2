# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:02:42 2023

@author: lesna
"""

cards = [['Астахов', 'Игорь', 'Александрович', 35, 'Муж', True, 'Москва', 'маркетолог'], 
['Вавилова', 'Елена', 'Сергеевна', 40, True, True, 'Таганрог', 'бухгалтер'], ['Карелин', 'Андрей', 
'Васильевич', 25, 'Муж', False, 'Подольск', 'специалист'], ['Воронова', 'Мария', 'Игоревна', 
30, True, False, 'Москва', 'менеджер'], ['Остроумовна', 'Карина', 'Владимировна', 44, True, 
True, 'Подольск', 'маркетолог'], ['Борзов', 'Владимир', 'Андреевич', 40, 'Муж', False, 
'Москва', 'начальник отдела']]

spec = ['маркетолог', 'бухгалтер', 'менеджер', 'специалист']
mid_manag = ['начальник отдела', 'главный бухгалтер']
top_manag = ['директор']
salary = [40000, 60000, 80000]

for list1 in cards:
    if list1[4] == True:
        list1[4]='Жен'

def append_salary (cards, spec, mid_manag, top_manag, salary):
    for emploee in cards:
        if emploee[-1] in spec:
            emploee.append(salary[0])
            
        elif emploee[-1] in mid_manag:
            emploee.append(salary[1])
            
        else:
            emploee.append(salary[2])
    return  cards

cards = append_salary(cards, spec, mid_manag, top_manag, salary)
# print(cards)

def bonus (card, bonus_sum):
    card[-1]+=bonus_sum
    return (card)


def tax (card, rate):
    card[-1]-=card[-1]*rate
    return card, card[-1]*rate


for card in cards:
    if card[5] == True:
        card = bonus (card, 5000)
    
sum_tax = []
for card in cards:
    card = tax (card, 0.13)[0]
    sum_tax.append(tax (card, 0.13)[1])
    
print(cards)
print(sum_tax)
    

