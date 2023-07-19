# #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
# import datetime
# class Mammals:
#     def __init__(self, height, weight, year_of_birth, age =0):
#         self.height = height
#         self.weight = weight
#         self.year_of_birth = year_of_birth
#         self.age = self.set_age()
#
#     def set_age(self):
#         current_year = datetime.datetime.now().year
#         self.age = current_year - self.year_of_birth
#         return self.age
#     def move(self):
#         print("I'm moving")
#
#     def make_noise(self):
#         pass
#     def eat(self,grass):
#         if 3 > self.hunger > 0:
#             print("I'm hungry")
#         elif self.hunger >= 3:
#             print("I'm satiety")
# class Girrafe():
#
#     def __init__(self, hunger = 100):
#          self.hunger = hunger
#     def make_noise(self):
#         print('Hum')
#     def eat(self,grass):
#         if 100 >= self.hunger > 20:
#             print("I'm hungry")
#             print("I ate")
#             self.hunger -= grass.value
#         elif self.hunger <= 20:
#             print("I'm satiety")
#             # self.hunger -= grass.value
#         return f'Now Hunger level: {self.hunger}'
#
# Das_Peter = Girrafe()
#
#
# class Grass():
#     def __init__(self, value=0):
#         self.value = value
#
# Hay = Grass(50)
# Clover = Grass(30)
# Wildberries = Grass(35)
#
#
# print(Das_Peter.eat(Wildberries))

class Knight:
    def __init__(self, sword=False):
        self.sword = sword
        self.hp = 100
        self.damage = self.set_damage()

    def set_damage(self):
        if self.sword:
            self.damage = 35
        else:
            self.damage = 5
        return self.damage
class BossKnight(Knight):
    def __init__(self, sword=False, super_damage=0):
        super().__init__(sword)
        self.super_damage = super_damage

player = Knight(True)
boss = BossKnight(True, super_damage=15)
#print(boss.damage)

while player.hp > 0 and boss.hp > 0:
    action = input('Если готовы, нажмите 1')
    if action == "1":
        print("Бьет рыцарь")
        boss.hp -= player.damage
        print("Бьет босс")
        player.hp -= boss.damage + boss.super_damage
        print(f'Жизни рыцаря: {player.hp}\nЖизни босса: {boss.hp}')
if player.hp > 0 and boss.hp < 0:
    print("Победил ыцарь")
else:
    print ('победил Босс')