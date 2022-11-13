import random  # импортируем модуль для работы с генерацией рандомных данных
from string import ascii_lowercase, ascii_uppercase, digits  # из модуля string испортируем константы с нужными по условиям задачи значениями


def get_random_password() -> str:
    all_characters = ascii_lowercase + ascii_uppercase + digits  # все символы, которые могут быть использованы для генерации пароля обьединяем в одну стрингу
    some_list = random.sample(all_characters, 8)  # генерируем list из 8ми однозначных строк, символы берем из стринги all_characters
    final_string = ''  # создаем пустую стрингу, куда будем записвать случайные значения
    for char in some_list:  # цикл для перебора списка с сгенерированными строками
        final_string = final_string + char  # обьединяем строки из списка some_list в одну стрингу
    return final_string  # возвращаем итоговую стрингу - в нашем случае пароль


print(get_random_password())


