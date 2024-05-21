def sol():
    try:
        n = int(input('Number: '))
        while n > 9:
            n = sum([int(i) for i in str(n)])
        print(n)
    except Exception:
        print("incorrect input")
