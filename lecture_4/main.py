import Game as g

game = g.Game()

try:
    n = int(input('Enter number of axis: '))
    cords = []
    player_1 = []
    player_2 = []
    print(f'Print {n} coords for player 1')
    for i in range(n):
        player_1.append(int(input()))
    print(f'Print {n} coords for player 2')
    for i in range(n):
        player_2.append(int(input()))
    cords.append(player_1)
    cords.append(player_2)
    print(cords)
    game.start(cords, int(input('Max steps: ')))
except Exception:
    game.start()
