class Tomato:
   stages = ['Отсутвует','Цветение','Зеленый','Красный']
   def __init__(self, idx = 0, count = 0):
       self.idx = idx
       self.state = self.stages[self.idx]

   def grow (self):
       if self.idx < 3:
        self.idx += 1

   def is_ripe(self):
       return True if self.idx ==3 else False
   def console (self):
       print(self.state[self.idx])


class Bush():

    def __init__(self,count=0):
        self.count = count
        self.tomatoes = [Tomato() for i in range(self.count)]
    def grow_all(self):
        for tomatoe in self.tomatoes:
            tomatoe.grow()

    def ripe_all(self):
        return all([t.is_ripe() for t in self.tomatoes])

    def console(self):
        print("кол-во помидоров:", self.count)




class Gardener:
    def __init__(self,name,plant,count=0):
        self.count = count
        self.name = name
        self.plant = plant

    def work(self):
        self.plant.grow_all()

    def gather_crop(self):
        if self.plant.ripe_all():
          self.plant.Tomatoes = []
          print(f'собранно {self.count} помидоров')

bush = Bush(15)
