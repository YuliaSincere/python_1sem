#Пусть дана матрица чисел размером NхN. Представьте данную матрицу в
#виде списка. Выведите результат сложения всех элементов матрицы.

#Запрашиваем ввод у пользователя
print("Введите количество столбцов матрицы")
m_j = int(input())
print("Введите количество строк матрицы")
m_i = int(input())

#Создаем матрицу: матрица имеет вид массива списков, расположенных друг за другом
matrix = []
for x in range(m_j):
    j_list = []
#Задаем список
    for x2 in range(m_i):
        print("Введите элемент матрицы")
        elem = input()
        j_list.append(elem)
#Помещаем список в массив списков - матрицу
    matrix.append(j_list)

#for i in range(len(matrix)):
#    for j in range(len(matrix[i])):
#        print(matrix[i][j] + " ")

#Проходимся по матрице
#Заходим на строку-список, перебираем все элементы, затем переходим на новую строку-список
matrix_sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix_sum = matrix_sum + int(matrix[i][j])
print("Сумма элементов матрицы = " + str(matrix_sum))



