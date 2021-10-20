#Вариант 3
#Пусть дана строковая переменная, содержащая информацию о студентах
#вида: my_string = «ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2
#курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21
#год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров
#Всеволод Борисович;21 год;Студент 2 курса».
#Выведите построчно информацию о студентах, чей возраст больше «21 года».

#импорт библиотеки для работы с регулярными выражениями
#регулярные выражения - шаблоны, используемые для поиска фрагмента текста или сопоставления символов
import re
#Задаем строку
my_string = "«ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса»"

#Проходимся по строке, разделяя ее на строки в список по разделителю
result = list(my_string.split("_"))
length = len(result)

#проходимся по списку
for i in range (1,length):
    #возраст = число(поиск в строке чисел ((\d+ - любая одна цифра от 0 до 9), строка)группировка найденных совпадений
    #в одну строку
    age = int(re.search('(\d+)', result[i]).group(0))
    #если возраст больше 21, то вывести строку, в которой осуществлялся поиск
    if age > 21:
        print(result[i])

