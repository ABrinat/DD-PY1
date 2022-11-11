import random
def get_random_password(num: int = 8) -> str:
    symbols = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    symbol_l = random.sample(symbols, num)
    password = ''.join(symbol_l)
    return password
print(get_random_password())