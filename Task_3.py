"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input('Введите число n: ')
summ = int(n)+int(n+n) + int(n + n + n)
print(f'Cумма чисел {n} + {n+n} + {n+n+n} = {summ}')