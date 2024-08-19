def sum_until_negative(mas: list) -> int:
    sum = 0
    for i in mas:
        if i < 0:
            return sum
        sum += i
    return sum

print(sum_until_negative([1, 2, 3, -1, 4, 5]))

print(sum_until_negative([1, 2, 3, 4, 5]))