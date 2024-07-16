import random
import string
from creature import Creature


class Game:
    def __init__(self):
        print("Started")
        self.types = []
        self.creatures = []
        self.food = 0

    def __random_type(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def __generate_types(self, n):
        types = []
        for i in range(n):
            types.append(self.__random_type(5))
        patterns = []
        for i in range(n):
            type_c = {'type': types[i]}  # type, eat_type, max_age, habitat
            if random.randint(0, 3) == 0:  # hunter
                type_c['eat_type'] = types[random.randint(0, n - 1)]
            else:  # herbivore
                type_c['eat_type'] = 'green'
            type_c['max_age'] = random.randint(15, 25)  # max_age
            if random.randint(0, 2) == 0:  # habitat
                type_c['habitat'] = 'water'
            elif random.randint(0, 1) == 0:
                type_c['habitat'] = 'air'
            else:
                type_c['habitat'] = 'earth'
            patterns.append(type_c)
        return patterns

    def add_food(self, n):
        self.food += n
        return self.food

    def make_creature(self, pattern, sex, saturation, age, size):
        self.creatures.append(Creature(pattern['type'], pattern['eat_type'], pattern['max_age'], pattern['habitat'],
                                       sex, saturation, age, size))
        return

    def show_creatures(self):
        print('--------------')
        for i, val in enumerate(self.creatures):
            print(f'ID: {i}')
            print(val)
            print('--------------')
        return

    def show_types(self):
        for i in self.types:
            print(i)
        return

    def show_food(self):
        print(self.food)
        return

    def show_creature(self, num):
        try:
            print(self.creatures[num])
        except Exception:
            print("No such creature")
        return

    def start(self):
        self.types = self.__generate_types(int(input('Введите количество типов: ')))
        # print(self.types)
        n = int(input('Введите количество создаваемых существ: '))
        for i in range(n):
            self.make_creature(self.types[random.randint(0, len(self.types) - 1)], random.randint(0, 1),
                               random.randint(15, 100), random.randint(0, 10), random.randint(1, 10))
        self.__loop()
        return

    def __loop(self):
        while True:
            command = input('Введите команду: ')
            if command == 'show':
                self.show_creatures()
            elif command == 'show_types':
                self.show_types()
            elif command == 'show_food':
                self.show_food()
            elif command == 'show_creature':
                self.show_creature(int(input('Введите номер существа: ')))
            elif command == 'add_food':
                self.add_food(int(input('Введите количество еды: ')))
            elif command == 'repr':  # reproduction
                cr1 = int(input('Введите номер первого существа: '))
                cr2 = int(input('Введите номер второго существа: '))
                if self.creatures[cr1].is_ready_to_fuck(self.creatures[cr2]):
                    print('Размножение прошло успешно')
                    if self.creatures[cr1].habitat == 'water':
                        for i in range(10):
                            self.creatures.append(Creature(self.creatures[cr1].type, self.creatures[cr1].eat_type,
                                                  self.creatures[cr1].max_age, self.creatures[cr1].habitat,
                                                  random.randint(0, 1), 23, 1, random.randint(1, 10)))
                    if self.creatures[cr1].habitat == 'air':
                        for i in range(4):
                            self.creatures.append(Creature(self.creatures[cr1].type, self.creatures[cr1].eat_type,
                                                  self.creatures[cr1].max_age, self.creatures[cr1].habitat,
                                                  random.randint(0, 1), 64, 1, random.randint(1, 10)))
                    if self.creatures[cr1].habitat == 'earth':
                        for i in range(2):
                            self.creatures.append(Creature(self.creatures[cr1].type, self.creatures[cr1].eat_type,
                                                  self.creatures[cr1].max_age, self.creatures[cr1].habitat,
                                                  random.randint(0, 1), 73, 1, random.randint(1, 10)))
                else:
                    print('Размножение не удалось')
                # print('Неверный ввод')
            elif command == 'step':
                for i, val in enumerate(self.creatures):
                    a = val.step(self.food, self.creatures, i)
                    self.food = a[0]
                    self.creatures = a[1]
                for i in self.creatures:
                    if i.live == 0:
                        self.creatures.remove(i)
                        del i
            elif command == 'exit':
                break
            else:
                print('Неверная команда')
        return


g = Game()
g.start()
