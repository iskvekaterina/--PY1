import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:  # создаем метод для преобразования csv в list_with_dicts
    final_list = []  # создаем список, который будет возвращать после наполнения данными
    with open(filename) as f:  # открываем файл в режиме чтения
        list_with_lines = []  # создаем пустой список, куда будем складывать массивы с значениями строк текущего csv файла
        for line in f:  # в цикле перебираем csv файл по строкам
            values_from_line = line.split(",")  # формируем список из значений строки, ориентируясь на разделитель ','
            for value in values_from_line:  # перебираем значения списка, чтобы убрать '\n' из значений списка (встречается в последнем значении списка)
                if '\n' in value:  # вычисляем строки, где встречается \n
                    values_from_line[values_from_line.index(value)] = value.strip('\n')  # заменяем значение строки на то же, но исключив '\n'
            list_with_lines.append(values_from_line)  # складываем списки в список для дольнейшей обрботки (формирования списка диктов)
        for current_raw in list_with_lines[1:]:  # перебираем все списки кроме первого (первый - заголовки)
            dict_for_raw = {}  # создаем пустой дикт для наполнения
            for raw_value in current_raw:  # перебираем значения списка с значенниями
                dict_for_raw.update({list_with_lines[0][current_raw.index(raw_value)]: raw_value})  # записываем ключ:значение в дикт
            final_list.append(dict_for_raw)  # в финальный лист добавляем сформированные дикты
        return final_list  # возвращаем наполненный лист с диктами


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
