import datetime
class Mammals:
    def __init__(self, height, weight, year_of_birth, age =0):
        self.height = height
        self.weight = weight
        self.year_of_birth = year_of_birth
        self.age = self.set_age()

    def set_age(self):
        current_year = datetime.datetime.now().year
        self.age = current_year - self.year_of_birth
        return self.age
    def move(self):
        print("I'm moving")

    def make_noise(self):
        pass
    def eat(self,grass):
        if 3 > self.hunger > 0:
            print("I'm hungry")
        elif self.hunger >= 3:
            print("I'm satiety")
class Girrafe():

    def __init__(self, hunger = 100):
         self.hunger = hunger
    def make_noise(self):
        print('Hum')
    def eat(self,grass):
        if 100 >= self.hunger > 20:
            print("I'm hungry")
            print("I ate")
            self.hunger -= grass.value
        elif self.hunger <= 20:
            print("I'm satiety")
            # self.hunger -= grass.value
        return f'Now Hunger level: {self.hunger}'

Das_Peter = Girrafe()


class Grass():
    def __init__(self, value=0):
        self.value = value

Hay = Grass(50)
Clover = Grass(30)
Wildberries = Grass(35)


print(Das_Peter.eat(Wildberries))
