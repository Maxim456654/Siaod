import random
import time


class Node:
    def __init__(self, data):
        self.data = data  # Инициализация данных узла
        self.left = None  # Инициализация левого потомка узла
        self.right = None  # Инициализация правого потомка узла


class BinaryTree:
    def __init__(self):
        self.root = None  # Инициализация корневого узла

    def add(self, data):
        if self.root is None:
            self.root = Node(data)  # Если корневой узел пуст, создаем новый узел с заданными данными
        else:
            self._add(data, self.root)  # Если корневой узел не пуст, вызываем вспомогательную функцию для добавления узла

    def _add(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)  # Если значение меньше значения узла и левый потомок пуст, создаем новый узел
            else:
                self._add(data, node.left)  # Если значение меньше значения узла и левый потомок не пуст, рекурсивно добавляем узел в левое поддерево
        else:
            if node.right is None:
                node.right = Node(data)  # Если значение больше или равно значению узла и правый потомок пуст, создаем новый узел
            else:
                self._add(data, node.right)  # Если значение больше или равно значению узла и правый потомок не пуст, рекурсивно добавляем узел в правое поддерево

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)  # Если корневой узел пуст, создаем новый узел с заданными данными
        else:
            self._insert(data, self.root)  # Если корневой узел не пуст, вызываем вспомогательную функцию для вставки узла

    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)  # Если значение меньше значения узла и левый потомок не пуст, рекурсивно вставляем узел в левое поддерево
            else:
                node.left = Node(data)  # Если значение меньше значения узла и левый потомок пуст, создаем новый узел
        else:
            if node.right:
                self._insert(data, node.right)  # Если значение больше или равно значению узла и правый потомок не пуст, рекурсивно вставляем узел в правое поддерево
            else:
                node.right = Node(data)  # Если значение больше или равно значению узла и правый потомок пуст, создаем новый узел

    def search(self, data):
        return self._search(data,
                            self.root)  # Вызываем вспомогательную функцию для поиска узла с заданными данными в дереве

    def _search(self, data, node):
        if node is None:
            return False  # Если узел пуст, возвращаем False
        if node.data == data:
            return True  # Если значение узла равно искомому значению, возвращаем True
        elif data < node.data:
            return self._search(data,
                                node.left)  # Рекурсивный поиск в левом поддереве, если значение меньше значения узла
        else:
            return self._search(data,
                                node.right)  # Рекурсивный поиск в правом поддереве, если значение больше значения узла

    def remove(self, data):
        self.root = self._remove(data, self.root)  # Удаление узла с заданными данными из дерева

    def _remove(self, data, node):
        if node is None:
            return node  # Если узел пуст, возвращаем узел
        if data < node.data:
            node.left = self._remove(data,
                                     node.left)  # Рекурсивное удаление узла из левого поддерева, если значение меньше значения узла
        elif data > node.data:
            node.right = self._remove(data,
                                      node.right)  # Рекурсивное удаление узла из правого поддерева, если значение больше значения узла
        else:
            if node.left is None:
                return node.right  # Если левый потомок пуст, возвращаем правый потомок
            elif node.right is None:
                return node.left  # Если правый потомок пуст, возвращаем левый потомок
            else:
                successor = self._find_min(node.right)  # Находим узел-преемник в правом поддереве
                node.data = successor.data  # Заменяем данные текущего узла данными узла-преемника
                node.right = self._remove(successor.data,
                                          node.right)  # Рекурсивно удаляем узел-преемник из правого поддерева
        return node  # Возвращаем узел

    def _find_min(self, node):
        while node.left:
            node = node.left  # Находим узел с минимальным значением в дереве
        return node  # Возвращаем узел

    def print_tree_elements(self):
        elements = []
        self._inorder_traversal(self.root,
                                elements)  # Вызываем вспомогательную функцию для обхода дерева в порядке возрастания и добавления элементов в список
        print("Элементы дерева:", elements)  # Выводим элементы дерева

    # Фибоначчиев поиск
    def fibonacci_search(self, data):
        elements = []
        self._inorder_traversal(self.root, elements)  # Получаем элементы дерева в порядке возрастания
        return self._fibonacci_search(data, elements)  # Выполняем поиск с использованием метода Фибоначчи

    def _fibonacci_search(self, data, elements):
        n = len(elements)  # Получаем количество элементов в дереве
        fib_m2 = 0  # (m-2)-е число Фибоначчи
        fib_m1 = 1  # (m-1)-е число Фибоначчи
        fib_m = fib_m2 + fib_m1  # m-е число Фибоначчи

        while fib_m < n:
            fib_m2 = fib_m1
            fib_m1 = fib_m
            fib_m = fib_m2 + fib_m1  # Вычисляем числа Фибоначчи до тех пор, пока m < n

        offset = -1

        while fib_m > 1:
            i = min(offset + fib_m2, n - 1)  # Вычисляем индекс i

            if elements[i] < data:
                fib_m = fib_m1
                fib_m1 = fib_m2
                fib_m2 = fib_m - fib_m1
                offset = i  # Обновляем значения чисел Фибоначчи и смещение, если элемент меньше искомого значения

            elif elements[i] > data:
                fib_m = fib_m2
                fib_m1 = fib_m1 - fib_m2
                fib_m2 = fib_m - fib_m1  # Обновляем значения чисел Фибоначчи, если элемент больше искомого значения

            else:
                return i  # Возвращаем индекс, если элемент найден

        if fib_m1 and offset < n - 1 and elements[offset + 1] == data:
            return offset + 1  # Возвращаем индекс, если элемент найден

        return -1  # Возвращаем -1, если элемент не найден

    def _inorder_traversal(self, node, elements):
        if node:
            self._inorder_traversal(node.left, elements)  # Рекурсивный обход левого поддерева
            elements.append(node.data)  # Добавляем данные узла в список элементов
            self._inorder_traversal(node.right, elements)  # Рекурсивный обход правого поддерева


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
result = tree.search(target)
end_time = time.time()
search_time = end_time - start_time
print(f"Поиск в дереве: {result}, время работы: {search_time:.6f} секунд")

# Добавление элемента
new_element = int(input("Введите элемент который хотите добавить: "))
tree.add(new_element)
print("Элементы дерева:")
tree.print_tree_elements()

# Удаление элемента
delete = int(input("Введите элемент который хотите удалить: "))
start_time = time.time()
tree.remove(delete)
end_time = time.time()
removal_time = end_time - start_time
print(f"Удаление из дерева: время работы: {removal_time:.6f} секунд")
print("После удаления:")
tree.print_tree_elements()

# Поиск элемента
tree.print_tree_elements()
target = int(input("Введите элемент для поиска: "))
start_time = time.time()
result = tree.fibonacci_search(target)
end_time = time.time()
search_time = end_time - start_time
print(f"Поиск в дереве: {result}, время работы: {search_time:.6f} секунд")