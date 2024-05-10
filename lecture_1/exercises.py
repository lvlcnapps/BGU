class Exercises():
    def __init__(self, id):
        self.id = id
        if id == 1:
            self.load_1()
        if id == 2:
            self.load_2()
        if id == 3:
            self.load_3()
        if id == 5:
            self.load_5()

    def load_1(self):
        a = int(input('Write first number: '))
        b = int(input('Write second number: '))
        c = int(input('Write third number: '))
        if (a ** 2 + b ** 2 == c ** 2 and a <= b <= c):
            print('Yes')
        else:
            print('No')

    def load_2(self):
        while True:
            str = input('Input string: ')
            if (len(str) < 3):
                print('Wrong string. Please try again.')
                continue
            break
        count = 0
        for i in range(len(str) - 2):
            if str[i:i+3] == 'tot':
                count += 1
        print(f'Founded "tot": {count}')

    def load_3(self):
        while True:
            str = input('Input string: ')
            flag = 0
            for i in str:
                if not (i.isalpha() and i.islower()):
                    print('Illegal input. Try again')
                    flag = 1
                    break
            if flag == 0:
                break

        k = int(input('Input number: '))
        if k < 0:
            vowels = ['a', 'u', 'i', 'o', 'y', 'e']
            count = 0
            for i in str:
                if i in vowels:
                    count += 1
            print(f'Founded {count} vowels')
            return
        if k < len(str):
            print(f'First  slice: {str[:k]}')
            print(f'Second  slice: {str[k:]}')
        else:
            print(f'Reversed string: {str[::-1]}')

    def load_4(self):
        str = input('Input string: ').lower()
        max_sub = 0
        for i in range(len(str)):
            if not str[i].isalpha():
                print('Illegal input')
                break
            for u in range(i, len(str) + 1):
                if str[i:u] == ''.join(sorted(str[i:u])) and len(str[i:u]) > 0:
                    if len(str[i:u]) > max_sub:
                        max_sub = len(str[i:u])
        print(f'Max size: {max_sub}')

    def load_5(self):
        k = int(input('Input number: '))
        if k < 0:
            print('Illegal input. Please try again.')
            return
        s = str(k)

        ans = 0
        while k != 0:
            ans = ans * 10
            ans += k % 10
            k //= 10
        print(f'Math solution: {ans}')
        print(f'String solution: {int(s[::-1])}')