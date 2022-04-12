"""
	•	Используя модуль random, сформируйте случайным образом последовательность, состоящую из 20-ти нечетных чисел
в диапазоне от 100 до 1000.
Удалите из полученной последовательности максимальный и минимальный элементы.
Найдите среднее арифметическое пяти наибольших элементов в преобразованной последовательности.
"""

import random

l = []
while len(l) < 20:
    i = random.randrange(101, 1000, 2)
    l.append(i)
print(f'List: {l} has length: {len(l)}')

max_l = max(l)
min_l = min(l)

print(f'Max element = {max_l}')
print(f'Min element = {min_l}')

l.remove(min_l)
l.remove(max_l)

print(f'New l: {l} has length: {len(l)}')

sorted_l = sorted(l, reverse=True)
print(f'Sorted l: {sorted_l} has length: {len(l)}')
sum_5 = sum(sorted_l[:5])
print(f'Sum of first 5 biggest: {sum_5}')
a = sum_5 / 5
print(f'Srednee arifmeticheskoe :{a}')
