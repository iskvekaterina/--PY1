# TODO решить с помощью list comprehension и распечатать его
import pprint

final_list = []  # создаем пустой список, в который будут добавлены dictionaries
for dec_digit in range(16):  # перебираем числа от 0 до 15
    dict_with_digit = {  # создаем словарь с нужными парами ключ / значение
        'bin': bin(dec_digit),
        'dec': dec_digit,
        'hex': hex(dec_digit),
        'oct': oct(dec_digit)
    }
    final_list.append(dict_with_digit)  # каждый словарь будет добавлен в ранее созданный список

pprint.pprint(final_list)  # выводим список с содержимих хранимых объектов
