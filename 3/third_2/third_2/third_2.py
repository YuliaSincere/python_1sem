#Вариант 3
#Пусть дана строковая переменная, содержащая информацию о студентах:
#my_string = «Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23
#года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса».
#Выведите информацию в виде:
#   Ф     И      О           О студенте
#Иванов Иван Иванович Студент 3 курса, 23 года
#Петров Семен Игоревич Студент 2 курса, 22 года

#Задаем строку
my_string = "_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса;_Иванов тест;Иван;Иванович;23 года;Студент 3 курса"

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
massiv_number = len(my_string_massiv)/5
massiv_number_int = int(massiv_number)
print(massiv_number_int)
len_m = len(my_string_massiv)
i = 0
while i <= len_m-1:
    print("".join(str(my_string_massiv[i])).ljust(15) + "".join(str(my_string_massiv[i+1])).ljust(15) +
        "".join(str(my_string_massiv[i+2])).ljust(15) + "".join(str(my_string_massiv[i+3])).ljust(10) +
        "".join(str(my_string_massiv[i+4])).ljust(8))
    i = i + 5

