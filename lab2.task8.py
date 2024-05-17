def reverse_file():
    stack = []

    with open('fff.txt', 'r') as file:
        stack = file.readlines()
        for i in stack:
            array = [i.strip() for i in stack]
    return array

print(reverse_file())

stack_new = reverse_file()
new_file = open('ggg.txt', 'w')
while stack_new:
    aaa = stack_new.pop()
    new_file.write(str(aaa) + '\n')
new_file.close
