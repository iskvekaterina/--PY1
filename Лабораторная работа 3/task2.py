def get_count_char(str_):
    src_str = "".join(str_.split())  # избавляемся от пробелов и переносов стро
    src_str = src_str.lower()  # приводим строку к нижнему регистру
    src_str = src_str.replace('.', '')  # убираем знаки препинания
    src_str = src_str.replace(',', '')
    src_str = src_str.replace('!', '')
    final_dict = {}  # создаем пусой словарь для наполнения
    for char in src_str:  # перебираем все символы преобразованной строки
        if char in final_dict:  # проверяем, есть ли в словаре указанный ключ
            final_dict[char] += 1  # если есть - прибавляем к исходному значению ключа 1
        else:
            final_dict[char] = 1  # иначе создаем в словаре пару с новым ключем и присваиваем значение 1
    return final_dict  # возвращаем итоговый словарь


def get_percentage_char(dict_=None):
    total_char_count = 0
    for char in dict_:
        total_char_count += dict_[char]  # получаем общее число символов
    for char in dict_:
        dict_[char] = round(dict_[char]*100/total_char_count, 2)  # переводчим численное значение в процентное, округляем до 2х значений после запятой
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_percentage_char(get_count_char(main_str)))
