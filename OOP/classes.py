class Auto:
    def __init__(self, model, color, year): #ициализация
        self.model = model #атрибут класса
        self.color = color  #атрибут классан
        self.year = year  #атрибут класса
    def display_into(self):
        print(f'Model: {self.model}\nYear:{self.year}\nColor:{self.color}')

auto1 = Auto('ВАЗ', 'red', 1981)
auto2 = Auto('Toyota', 'white', 2003)
auto3 = Auto('Honda', 'Gray', 2003)
auto1.display_into()
auto2.display_into()
auto3.display_into()
# print(auto1.model)