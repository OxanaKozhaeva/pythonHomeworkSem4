# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть
# ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9
import random

n = int(input('Введите количество кустов на грядке: '))
garden_bed = []
for i in range(n):
    garden_bed.append(random.randint(0, 20))
print(garden_bed)
three_bushes = 0
for i in range(n):
    if (garden_bed[i]+garden_bed[n-i-1]+garden_bed[n-i+1]) > three_bushes:
        three_bushes = garden_bed[i]+garden_bed[n-i-1]+garden_bed[n-i+1]
print(three_bushes)

Доброго времени суток, Кирилл! К сожалению, очень отстала по курсу.
Но очень хотелось по-честному выполнять д/з. Задача про чернику не получилась.