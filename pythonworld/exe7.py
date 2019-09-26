
def date(day, month, year):
    import datetime
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True

day = int(input('Введите день: '))
month = int(input('Введите месяц: '))
year = int(input('Введите год: '))

if date(day,month,year):
    print('Дата '+str(day)+'.'+str(month)+'.'+str(year)+' есть в нашем календаре')
else:
    print('Даты ' + str(day) + '.' + str(month) + '.' + str(year) + ' нету в нашем календаре')



