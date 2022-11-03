money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение



while 1:
    money_capital -= spend
    if money_capital < 0:
        break
    pr = 1 + increase
    spend *= pr
    month += 1
    money_capital += salary

print(month)
