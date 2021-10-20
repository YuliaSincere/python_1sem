#Вариант 3
#Пусть дана строковая переменная, содержащая информацию о студентах:
#my_string = «Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23
#года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса».
#Выведите информацию в виде:
#   Ф     И      О           О студенте
#Иванов Иван Иванович Студент 3 курса, 23 года
#Петров Семен Игоревич Студент 2 курса, 22 года

#Запрашиваем у пользователя строку
print("Введите информацию о двух студентах в виде:")
print("Ф;И;О;Возраст;Категория;Ф;И;О;Возраст;Категория")
my_string = input()

#Создаем строку, которая будет заглавием таблицы. Прописываем заголовки фиксированной длины
#(с помощью ljust) и выводим единой строкой
title_string = ("".join("Ф").ljust(15) + "".join("И").ljust(15) + 
                "".join("О").ljust(15) + "".join("О студенте").ljust(15))
print(title_string)

#Создаем разделитель под заглавной строкой
len_title = len(title_string)
divider = "_"
for i in range(len_title-1):
    divider = divider + "_"
print(divider)

#Создаем массив из полученной от пользователя строки для удобства
my_string_massiv = []
for i in my_string.split(";"):
    my_string_massiv.append(i)

print("".join(str(my_string_massiv[0])).ljust(15) + "".join(str(my_string_massiv[1])).ljust(15) +
      "".join(str(my_string_massiv[2])).ljust(15) + "".join(str(my_string_massiv[4])).ljust(10) +
      "".join(str(my_string_massiv[3])).ljust(8))
print("".join(str(my_string_massiv[5])).ljust(15) + "".join(str(my_string_massiv[6])).ljust(15) +
      "".join(str(my_string_massiv[7])).ljust(15) + "".join(str(my_string_massiv[9])).ljust(10) +
      "".join(str(my_string_massiv[8])).ljust(8))



