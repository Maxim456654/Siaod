def spisok():

    with open("numbers.text", "r") as file:
        deque = file.readlines()
        for i in deque:
            list = [i.strip() for i in deque]
    return list


list1 = spisok()
print(list1)
def sort_numbers():
    first_deque = []
    second_deque = []
    while list1:
        aaa = list1.pop()
        if aaa.isdigit():
            print(aaa)
            if int(aaa) >= 0:
                first_deque.append(aaa)
        elif int(aaa) < 0:
            second_deque.append(aaa)
    return first_deque, second_deque

print(sort_numbers())














