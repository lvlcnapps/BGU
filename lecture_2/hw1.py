def sol():
    try:
        n = int(input('Number of rows: '))
        for i in range(n):
            print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    except Exception:
        print("incorrect input")
