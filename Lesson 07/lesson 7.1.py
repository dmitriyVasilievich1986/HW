# инициализация класса матрицы
class Matrix:
    # конструктор класса
    def __init__(self, using_matrix):
        self.matrix = using_matrix      # передаем список списков при создании класса

    # вывод матрицы в консоль
    def __str__(self):
        line = ''
        # цикл прохода по всем спискам матрицы
        for row in range(0, len(self.matrix)):
            for column in self.matrix[row]:
                line += str(column) + '\t'
            line += '\n'
        return line         # возвращаем результат

    # функция сложения двух матриц
    def __add__(self, other):
        output_matrix = []      # создание списка куда записываем результат
        # реализация цикла прохода по всем матрицам, выбираем большее число списков
        for row in range(0, max(len(self.matrix), len(other.matrix))):
            line = []
            # проход по всем числам в строке
            for column in range(0, max(len(self.matrix[row]), len(other.matrix[row]))):
                line.append(0)
                line[column] = 0 if len(self.matrix[row]) <= column else self.matrix[row][column]
                line[column] += 0 if len(other.matrix[row]) <= column else other.matrix[row][column]
            output_matrix.append(line)
        # возвращаем новый экземпляр класса, чтобы сразу вывести в консоль результирующую матрицу
        return Matrix(output_matrix)


# создание экземпляров класса
matrix1 = Matrix([[1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 50, 60]])
matrix2 = Matrix([[1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70, 80]])
# вывод в консол матрицы
print(matrix1)
# сложение и вывод в консол полученной матрицы
print(matrix1 + matrix2)
