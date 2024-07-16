class Creature:
    def __init__(self, type, eat_type, max_age, habitat, sex, saturation, age, size):
        self.live = 1
        self.type = type
        self.eat_type = eat_type
        self.max_age = max_age
        self.habitat = habitat
        self.sex = sex
        self.saturation = saturation
        self.age = age
        self.size = size
        # print("Creature created")

    def print_info(self):
        print(
            f"Type: {self.type}\nEat type: {self.eat_type}\nMax age: {self.max_age}\nHabitat: {self.habitat}\nSex: {self.sex}\nSaturation: {self.saturation}\nAge: {self.age}\nSize: {self.size}")
        return [self.type, self.eat_type, self.max_age, self.habitat, self.sex, self.saturation, self.age, self.size]

    def str_info(self):
        return f"Type: {self.type}\nEat type: {self.eat_type}\nMax age: {self.max_age}\nHabitat: {self.habitat}\nSex: {self.sex}\nSaturation: {self.saturation}\nAge: {self.age}\nSize: {self.size}"

    def is_ready_to_fuck(self, cr2):
        if self.type == cr2.type and self.sex != cr2.sex:
            if self.habitat == 'water':
                if self.saturation > 50 and cr2.saturation > 50:
                    return True
            if self.habitat == 'air':
                if self.saturation > 42 and cr2.saturation > 42 and self.age > 3 and cr2.age > 3:
                    return True
            if self.habitat == 'earth':
                if self.saturation > 20 and cr2.saturation > 20 and self.age > 5 and cr2.age > 5:
                    return True
        return False

    def step(self, food, list_crs, id_c) -> (int, list):
        self.age += 1
        if self.live == 0:
            return food, list_crs
        if self.age >= self.max_age:
            print(f'Creature №{id_c} died because of age! Food increased by {self.size}')
            s = self.size
            self.live = 0
            return food + s, list_crs
        if self.eat_type == 'green':
            if food > 0:
                print(f'Creature №{id_c} ate some food! Food decreased by 1')
                self.saturation += 26
                if self.saturation > 100:
                    self.saturation = 100
                food -= 1
            else:
                print(f'Creature №{id_c} in search of food! Saturation decreased by 9')
                self.saturation -= 9
                if self.saturation < 10:
                    print(f'Creature №{id_c} died because of saturation! Food increased by {self.size}')
                    s = self.size
                    self.live = 0
                    return food + s, list_crs
        else:
            flag = 0
            for i in list_crs:
                if i.type == self.eat_type:
                    flag = 1
                    import random as r
                    if r.randint(0, 1) == 1:
                        print(f'Creature №{id_c} ate creature №{list_crs.index(i)}! Saturation increased by 53')
                        self.saturation += 53
                        if self.saturation > 100:
                            self.saturation = 100
                        list_crs.remove(i)
                        break
                    else:
                        print(
                            f'Creature №{id_c} failed to eat creature №{list_crs.index(i)}! Saturation decreased by 16')
                        self.saturation -= 16
                        if self.saturation < 10:
                            print(f'Creature №{id_c} died because of saturation! Food increased by {self.size}')
                            s = self.size
                            del self
                            food += s
                        break
            if flag == 0:
                print(f'Creature №{id_c} in search of food! Saturation decreased by 16')
                self.saturation -= 9
                if self.saturation < 10:
                    print(f'Creature №{id_c} died because of saturation! Food increased by {self.size}')
                    s = self.size
                    self.live = 0
                    return food + s, list_crs
            return food, list_crs
        return food, list_crs

    def __repr__(self):
        return self.str_info()

# c1 = Creature('bebri', 'green', 20, 'earth', 0, 40, 6, 5)
# c1.print_info()
