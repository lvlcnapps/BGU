def first(h):
    try:
        vals = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
        return vals[h]
    except Exception:
        return ""


def second(h):
    try:
        vals = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
                "семнадцать", "восемнадцать", "девятнадцать"]
        return vals[h % 10]
    except Exception:
        return ""


def second_full(h):
    try:
        vals = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто"]
        return vals[h]
    except Exception:
        return ""


def third(h):
    try:
        vals = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
        return vals[h]
    except Exception:
        return ""


def sol():
    try:
        n = int(input('Number: '))
        ans = third(n // 100) + " "
        if not n % 100 // 10 == 1:
            ans += second_full(n % 100 // 10) + " " + first(n % 10)
        else:
            ans += second(n % 100)
        kom = ans.split()
        print(" ".join(kom))
    except Exception:
        print("incorrect input")
