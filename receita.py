class Receita():
    def __init__(self, ingredientes, modo_de_preparo, tempo, porcao):
        self.ingredientes = ingredientes
        self.modo = modo_de_preparo
        self.tempo = tempo
        self.porcao = porcao

    def get_all(self):
        print("Essa receita tem {}, para fazer {}, tempo total é {}, serve {}.".format(
            self.ingredientes, self.modo, self.tempo, self.porcao))

torta = Receita("ovos, farinha , mateiga , acucar", "misture os ingrediente e leve ao forno", "30 minutos", "Serve 4 pessoas")

torta.get_all()
    
# class Cachorro(Animal):

#     def __init__(self, raca, olhos, patas, nome, ):
#         self.raca = raca
#         self.olhos = olhos
#         self.patas = patas
#         self.nome = nome

# cleiton = Cachorro('vira lara', 1, 3,'cleiton')
# cleiton.quero_todas_as_informacoes()

