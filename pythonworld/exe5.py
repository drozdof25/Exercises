def bank(a,years):
    for i in range(0,years):
        a *= 1.1
    return a
a = float(input('Введите сумму вклада: '))
years = int(input('Кол-во лет: '))
print('Итого: ' + str(bank(a,years)))