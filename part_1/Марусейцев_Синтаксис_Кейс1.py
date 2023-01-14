#Oil:
Oil_work_price = 500
Oil_work_time = 0.7
oil_extra = 5
oil_p = 700
Oil_price = oil_p / 100 * oil_extra + oil_p

#Filter:
Filtr_work_time = 0.5
Filtr_work_price = 450
filtr_extra = 5
Filtr_p = 300
Filtr_price = Filtr_p / 100 * filtr_extra + Filtr_p

#Calc:
Oil_work_cost = Oil_work_price * Oil_work_time
Filtr_work = Filtr_work_time * Filtr_work_price

Cost_sum = Oil_work_cost + Filtr_work + Oil_price + Filtr_price

#Discount:
discount = 3
Net_sum_cost = Cost_sum - Cost_sum / 100 * discount 

#show:
print('Расчет работ по представленному автомобилю:','\n',
      'Замена масла (работы)…………', Oil_work_cost , 'руб' '\n',
      'Масло Castrol…………………………',Oil_price, 'руб.' '\n',
      'Замена воздушного фильтра…',Filtr_work, 'руб.' '\n',
      'Воздушный фильтр…………………',Filtr_price, 'руб.' '\n',
      'Итого………………………………………',Cost_sum, 'руб.' '\n',
      'Персональная скидка……………………………3%' '\n',
      'Итого с учетом скидки……………', Net_sum_cost, '\n',
      'Спасибо, что выбираете Нас!')

