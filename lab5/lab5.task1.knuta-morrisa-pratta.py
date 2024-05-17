import time

def compute_prefix_function(pattern):
    m = len(pattern)  # Длина подстроки pattern
    prefix = [0] * m  # Создаем массив префиксов длины m, заполненный нулями
    k = 0  # Инициализируем переменную k для сравнения символов
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k - 1]  # Уменьшаем k на значение префикса предыдущего символа
        if pattern[k] == pattern[q]:  # Если символы совпадают
            k += 1
        prefix[q] = k  # Записываем значение k в массив префиксов
    return prefix

def kmp_search(text, pattern):
    n = len(text)  # Длина строки text
    m = len(pattern)  # Длина подстроки pattern
    prefix = compute_prefix_function(pattern)  # Вычисляем префикс-функцию для подстроки pattern
    q = 0  # Инициализируем переменную q для сравнения символов
    for i in range(n):  # Проходим по индексам строки text
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q - 1]  # Уменьшаем q на значение префикса предыдущего символа
        if pattern[q] == text[i]:
            q += 1
        if q == m:  # Если q равно длине подстроки pattern
            print(f"Подстрока найдена на позиции {i - m + 1}")
            q = prefix[q - 1]  # Уменьшаем q на значение префикса последнего символа

if __name__ == "__main__":
    text = input("Введите строку: ").strip()
    pattern = input("Введите подстроку: ").strip()
    case_sensitive = input("Чувствительность к регистру (y/n)? ").strip().lower() == "y"

    if not case_sensitive:
        text = text.lower()
        pattern = pattern.lower()

    start_time = time.time()
    kmp_search(text, pattern)
    elapsed_time = time.time() - start_time
    print(f"Время работы алгоритма КМП: {elapsed_time:.6f} секунд")
    start_time = time.time()
    occurrences = [i for i in range(len(text) - len(pattern) + 1) if text[i:i + len(pattern)] == pattern]
    elapsed_time = time.time() - start_time
    print(f"Время работы стандартной функции поиска: {elapsed_time:.6f} секунд")
