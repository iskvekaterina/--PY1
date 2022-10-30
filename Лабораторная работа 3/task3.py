def delete(list_, index=None):
    if index is None:  # если None - аргумен с индексом не передан
        list_.pop()  # убираем последний элемент из списка
    else:  # если не None - аргумен с индексом передан
        list_.pop(index)  # убираем элемент с указанным индексом из списка
    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
