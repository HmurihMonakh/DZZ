# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь 
# вводит сами элементы множеств.

import random
mn1 = set([random.randint(1, 10) for i in range(int(input('введите количество элементов 1: ')))])
print(mn1)
mn2 = set([random.randint(1, 10) for i in range(int(input('введите количество элементов 2: ')))])
print(mn2)
mn_set = sorted(mn1.intersection(mn2))
print(mn_set)













