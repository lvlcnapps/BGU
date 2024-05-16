import math
def result(a,b): # 0 - rock, 1 - paper, 2 - scissors
    if (a == b):
        return 0
    rz = a - b
    if (rz < 0):
        rz += 3
    return rz

def start4():
    while True:
        print("input rock, paper or scissors")
        numb = int(input('Number of players: '))
        if numb < 2:
            print("Number of players must be more than 1")
            continue
        if numb > 5:
            print("Number of players must be less than 5")
            continue
        inputs = []
        for i in range(numb):
            print(f"Player {i+1}: ", end="")
            inputs.append(input())
        ids = list(range(numb))
        for i, val in enumerate(inputs):
            if val == "rock":
                ids[i] = 0
            if val == "paper":
                ids[i] = 1
            if val == "scissors":
                ids[i] = 2

        uniq = list(set(ids))
        if len(uniq) == 1 or len(uniq) == 3:
            print("Draw")
            continue

        #print(uniq)
        ans = uniq[result(uniq[0], uniq[1]) - 1]
        if ans == 0:
            print("Rock win")
        if ans == 1:
            print("Paper win")
        if ans == 2:
            print("Scissors win")

def find_prime_numbers(n):
    prime_numbers = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers

def resheto_eratosphena(n):
    numbers = [i for i in range(0, n)]
    primes = []
    for i in range(2, n):
        if numbers[i] != 0:
            primes.append(numbers[i])
            for j in range(i * i, n, i):
                numbers[j] = 0
    return primes


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start4()