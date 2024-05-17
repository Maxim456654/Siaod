def check_balance():
    deque = []

    with open('balance.txt', 'r') as file:
        for line in file:
            for i in line:
                if i == '[':
                    deque.append(i)
                elif i == ']':
                    if not deque:
                        return False
                    deque.pop()

    if not deque:
        return True
    else:
        return False


if check_balance():
    print("Квадратные скобки сбалансированы")
else:
    print("Квадратные скобки не сбалансированы")