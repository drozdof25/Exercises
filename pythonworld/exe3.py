def square(a):
    P = a*4
    S = a**2
    d = a*2**0.5
    return (P,S,d,)
a = float(input('Введите сторону квадрата: '))
print('Периметр ' + str(square(a)[0]))
print('Площадь ' + str(square(a)[1]))
print('Диагональ ' + str(square(a)[2]))