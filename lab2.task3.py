import random

n = int(input('кол-во дисков: '))
min = int(input('мин значение рамзера диска: '))
max = int(input('макс значение размера диска: '))


def move_disk(sterzhen, source, destination):
    disk = sterzhen[source].pop()
    sterzhen[destination].append(disk)
    print(f"Move disk {disk} from {source} to {destination}")


def hanoi_recursive(n, sterzhen, source, auxiliary, destination):
    if n > 0:
        hanoi_recursive(n-1, sterzhen, source, destination, auxiliary)
        move_disk(sterzhen, source, destination)
        hanoi_recursive(n-1, sterzhen, auxiliary, source, destination)


def solve_hanoi():
    hanoi_recursive(n, sterzhen, 'A', 'B', 'C')


sterzhen = {'A': [], 'B': [], 'C': []}
for i in range(n):
    sterzhen['A'].append(random.randint(min, max))
    sterzhen['A'].sort(reverse=True)
print(sterzhen['A'])

solve_hanoi()