def check_balance():
    stack = []

    with open('balance.txt', 'r') as file:
        for line in file:
            for char in line:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if not stack:
                        return False
                    stack.pop()

    if not stack:
        return True
    else:
        return False


if check_balance():
    print("Скобки сбалансированы")
else:
    print("Скобки не сбалансированы")