plays = 0.0
max_sides = int(input('Input sides: '))
min = max_sides
max = 1
print('ROLLS:')
n = 1
sub = 0
max_sub = 0
max_sub_vals = []
temp_sub_vals = []
past = 0
while True:
    # input
    while True:
        pl = int(input('Input roll: '))
        if max_sides >= pl >= 0:
            break
    # exit
    if pl == 0:
        print('ROLLS END')
        print('FINISH:')
        print(f'min - {min}')
        print(f'max - {max}')
        print(f'avg - {plays}')

        print(f'max sub length - {len(max_sub_vals)} - {max_sub_vals}')
        continue
    # avg, min and max
    plays = (plays * (n - 1) + pl) / n
    n += 1
    if pl > max:
        max = pl
    if pl < min:
        min = pl
    # subs
    if past < pl:
        sub += 1
        temp_sub_vals.append(pl)
    else:
        temp_sub_vals = [pl]
        sub = 1
    if sub > max_sub:
        max_sub = sub
        max_sub_vals = temp_sub_vals
    past = pl