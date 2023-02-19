# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:36:21 2023

@author: lesna
"""

# favorite_song = 'SmOoTH'
# favorite_song = favorite_song.lower()
# favorite_song = favorite_song.upper()
# favorite_song = favorite_song.title()
# print(favorite_song)

# poem_title = "spring storm"
# poem_author = "William Carlos Williams"
# poem_title_fixed = poem_title.title()
# print(poem_title_fixed)


# man_its_a_hot_one = "Like seven inches from the midday sun"
# print(man_its_a_hot_one.split())


# line_one = "The sky has given over"
# list_poem = line_one.split()


# authors = "Audre Lorde, Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman,\
#     Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes,\
#     Adrienne Rich, Nikki Giovanni"


# author_names = authors.split(', ')
# # print(author_names)
# author_last_names =authors.split()[1::2]

# # for index in range(len(author_last_names)):
# #     author_last_names[index] = author_last_names[index].replace(',', '')

# author_last_names = [author_last_names[index].replace(',', '') for index in range(len(author_last_names))]
# # for item in author_last_names:
# #     item = item.replace(',', '')

# print(author_last_names)

# spring_storm_text = \
# """The sky has given over
# its bitterness.
# Out of the dark change
# all day long
# rain falls and falls
# as if it would never end.
# Still the snow keeps
# its hold on the ground.
# But water, water
# from a thousand runnels!
# It collects swiftly,
# dappled with black
# cuts a way for itself
# through green ice in the gutters.
# Drop after drop it falls
# from the withered grass-stems
# of the overhanging embankment."""

# poem_list = spring_storm_text.split('\n')

# print(poem_list)
# my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
# my_munequita = ' '.join(my_munequita)
# print(my_munequita)


# string = 'престидижитатор'
# print(string[2])
# print(string[-2])
# print(string[:5])
# print(string[:-2])
# print(string[::2])
# print (string[1::2])
# print(string[::-1])
# print(string[::-2])
# print(len(string))


# def login_generator (first_name, patronymic, last_name):
#     return last_name+'.'+first_name[0]+patronymic[0]+'@company.ru'


# def password_check (password, first_name):
    
#     if (len(password)>=7) & (first_name[0].title() in password) & ('"' in password):
#         return 'Пароль изменен!'
#     else:
#         return 'Пароль не соответствует требованиям компании'


# print(login_generator('Victoria', 'Mikhailovna', 'Savinova'))
# print(password_check('cghnhyn"$', 'Victoria'))


def formating (header, author, doc_type):
    return header.upper(), author.title(), doc_type.lower()


print(formating('договор с заказчиком', 'иванов', 'Договор'))





