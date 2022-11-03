list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

L = len(list_numbers)

for i, value in enumerate(list_numbers):
    if value == max(list_numbers):
        list_numbers[i], list_numbers[L - 1] = list_numbers[L - 1], list_numbers[i]
        break

print(list_numbers)