consump = 123
time_start = 12
time_stop = 15
stove_type = 'Электро'

#############
# if (7<=time_start<10 and 7<=time_stop<10) or (17<=time_start<21 and 17<=time_stop<21):
#     tarif1 = 6.18
# elif 10<=time_start<17 and 10<=time_stop<17 or 21<=time_start<23 and 21<=time_stop<23:
#     tarif1 = 5.15
# elif (23<=time_start<24 or 0<=time_start<7) and (23<=time_stop<24 or 0<=time_stop<7) :
#     tarif1 = 1.74    
    
# if (7<=time_start<10 and 7<=time_stop<10) or (17<=time_start<21 and 17<=time_stop<21):
#     tarif = 6.18
# elif 10<=time_start<17 and 10<=time_stop<17 or 21<=time_start<23 and 21<=time_stop<23:
#     tarif = 5.92
# elif (23<=time_start<24 or 0<=time_start<7) and (23<=time_stop<24 or 0<=time_stop<7) :
#     tarif = 7.10    

# if stove_type == 'газ':
#     result_calc = consump*tarif
# elif stove_type == 'электро':
#     result_calc = consump*tarif1
    
####################

if stove_type == 'газ':
    if (7<=time_start<10 and 7<=time_stop<10) or (17<=time_start<21 and 17<=time_stop<21):
        tarif = 6.18
    elif 10<=time_start<17 and 10<=time_stop<17 or 21<=time_start<23 and 21<=time_stop<23:
        tarif = 5.92
    elif (23<=time_start<24 or 0<=time_start<7) and (23<=time_stop<24 or 0<=time_stop<7) :
        tarif = 7.10 
    # result_calc = consump*tarif
    # print( f'Потребление составило {result_calc} рублей' )
    
elif stove_type == 'электро':
    if (7<=time_start<10 and 7<=time_stop<10) or (17<=time_start<21 and 17<=time_stop<21):
        tarif = 6.18
    elif 10<=time_start<17 and 10<=time_stop<17 or 21<=time_start<23 and 21<=time_stop<23:
        tarif = 5.15
    elif (23<=time_start<24 or 0<=time_start<7) and (23<=time_stop<24 or 0<=time_stop<7) :
        tarif = 1.74
    # result_calc = consump*tarif
    # print( f'Потребление составило {result_calc} рублей' )    

# else:
#     print ("Введите корректные данные")
try:
    result_calc = consump*tarif
    print (f'Потребление составило {result_calc}')

except NameError:
    print ('Проверьте корректность данных')