#Задание 2

deque = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
name = ("MAKSIMZ")


def shifr(array):
    shifr_name = ''
    for j in array:
        name_id = j
        if name_id in deque:
            index = deque.index(name_id)
            shifr_index = (index + 2) % len(deque)
            shifrr = deque[shifr_index]
            shifr_name += shifrr
    return shifr_name


shifr_name = shifr(name)
print(shifr(name))


def unshifr(array):
    unshifr_name = ''
    for i in array:
        if i in deque:
            shifr_index = deque.index(i)
            unshifr_index = (shifr_index - 2) % len(deque)
            unshifr_name += deque[unshifr_index]
    return(unshifr_name)


print(unshifr(shifr_name))
