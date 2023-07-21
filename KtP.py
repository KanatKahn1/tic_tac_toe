class Kilo_to_Pounds:
    kpt = 0.454
    def __init__(self, kg=0):
        self.kg = kg

    def Kg_to_Pn(self):
        print(f' Кило - {self.kg} = Фунтов - {self.kg / self.kpt} ')

k_t_p = Kilo_to_Pounds(2)
k_t_p.Kg_to_Pn()