# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input("Enter number money: "))
sides_one = 0
sides_two = 0
for i in range(n):
    rand = random.randint(0, 1)
    print(rand, end=' ') # сколько всего монет и какой стороной, лежало на столе
    if rand == 0:
        sides_one += 1
    else:
        sides_two +=1
print('')
if sides_one < sides_two:
    print(sides_one)
if sides_two < sides_one:
    print(sides_two)

