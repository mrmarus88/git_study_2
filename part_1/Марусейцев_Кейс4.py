#data : 

incident_type = ['ложное срабатывание', 'событие', 'инцидент', 
                 'ложное срабатывание', 'инцидент', 
                 'ложное срабатывание', 
                 'ложное срабатывание', 'событие', 
                 'ложное срабатывание', 'инцидент', 
                 'ложное срабатывание', 'инцидент', 
                 'ложное срабатывание', 
                 'ложное срабатывание', 'инцидент', 'событие', 'событие', 'событие', 
                 'ложное срабатывание', 'ложное срабатывание', 'ложное срабатывание', 'ложное срабатывание', 'инцидент'] 

owner = ['ivanov', 'petrov', 'meshkov', 'alexandrova',
         'potanina', 'druyan', 'alexandrova', 'meshkov',
         'petrov', 'potanina', 'ivanov', 'potanina', 
         'meshkov', 'meshkov', 'potanina', 'ivanov',
         'druyan', 'druyan', 'potanina', 'ivanov', 
         'meshkov', 'meshkov', 'petrov'] 

minutes = [5, 7, 19, 8, 7, 4, 4, 19, 6, 12, 4, 17, 4, 6, 4, 5, 2, 18, 14, 13, 3, 17, 2]

#scripts:

#1  Рассчитать сумму времени в часах, затраченное диспетчером Александром на инциденты 
all_sum = float('{:.2f}'.format(sum(minutes)/60))
print('Общее время на инциденты (hour):', all_sum)

#2 Рассчитать среднее время, затраченное Александром на инцидент 
mid_time = float('{:.2f}'.format(sum(minutes)/len(minutes)))
print('Среднее время (min):', mid_time)

#3 Рассчитать максимальное время, потраченное на инцидент и выявить его тип
max_time = max(minutes)
index_minutes = minutes.index(max(minutes))
type_inci = incident_type[index_minutes]
print('Максимальное время потраченое на инцидент:',max_time,'; Тип инцидента:',type_inci)

#4 Вывести в консоль, сколько всего ложных срабатываний было среди инцидентов 
fault_count = 0
for n in incident_type:
    if n == 'ложное срабатывание':
        fault_count += 1
print('Всего ложных срабатываний: ', fault_count)

#5 Вывести в консоль, сколько всего событий было среди инцидентов 
event_count = 0
for n in incident_type:
    if n == 'событие':
        event_count += 1
print('Всего событий: ', event_count)

#6 Вывести в консоль, сколько всего инцидентов было среди инцидентов 
inci_count = 0
for n in incident_type:
    if n == 'инцидент':
        inci_count += 1
print('Всего инцидентов: ', inci_count)

#7 Объединить 3 списка в новый и вывести в консоль для удобства отображения 
all_list = incident_type + owner + minutes
print(all_list)

#8 Рассчитать, сколько времени в сумме диспетчер потратил на события
events_time = []
for index in range(len(incident_type)):
    if incident_type[index] == 'событие':
        events_time.append(minutes[index])
        events_t = sum(events_time)  
print('Общее время на события (min):',events_t)

#9 Вывести последние 10 инцидентов и поместить их в отдельный список
incident_type.reverse()
rvrs = incident_type[:10]
rvrs.reverse()
print(rvrs)

#10 Вывести ответственных за инциденты, на которые было потрачено больше 15 минут 
inci_name = []
for index in range(len(minutes)):
    if minutes[index] >= 15 :
        inci_name.append(owner[index])
print(inci_name)

#11 Пришла информация еще о 3-х инцидентах в виде списков. Добавить в соответствующие списки информацию о новых инцидентах
incident_type_new = ['событие', 'событие', 'ложное срабатывание'] 
owner_new = ['petrov', 'potanina', 'ivanov'] 
minutes2 = [3, 5, 6] 

incident_type_final = incident_type + incident_type_new
owner_final = owner + owner_new
time_final = minutes + minutes2

print(incident_type_final,owner_final,time_final, sep = '\n')
