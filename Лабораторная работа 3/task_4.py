salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение


def get_a_sum_of_money(_salary, _spend, _months, _increase, _need_money):
    grow = _increase + 1
    for money in range(1, months + 1):
        money = _spend - _salary
        _spend = _spend * grow
        _need_money += money

    print(round(_need_money))


get_a_sum_of_money(salary, spend, months, increase, need_money)
