import random as r
import exercises as exe
def load():
    num = r.randint(int(input('Input first ')),int(input('Input second ')))
    guess = input('Guess the number: ')
    if (guess != '!'):
        while (num != int(guess)):
            if (num < int(guess)):
                print('The answer is smaller. Please try again!')
            if (num > int(guess)):
                print('The answer is bigger. Please try again!')
            guess = input('Guess the number: ')
            if (guess == '!'):
                print(f'Halted! The answer was: {num}')
                return
        print(f'Congratulations! The answer was: {num}')
    else:
        print(f'Halted! The answer was: {num}')
    return

def load_2():
    while True:
        str = input('Input string: ')
        if (len(str) < 2):
            print('Input string is too short! Please try again!')
            continue
        count = 0
        for i in range(len(str)):
            for u in range(i, len(str) + 1):
                temp = str[i:u]
                if temp == "":
                    continue
                if (temp == temp[::-1]):
                    # print(f'Founded palindrome: {temp}')
                    count += 1
        print(f'Founded {count} palindromes')
        break
    return

def find_integers(str): # summary & exist
    temp = 0
    summ = 0
    flag = 0
    for i in str:
        if i.isdigit():
            temp *= 10
            temp += int(i)
            flag = 1
        else:
            summ += temp
            temp = 0
    summ += temp
    if flag == 1:
        return summ, True
    return 0, False

def load_3():
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    while True:
        str = input('Input string: ')
        if (str == ""):
            print('Input string is too short! Please try again!')
            continue
        break
    a, b = find_integers(str)
    if (b == True):
        print(f'1-summary: {a}')
        return
    flag = 0
    ans = ""
    for i in str:
        if (i in vowels):
            flag = 1
            ans += i
    if (flag == 1):
        print(f'2-vowels: {ans}')
        return
    print(f'3-last symbol: {str[-1]}')
    return

def load_4():
    while True:
        str = input('Input string: ')
        flag = 0
        for i in str:
            if (not i.isalpha()):
                flag = 1
                print('Input string is invalid! Please try again!')
                break
        if (flag == 0):
            break

    while True:
        n = int(input('Input a number: '))
        if (0 < n <= len(str)):
            break

    for i in range(len(str)):
        for u in range(i, len(str) + 1):
            if (len(str[i:u]) == n) and (len(str[i:u]) != 0):
                # print(str[i:u])
                used = []
                flag = 0
                for j in (str[i:u]):
                    if (not j in used):
                        used.append(j)
                    else:
                        flag = 1
                        break
                if (flag == 0):
                    print(str[i:u])
    return


if __name__ == '__main__':
    exe.Exercises(5)