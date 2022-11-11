import random
def get_unique_list_numbers() -> list:
    list_n = []
    for i in range(15):
        while 1:
            rand_n = random.randint(-10, 10)
            if rand_n not in list_n:
                list_n.append(rand_n)
                break

    return list_n

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers))
