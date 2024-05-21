def first(h):
    if h == 1:
        return "один"
    if h == 2:
        return "два"
    if h == 3:
        return "три"
    if h == 4:
        return "четыре"
    if h == 5:
        return "пять"
    if h == 6:
        return "шесть"
    if h == 7:
        return "семь"
    if h == 8:
        return "восемь"
    if h == 9:
        return "девять"
    return ""


def second(h):
    if h == 10:
        return "десять"
    if h == 11:
        return "одиннадцать"
    if h == 12:
        return "двенадцать"
    if h == 13:
        return "тринадцать"
    if h == 14:
        return "четырнадцать"
    if h == 15:
        return "пятнадцать"
    if h == 16:
        return "шестнадцать"
    if h == 17:
        return "семнадцать"
    if h == 18:
        return "восемнадцать"
    if h == 19:
        return "девятнадцать"
    return ""


def second_full(h):
    if h == 2:
        return "двадцать "
    if h == 3:
        return "тридцать "
    if h == 4:
        return "сорок "
    if h == 5:
        return "пятьдесят "
    if h == 6:
        return "шестьдесят "
    if h == 7:
        return "семьдесят "
    if h == 8:
        return "восемьдесят "
    if h == 9:
        return "девяносто "
    return ""


def third(h):
    if h == 1:
        return "сто "
    if h == 2:
        return "двести "
    if h == 3:
        return "триста "
    if h == 4:
        return "четыреста "
    if h == 5:
        return "пятьсот "
    if h == 6:
        return "шестьсот "
    if h == 7:
        return "семьсот "
    if h == 8:
        return "восемьсот "
    if h == 9:
        return "девятьсот "
    return ""


def sol():
    try:
        n = int(input('Number: '))

        ans = third(n // 100)
        if second(n % 100) == "":
            ans += second_full(n % 100 // 10) + " " + first(n % 10)
        else:
            ans += second(n % 100)
        print(ans)
    except Exception:
        print("incorrect input")