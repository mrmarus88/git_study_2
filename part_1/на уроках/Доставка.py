weight = float (input('Введите вес вашей посылки:'))
fix = 20
premium_deliv = 40

if weight <= 2:
    tarif_courier = 1.5
    tarif_drone = 4.5
elif 2 < weight <= 6:
    tarif_courier = 3
    tarif_drone = 9
elif 6 < weight <= 10:
    tarif_courier = 4
    tarif_drone = 12
else:
    tarif_courier = 4.75
    tarif_drone = 14.25
    
delivery_courier = fix + weight*tarif_courier
delivery_drone = weight*tarif_drone
print(delivery_drone, delivery_courier, premium_deliv)

#####БЕЗ ПРЕМИУМ
# if delivery_courier > delivery_drone :
#     print ('Ваша посылка будет доставлена дроном и составит ', delivery_drone)
# elif delivery_courier < delivery_drone :
#     print ('Ваша посылка будет доставлена курьером и составит ', delivery_courier)
  
# elif delivery_courier == delivery_drone:
#     print ('Ваша посылка будет доставлена  выбранным вами способом и составит ', delivery_courier)

################### С премиум

if delivery_courier > delivery_drone and premium_deliv > delivery_drone:
    print ('Ваша посылка будет доставлена дроном и составит ', delivery_drone)

elif delivery_courier < delivery_drone and delivery_courier < premium_deliv:
    print ('Ваша посылка будет доставлена курьером и составит ', delivery_courier)

elif premium_deliv < delivery_drone and delivery_courier > premium_deliv:
    print ('Ваша посылка будет доставлена премиум доставкой и составит ', premium_deliv)    
    
elif delivery_courier == delivery_drone:
    print ('Ваша посылка будет доставлена  выбранным вами способом и составит ', delivery_courier)

elif premium_deliv == delivery_drone:
    print('Ваша посылка будет доставлена выбранным вами способом и составит', delivery_drone)

elif premium_deliv == delivery_courier:
    print('Ваша посылка будет доставлена выбранным вами способом и составит', delivery_courier)

elif premium_deliv == delivery_drone == delivery_courier:
    print('Ваша посылка будет доставлена выбранным вами способом и составит', delivery_drone)    
    
    
    
    
    
    
    
    
    
    
    