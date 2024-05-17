def is_safe(board, row, col, n):
    # Проверка строки слева
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Проверка левой верхней диагонали
    j = col
    i = row
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Проверка левой нижней диагонали
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens(board, col, n):
    # Если все ферзи размещены, вывести решение и вернуть True
    if col == n:
        print_solution(board, n)
        return True

    # Попробовать разместить ферзя в каждой строке текущего столбца
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            # Рекурсивно разместить остальных ферзей
            if solve_n_queens(board, col + 1, n):
                return True

            # Если решение не найдено, отменить размещение ферзя
            board[row][col] = 0

    # Если не удалось разместить ферзя в текущем столбце, вернуть False
    return False


def print_solution(board, n):
    for row in range(n):
        for col in range(n):
            print(board[row][col], end=" ")
        print()
    print()


# Инициализация доски
n = 8
board = [[0 for j in range(n)] for i in range(n)]

# Решение задачи
solve_n_queens(board, 0, n)
