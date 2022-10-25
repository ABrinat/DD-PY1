def delete(list_, index=None):
    lenf = len(list_)
    if index is None:
        l = list_[: (lenf - 1)]
    elif index < 0:
        index = index + lenf
        l = list_[: (index)] + list_[(index + 1) :]
    else:
        l = list_[: (index)] + list_[(index + 1) :]
    return l


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]


