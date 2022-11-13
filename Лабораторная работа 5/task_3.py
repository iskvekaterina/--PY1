import random  # импортируем подходящий модуль для генерации случайных чисел


def get_unique_list_numbers() -> list[int]:
    final_list = []  # создаем пустой список, в который будут добавлены подходящие элементы
    while len(final_list) != 15:  # цикл будет выполняться до тех пор, пока в списоке не будет ожидаемого числа элементов
        random_int = random.randrange(-10, 10)  # создем рандомный integer от -10 до 10
        if random_int not in final_list:  # проверяем, есть ли элемент в списке
            final_list.append(random_int)  # если нету, добавляем новйы уникальный элемент
    return final_list  # возвразаем итоговый спиоск


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
