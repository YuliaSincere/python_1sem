#Вариант 3
#Пусть дан список из 10 элементов.
#Удалите элементы с 4 по 8 и добавьте 2 новых. Выведите список на экран.

print("Введите 10 элементов")
list = []
for i in range(10):
    elem = input()
    list.append(elem)
print(list)

for i in range(len(list)):
    if (i == 4 or i == 8):
        del list[i]
print(list)
