# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1
# 2
# 5
# Output:
# 1, 3, 5, 7, 9

def arith_progression(base: int, step: int, len_array: int) -> list:
    return [(base + (el_num - 1) * step) for el_num in range(1, len_array + 1)]

base_number = int(input('Введите первый элемент арифметической прогрессии: '))
difference = int(input('Введите значение разности между элементами прогрессии: '))
amount_elements = int(input('Введите количество элементов прогрессии: '))

print(*arith_progression(base_number, difference, amount_elements))