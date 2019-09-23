def arithmetic(num1,num2,operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        return num1/num2
    else:
        return 'Неизвестная операция'
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
operation = str(input('Операция: '))
print('Ответ: ' + str(arithmetic(num1,num2,operation)))

