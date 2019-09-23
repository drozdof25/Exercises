def is_prime(num):
    de = int(num**0.5)
    if num == 1:
        return False
    for i in range(2,de+1):
        if num % i == 0:
            return False
    return True
num = int(input('Введите число от 0 до 1000: '))
if is_prime(num):
    print(str(num)+' - простое число')
else:
    print(str(num) + ' - составное число')