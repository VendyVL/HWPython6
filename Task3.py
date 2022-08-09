# Найти сумму чисел списка стоящих на нечетной позиции

list1 = [10, 10, 23, 10, 17, 66, 45, 58, 17, 45]

a = sum([list1[i] for i in range (len(list1)) if not i%2])


print(a)
