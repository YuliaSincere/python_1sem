# Дан произвольный список чисел. Выведите результат умножения всех чисел меньше 10.

list = [1, 4, 8, 34, 12, 5, 56]
list_new = []
for i in range(0, len(list)):
    if list[i] < 10:
        list_new.append(list[i])
result = 1;
for i in range(0, len(list_new)):
    result = result * list_new[i]
print(list_new)
print(result)

