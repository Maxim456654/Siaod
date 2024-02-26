print("Hello world")

import random
import time
import copy

n = int(input('кол-во строк: '))
m = int(input('кол-во столбцов: '))
min = int(input('мин значение: '))
max = int(input('макс значение: '))


def generation_random_matrix(m, n):
    a = 1
    b = 0
    matrix1 = []
    for i in range(m):
        matrix2 = []
        for j in range(n):
            matrix2.append(random.randint(min, max))
            if a > matrix2[j]:
                a = matrix2[j]
            elif b < matrix2[j]:
                b = matrix2[j]
        matrix1.append(matrix2)
    return matrix1, a, b


random_matrix = generation_random_matrix(m, n)
for i, matrix in enumerate(random_matrix[0]):
    print(matrix)

fix_matrix = copy.deepcopy(random_matrix[0])
print('Несортированная матрица:', fix_matrix)


start_time = time.time()


# Сортировка выбором
def sort_choice(fix_matrix):
    n = len(fix_matrix)
    for x in range(n):
        nov = fix_matrix[x]
        m = len(nov)
        for i in range(0, m-1):
            min_index = i
            for j in range(i+1, m):
                if nov[j] < nov[min_index]:
                    min_index = j
            nov[i], nov[min_index] = nov[min_index], nov[i]
    return(fix_matrix)


print('сортировка выбром:', sort_choice(fix_matrix))
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


start_time = time.time()


# Сортировка вставкой
def sort_insert(fix_matrix):
    n = len(fix_matrix)
    for x in range(n-1):
        nov = fix_matrix[x]
        y = len(nov)
        for i in range(1, y):
            m = nov[i]
            j = i
            while (j - 1 >= 0) and (nov[j - 1] > m):
                m, nov[j] = nov[j], m
            nov[j] = m
    return(fix_matrix)


print('сортировка вставкой:', sort_insert(fix_matrix))
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


start_time = time.time()


# Сортировка обменом
def sort_change(fix_matrix):
    for i in range(len(fix_matrix) - 1):
        for i in range(len(fix_matrix[i]) - 1):
            for j in range(len(fix_matrix[i]) - i - 1):
                if fix_matrix[i][j] > fix_matrix[i][j + 1]:
                    fix_matrix[i][j], fix_matrix[i][j + 1] = fix_matrix[i][j], fix_matrix[i][j + 1]
    return(fix_matrix)


print('сортировка обменом:', sort_change(fix_matrix))
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


start_time = time.time()


#Сортировка Шелла
def sort_shell(fix_matrix):
    n = len(fix_matrix)
    for i in range(n-1):
        nov = fix_matrix[i]
        y = len(nov)
        gap = y // 2
        while gap > 0:
            for j in range(gap, y):
                m = nov[j]
                x = j
                while x >= gap and nov[j - 1] > m:
                    nov[j - 1], m = m, nov[j - 1]
                    j = j - gap
                nov[j] = m
            gap //= 2
    return(fix_matrix)


print('сортировка Шелла:', sort_shell(fix_matrix))
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


start_time = time.time()


# Быстрая сортировка
def sort_quick(fix_matrix):
    if len(fix_matrix) <= 1:
        return fix_matrix
    pivot = fix_matrix[len(fix_matrix) // 2]
    left = [x for x in fix_matrix if x < pivot]
    middle = [x for x in fix_matrix if x == pivot]
    right = [x for x in fix_matrix if x > pivot]
    return sort_quick(left) + middle + sort_quick(right)


print('быстрая сортировка:', sort_shell(fix_matrix))
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


start_time = time.time()


# Турнирная сортировка
def tournament_sort(fix_matrix):
    n = len(fix_matrix)
    tree = [0] * (2 * n)
    for i in range(n):
        tree[n + i] = fix_matrix[i]
    for i in range(n - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
    sorted_matrix = []
    while len(sorted_matrix) < n:
        winner = tree[1]
        sorted_matrix.append(winner)
        index = tree.index(winner)
        tree[index] = float('-inf')
        while index > 1:
            index //= 2
            tree[index] = max(tree[2 * index], tree[2 * index + 1])
    return sorted_matrix


print('Турнирная сортировка :', fix_matrix)
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))


start_time = time.time()

#стандартная функция сортировки
for sublist in fix_matrix:
    sublist.sort()
print('Стандартная функция сортировки:', fix_matrix)
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
