# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

list = [1, 2, 3, 5, 1, 5, 3, 10]


res = []
for i in range (0, len(list)):
    count = 0
    for j in range (0, len(list)):
        if list[i] == list[j]:
            count +=1
    res.append(count)

#  не придумала как поставить укороченную функцию где есть i и j

list2 = [list[i] for i in range(len(list)) if res[i] == 1]

print(list2)