# Задание 1
from collections import deque

# Создание двух деков
first_deque = deque()
second_deque = deque()

# Чтение названий книг из файла и добавление их в первый дек
with open('books.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        book_title = line.strip()  # Удаление лишних пробелов и символов перевода строки
        first_deque.append(book_title)

# Сортировка названий книг с использованием двух деков
while first_deque:
    book_title = first_deque.pop()  # извлекаем
    # Вставка названия книги вторым деком в алфавитном порядке
    if not second_deque or book_title > second_deque[-1]:  # пока пустой
        second_deque.append(book_title)
    else:
        while second_deque and book_title < second_deque[-1]:  # пока непустой
            first_deque.append(second_deque.pop())
        second_deque.append(book_title)

# Вывод отсортированных названий книг
for i, name in enumerate(second_deque):
    print(i+1, name)