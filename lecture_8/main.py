class Date():
    def __init__(self, in_id, dd, mm, yy):
        self.id = in_id
        self.day = dd
        self.month = mm
        self.year = yy

    def isequal(self, d2):
        if self.day == d2.day and self.month == d2.month and self.id != d2.id:
            return True
        return False

    def __repr__(self):
        return f'({self.day}:{self.month}:{self.year})'

import random as r
class DateGen():
    def __init__(self):
        self.dates = []
        self.rand_arr = r.sample(range(1, 10000), 9999)

    def gen(self):
        dd = r.randint(1, 31)
        mm = r.randint(1, 12)
        yy = r.randint(1970, 2024)
        if mm in (4, 6, 9, 11) and dd == 31:
            dd = 30
        if mm == 2 and yy % 4 == 0 and dd > 29:
            dd = 29
        if mm == 2 and yy % 4 != 0 and dd > 28:
            dd = 28
        self.dates.append(Date(self.rand_arr.pop(r.randint(0, len(self.rand_arr) - 1)), dd, mm, yy))
        return self.dates


app = DateGen()
for i in range(int(input('Input number of dates: '))):
    app.gen()
print(app.dates)
for i in app.dates:
    flag = 0
    for u in app.dates:
        if i.isequal(u):
            flag += 1
            print(f'pair - {i} | {u}')