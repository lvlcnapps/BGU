import time


def count_ways(n):
    def rec_find(n, temp=None):
        if temp is None:
            temp = {}

        if n in temp:
            return temp[n]

        if n == 0:
            return 1
        if n == 1:
            return 1

        temp[n] = rec_find(n - 1, temp) + rec_find(n - 2, temp)
        return temp[n]
    return rec_find(n - 1)


def tricky_solution(n):
    n -= 1
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b

    return a


n = int(input("Введите количество ступенек: "))
print(f"Количество способов подняться на {n} ступенек: {count_ways(n)}\n")
print("☻Хитрое решение????? (в среднем в 10 раз быстрее чем рекурсией):")
print(f"Количество способов подняться на {n} ступенек: {tricky_solution(n)}")
