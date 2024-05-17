from collections import defaultdict


def boyer_moore(pattern, text, case_insensitive=False):
    if case_insensitive:
        pattern = pattern.lower()
        text = text.lower()

    m = len(pattern)
    n = len(text)

    if m > n:  # Если длина подстроки больше длины текста
        return -1

    last = defaultdict(lambda: -1)  # Создаем словарь с значением по умолчанию -1

    for i in range(m):  # Проходим по индексам подстроки
        last[pattern[i]] = i  # Запоминаем последнее вхождение символа в подстроке

    i = m - 1
    k = m - 1

    while i < n:  # Пока i меньше длины текста
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j < 0:  # Если условие выполняется, то подстрока найдена
            return i + 1  # Возвращаем позицию, на которой найдена подстрока
        i += max(k - j, 1)  # Увеличиваем i на максимум из (k - j, 1)
        k = max(1, j - last[text[i]])  # Обновляем k

    return -1


def main():
    text = input("Введите строку: ")
    pattern = input("Введите подстроку: ")
    case_insensitive = input("Учитывать регистр? (y/n): ").lower() == 'n'

    start_time = time.time()
    result = boyer_moore(pattern, text, case_insensitive)
    end_time = time.time()
    boyer_moore_time = end_time - start_time

    start_time = time.time()
    result_builtin = text.find(pattern, 0, len(text)) if not case_insensitive else text.lower().find(pattern.lower(), len(text))  # Выполняем поиск с использованием встроенной функции
    end_time = time.time()
    builtin_time = end_time - start_time

    if result == -1:
        print("Подстрока не найдена")
    else:
        print(f"Подстрока найдена на позиции {result}")
    print(f"Время работы алгоритма Бойера-Мура: {boyer_moore_time:.6f} секунд")
    print(f"Время работы встроенной функции: {builtin_time:.6f} секунд")


if __name__ == "__main__":
    import time

    main()
