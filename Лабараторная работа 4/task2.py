def get_count_char(str_):
    count_char = {}
    lower_str = str_.lower()
    for ch in lower_str:
        if ch.isalpha() == False:
            continue
        else:
            if ch in count_char:
                count_char[ch] += 1
            else:
                count_char[ch] = 1
    return count_char


def procent(count_char):
    total_count = sum(count_char.values())
    for char, num in count_char.items():
        pr = (num / total_count) * 100
        count_char[char] = pr
    return count_char



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

print(procent(get_count_char(main_str)))
