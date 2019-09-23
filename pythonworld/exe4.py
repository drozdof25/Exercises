def season(month):
    year = {'Зима' : (1,2,12),'Весна' : (3,4,5), 'Лето' : (6,7,8), 'Осень' : (9,10,11)}
    for seas in year.items():
       if month in seas[1]:
           return seas[0]
month = int(input('Введите месяц: '))
print(str(month)+'-ый месяц это ' + season(month))
