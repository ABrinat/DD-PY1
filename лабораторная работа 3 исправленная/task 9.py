salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
for i in range(months):
    current_need = spend - salary
    need_money += current_need
    spend = (1 + increase) * spend

print(round(need_money))
