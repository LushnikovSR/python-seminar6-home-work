# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)

from typing import Union

def find_indexes_elements(arr: Union[list, tuple[int, ...]], min: int, max: int) -> list:
    return [f'{i}({arr[i]})' for i in range(len(arr)) if arr[i] >= min and arr[i] <= max]


print('Задайте массив, введите целые числа через пробел:')
array = [int(num) for num in input().split()]
lower_bound = int(input('Задайте нижнюю границу диапазона поиска: '))
upper_bound = int(input('Задайте верхнюю границу диапазона поиска: '))

print(*find_indexes_elements(array, lower_bound, upper_bound))