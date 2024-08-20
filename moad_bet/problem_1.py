def find_max(lst) -> int:
    if len(lst) == 0:
        return -1000000
    if type(lst[0]) == int:
        if len(lst) == 1:
            return lst[0]
        return max(lst[0], find_max(lst[1:]))
    else:
        if len(lst) == 1:
            return find_max(lst[0])
        return max(find_max(lst[0]), find_max(lst[1:]))

print(find_max([1, 3, [4, 5, [10, 50]], 2]))
