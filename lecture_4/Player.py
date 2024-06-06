class Player:
    def __init__(self, chaser=False, cords=None, speed=1, max_speed=2):
        if cords is None:
            self.cords = [0, 0]
        self.chaser = chaser
        self.cords = cords
        self.speed = max_speed if self.chaser else speed

    def move_player(self, command):  # command: axis-direction
        kom = command.split()
        try:
            axis = int(kom[0]) - 1
            direction = int(kom[1])
            if axis > len(self.cords) or axis < 0:
                raise Exception
            if direction != 1 and direction != -1:
                raise Exception
            self.cords[axis] += direction * self.speed
            print(f'New coords: {self.cords}')
        except Exception:
            print('Invalid command')
            return
