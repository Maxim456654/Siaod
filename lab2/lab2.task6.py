def sort():
    rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    stack_numbers = []
    stack_letters_rus = []
    stack_letters_eng = []
    stack_other = []

    with open('text.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            for i in line:
                if i.isdigit():
                    stack_numbers.append(i)
                elif i.isalpha():
                    if i.lower() in rus:
                        stack_letters_rus.append(i)
                    else:
                        stack_letters_eng.append(i)
                else:
                        stack_other.append(i)
    return stack_letters_rus, stack_letters_eng, stack_numbers, stack_other


for i, stack in enumerate(sort()):
    print(stack)

