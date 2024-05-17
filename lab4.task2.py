# Простое рэхеширование
class HashTable1:
    def __init__(self, size):
        self.size = size  # Инициализация размера хэш-таблицы
        self.table = [[] for _ in range(size)]  # Создание пустой хэш-таблицы заданного размера

    def hash(self, key):
        return hash(key) % self.size  # Вычисление хэша ключа

    def insert(self, key, value):
        index = self.hash(key)  # Получение индекса для вставки
        self.table[index].append((key, value))  # Вставка ключа и значения в соответствующий индекс

    def search(self, key):
        index = self.hash(key)  # Получение индекса для поиска
        for k, v in self.table[index]:  # Поиск ключа в соответствующем индексе
            if k == key:
                return v  # Возвращаем значение, если ключ найден
        return None  # Возвращаем None, если ключ не найден

    def rehash(self, new_size):
        old_table = self.table  # Сохранение старой хэш-таблицы
        self.size = new_size  # Обновление размера хэш-таблицы
        self.table = [[] for _ in range(new_size)]  # Создание новой пустой хэш-таблицы заданного размера

        for bucket in old_table:  # Перехеширование элементов из старой таблицы в новую
            for key, value in bucket:
                self.insert(key, value)  # Вставка ключа и значения в новую хэш-таблицу


import random


# Рехэширование с помощью псевдослучайных чисел
class HashTable2:
    def __init__(self, size):
        self.size = size  # Инициализация размера хэш-таблицы
        self.table = [[] for _ in range(size)]  # Создание пустой хэш-таблицы заданного размера
        self.rehash_count = 0  # Инициализация счетчика рехэширований

    def hash(self, key):
        return hash(key) % self.size  # Вычисление хэша ключа

    def insert(self, key, value):
        index = self.hash(key)  # Получение индекса для вставки
        self.table[index].append((key, value))  # Вставка ключа и значения в соответствующий индекс

        # Триггер для рехэширования
        if len(self.table[index]) > self.size // 2:
            self.rehash(self.size * 2)  # Вызов метода рехэширования

    def search(self, key):
        index = self.hash(key)  # Получение индекса для поиска
        for k, v in self.table[index]:  # Поиск ключа в соответствующем индексе
            if k == key:
                return v  # Возвращаем значение, если ключ найден
        return None  # Возвращаем None, если ключ не найден

    def rehash(self, new_size):
        old_table = self.table  # Сохранение старой хэш-таблицы
        self.size = new_size  # Обновление размера хэш-таблицы
        self.table = [[] for _ in range(new_size)]  # Создание новой пустой хэш-таблицы заданного размера
        self.rehash_count += 1  # Увеличение счетчика рехэширований

        for bucket in old_table:  # Перехеширование элементов из старой таблицы в новую
            for key, value in bucket:
                self.insert(key, value)  # Вставка ключа и значения в новую хэш-таблицу

        # Перемешивание таблицы после рехэширования
        random.shuffle(self.table)


# Метод цепочек
class HashTable3:
    def __init__(self, size):
        self.size = size  # Инициализация размера хэш-таблицы
        self.table = [[] for _ in range(size)]  # Создание пустой хэш-таблицы заданного размера

    def hash(self, key):
        return hash(key) % self.size  # Вычисление хэша ключа

    def insert(self, key, value):
        index = self.hash(key)  # Получение индекса для вставки
        for k, v in self.table[index]:  # Поиск ключа в соответствующем индексе
            if k == key:
                self.table[index].remove((k, v))  # Удаление существующей пары ключ-значение
                break
        self.table[index].append((key, value))  # Вставка новой пары ключ-значение

    def search(self, key):
        index = self.hash(key)  # Получение индекса для поиска
        for k, v in self.table[index]:  # Поиск ключа в соответствующем индексе
            if k == key:
                return v  # Возвращаем значение, если ключ найден
        return None  # Возвращаем None, если ключ не найден

    def delete(self, key):
        index = self.hash(key)  # Получение индекса для удаления
        for k, v in self.table[index]:  # Поиск ключа в соответствующем индексе
            if k == key:
                self.table[index].remove((k, v))  # Удаление пары ключ-значение
                return v  # Возвращаем значение, если ключ найден
        return None  # Возвращаем None, если ключ не найден


# Простое рехэширование
ht = HashTable1(3)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)
ht.rehash(6)
print(ht.search("apple"))  # 10

# Рехэширование с помощью псевдослучайных чисел
ht = HashTable2(3)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)
ht.insert("date", 40)  # Триггер для рехэширования
print(ht.search("apple"))  # 10

# Метод цепочек
ht = HashTable3(3)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)
ht.insert("apple", 40)  # Обновление значения для ключа "apple"
print(ht.search("apple"))  # 40
ht.delete("banana")
print(ht.search("banana"))  # None
