import random
import time

def binary_search(arr, i):
    if len(arr) == 0:
        return -1

    a = len(arr) // 2

    if i == arr[a]:
        return a

    if i < arr[a]:
        return binary_search(arr[:a], i)

    if i > arr[a]:
        return binary_search(arr[a + 1:], i)


def add_element(arr, element):
    arr.append(element)
    arr.sort()

def remove_element(arr, element):
    arr.remove(element)

# Генерация начального набора случайных данных
start = int(input("Введите минимальное значение генерируемых объектов: "))
end = int(input("Введите максимальное значение генерируемых объектов: "))
data = [random.randint(start, end) for _ in range(end)]
data.sort()
print("Массив: ", data)

# Поиск элемента
target = int(input("Введите элемент для поиска: "))
start_time = time.time()
result = binary_search(data, target)
end_time = time.time()
binary_search_time = end_time - start_time
print(f"Бинарный поиск: {result}, время работы: {binary_search_time:.6f} секунд")

# Поиск элемента с использованием стандартной функции
start_time = time.time()
result = data.index(target) if target in data else -1
end_time = time.time()
standard_search_time = end_time - start_time
print(f"Стандартный поиск: {result}, время работы: {standard_search_time:.6f} секунд")

# Добавление элемента
new_element = int(input("Введите элемент который хотите добавить: "))
add_element(data, new_element)
print("Массив с добавленным элементом: ", data)

# Удаление элемента
delete = int(input("Введите элемент который хотите удалить: "))
remove_element(data, delete)
print("Массив без элемента: ", data)
