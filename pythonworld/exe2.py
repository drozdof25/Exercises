def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 ==0 and year % 100 !=0:
        return True
    return False

year = int(input('Введите год: '))
if is_year_leap(year):
    print(str(year) + ' - високосный год')
else:
    print(str(year) + ' - не високосный год')