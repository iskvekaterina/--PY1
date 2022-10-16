money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
grow = 1.05

month = 0  # количество месяцев, которое можно прожить
# TODO Оформить решение


def get_month_count(_money_capital, _salary, _spend, _grow, _month):
    delta = _salary - _spend
    while _money_capital + delta >= _spend:
        _money_capital += delta
        _spend = spend * grow
        _month += 1
    print(_month)


get_month_count(money_capital, salary, spend, increase, month)
