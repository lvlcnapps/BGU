import Player as pl


class Game:
    def __init__(self):
        self.steps = 1
        self.running = True

    def start(self, cords=None, max_steps=10):
        if cords is None:
            cords = [[0, 0], [10, 0]]
        self.steps = 1
        pl1 = pl.Player(cords=cords[0])
        pl2 = pl.Player(chaser=True, cords=cords[1])
        while self.running:
            self.loop(pl1, pl2, max_steps)

    def loop(self, pl1, pl2, max_steps):
        print(f'Step number {self.steps}')
        pl1.move_pl(input('Player 1 move: '))
        pl2.move_pl(input('Player 2 move: '))
        self.steps += 1
        self.check_win(pl1, pl2, max_steps)

    def check_win(self, pl1, pl2, max_steps):
        if self.steps > max_steps:
            print('Player 1 wins!')
            self.stop()
            return
        sum_quad = 0
        for i in range(len(pl1.cords)):
            sum_quad += (pl1.cords[i] - pl2.cords[i]) ** 2
        if sum_quad <= len(pl1.cords):
            print('Player 2 wins!')
            self.stop()
            return

    def stop(self):
        self.running = False
