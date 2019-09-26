

import itertools


def XOR_cipher(string, key):
    answer = []
    key = itertools.cycle(key)
    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))
    return ''.join(answer)

string = str(input('Введите строку: '))
key = str(input('Введите ключ: '))

print('Зашифровано:   ' + XOR_cipher(string, key))
print('Разшифровано:   ' + XOR_cipher(XOR_cipher(string, key), key))