import Game

game = Game.Game()
try:
    n = int(input('Enter number of axis: '))
    cords = [[], []]
    print(f'Print {n} coords for player 1')
    for i in range(n):
        cords[0].append(int(input()))
    print(f'Print {n} coords for player 2')
    for i in range(n):
        cords[1].append(int(input()))
    print(cords)
    game.start(cords, int(input('Max steps: ')), int(input('Runner speed: ')), int(input('Chaser speed: ')))
except Exception:
    game.start()
