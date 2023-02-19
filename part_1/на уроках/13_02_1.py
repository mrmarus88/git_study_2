# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:57:49 2023

@author: lesna
"""

string = 'яблоко'

# print(string[:-1:2])
# print(len(string))

# # string[0] = 'Я'
# string = 'Я' + string[1:]
# print(string*2)



# first_name = 'Виталий'
# last_name = 'Красилов'

# new_account = last_name[:5]
# temp_password = last_name[3:6]
# print(new_account, temp_password)


# def account_generator (first_name, last_name):
#     return first_name[:3]+last_name[:3]

# new_account = account_generator(first_name, last_name)
# print(new_account)

# def middle (string):
#     return (len(string)-1)/2


# first_name = 'роб'
# last_name = 'Дейли'

# first_name = "Р" + first_name[1:]

# print("theycallme\"crazy\"91")
# summ=0
# for index in range(len(string)):
#     summ+=1

# print(len(string), summ)
# print(tuple(string))

# def letter_check (word, letter):
#     if letter in word:
#         return True
#     else:
#         return False

# print(letter_check('Котя', 'к'))



# def contains (big_string, little_string):
#     if little_string in big_string:
#         return True
#     else:
#         return False

# print(contains("watermelon", "melon"))


# def common_letters (string1, string2):
#     result = []
#     for letter in string1:
#         if letter in string2 and letter not in result:
#             result.append(letter)
            
#     return result

# print(common_letters("banana", "cream"))


def username_generator (first_name, last_name):
    return first_name[:3]+last_name[:4]


def password_generator (username):
    return username[-1] + username[:-1]
    
print(username_generator('Abe', 'Simpson'))
print(password_generator(username_generator('Abe', 'Simpson')))

