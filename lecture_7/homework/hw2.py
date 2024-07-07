def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = gcd(num1, num2)
print(f"Наибольший общий делитель {num1} и {num2} равен {result}")
