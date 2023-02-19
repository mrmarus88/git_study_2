# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:03:27 2023

@author: lesna
"""

#[0,1,2,3,4]
# board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
# sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

# for index_game in board_games: 
#     board_games.append(1) #бесконечный цикл, так как меняется длина перебираемого списка

# print('Hello')


# for index_game in range(len(board_games)): #for index_game in [0,1,2,3,4]
#     print(index_game)

# print('Hello')


# students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
# students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

# for student in students_period_A:
#     students_period_B.append(student)

# print(students_period_B)


# items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", 
# "dinosaur_onesie"]

# for item in items_on_sale:
#     if item == "striped_socks":
#         print(item)
#         break

# print('!!!!')


# big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# for number in big_number_list:
#     if number<0:
#         continue
#     print(number)


# dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

# dog_breed_I_want = 'dalmatian'

# for breed in dog_breeds_available_for_adoption:
#     if breed==dog_breed_I_want:
#         print("У них есть собака, которую я хочу!")
#         break


# students_period_A = [("Alex",2,3), ("Briana",3,4)]

# for index, student in enumerate(students_period_A):
#     print(index, student)


# students_period_A = [["Alex",2,3], ["Briana",3,4]]

# for index, student, ind in students_period_A:
#     print(index, student, ind)


# dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

# index = 0
# while index < len(dog_breeds):
#     print(dog_breeds[index])
#     index+=1



# students_period_A = [["Alex",2,3], ["Briana",3,4]]

# for item in students_period_A:
#         print(item[0])
    
# print(students_period_A[0][0])


# words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", 
# "@matchamom", "follow", "#updog"]

# result = []
# for word in words: 
#     if "@" in word:
#         result.append(word)
# print(result)

# result =[word for word in words if "@" in word]
# print(result)


single_digits = list(range(10))
squares = []

for digit in single_digits:
    print(digit)

for number in single_digits:
    squares.append(number**2)


# cubes = [number**3 for number in single_digits]
cubes = []
for number in single_digits:
    cubes.append(number**3)

print(squares)
print(cubes)