import random
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Инициализация левого потомка узла
        self.right = None  # Инициализация правого потомка узла


class BinaryTree:
    def __init__(self):
        self.root = None  # Инициализация корневого узла

    def insert(self, data):
        self.root = self._insert(self.root, data)  # Вставка нового узла в дерево

    def _insert(self, node, data):
        if node is None:
            return Node(data)  # Если узел пуст, создаем новый узел с заданными данными

        if data < node.data:
            node.left = self._insert(node.left, data)  # Рекурсивное добавление узла в левое поддерево
        else:
            node.right = self._insert(node.right, data)  # Рекурсивное добавление узла в правое поддерево

        return node  # Возвращаем узел

    def interpolation_search(self, data):
        return self._interpolation_search(self.root, data, self._min_value(), self._max_value())  # Поиск с
        # использованием интерполяционного поиска

    def _interpolation_search(self, node, data, min_val, max_val):
        if node is None or min_val > max_val:
            return False  # Если узел пуст или минимальное значение больше максимального, возвращаем False

        if node.data == data:
            return True  # Если значение узла равно искомому значению, возвращаем True

        if min_val == max_val:
            return False  # Если минимальное значение равно максимальному, возвращаем False

        mid = min_val + ((max_val - min_val) // (self._max_value() - self._min_value())) * (data - self._min_value())
        # Вычисляем среднее значение для интерполяции

        if node.data < mid:
            return self._interpolation_search(node.right, data, node.data + 1, max_val)
            # Рекурсивный поиск в правом поддереве, если значение узла меньше среднего значения
        else:
            return self._interpolation_search(node.left, data, min_val, node.data - 1)
            # Рекурсивный поиск в левом поддереве, если значение узла больше или равно среднему значению

    def _min_value(self):
        node = self.root
        while node.left:
            node = node.left
        return node.data  # Находим минимальное значение в дереве

    def _max_value(self):
        node = self.root
        while node.right:
            node = node.right
        return node.data  # Находим максимальное значение в дереве

    def print_tree_elements(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        print("Элементы дерева:", elements)
        # Выводим элементы дерева в порядке возрастания

    def _inorder_traversal(self, node, elements):
        if node:
            self._inorder_traversal(node.left, elements)
            elements.append(node.data)
            self._inorder_traversal(node.right, elements)
        # Рекурсивный обход дерева в порядке возрастания и добавление элементов в список

    def _inorder_traversal(self, node, elements):
        if node:
            self._inorder_traversal(node.left, elements)  # Рекурсивный обход левого поддерева
            elements.append(node.data)  # Добавление данных узла в список элементов
            self._inorder_traversal(node.right, elements)  # Рекурсивный обход правого поддерева)


# Генерация начального набора случайных данных
start = int(input("Введите минимальное значение генерируемых объектов: "))
end = int(input("Введите максимальное значение генерируемых объектов: "))
data = [random.randint(start, end) for _ in range(end)]
data.sort()

# Создание бинарного дерева
tree = BinaryTree()
start_time = time.time()
for item in data:
    tree.insert(item)
end_time = time.time()
tree_creation_time = end_time - start_time
print(f"Время создания дерева: {tree_creation_time:.6f} секунд")
tree.print_tree_elements()

# Поиск элемента
target = int(input("Введите элемент для поиска: "))
start_time = time.time()
result = tree.interpolation_search(target)
end_time = time.time()
search_time = end_time - start_time
print(f"Поиск в дереве: {result}, время работы: {search_time:.6f} секунд")