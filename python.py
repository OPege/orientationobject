class Animal():
    def __init__(self, pelo, especie, olhos, patas):
        self.pelo = pelo
        self.especie = especie
        self.olhos = olhos
        self.patas = patas

    def get_all(self):
        print("Esse animal é um {}, tem {} olhos e tem {} patas.".format(
            self.especie, self.olhos, self.patas))

porco = Animal(True, "Suíno", 2, 4)

porco.get_all()
    
class Cachorro(Animal):

    def __init__(self, raca, olhos, patas, nome, ):
        self.raca = raca
        self.olhos = olhos
        self.patas = patas
        self.nome = nome

cleiton = Cachorro('vira lara', 1, 3,'cleiton')
cleiton.quero_todas_as_informacoes()
