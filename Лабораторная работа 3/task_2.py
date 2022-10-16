list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_number = max(list_numbers)
index_max_number = list_numbers.index(max_number)

list_numbers[index_max_number], list_numbers[-1] = list_numbers[-1], list_numbers[index_max_number]

print(list_numbers)
