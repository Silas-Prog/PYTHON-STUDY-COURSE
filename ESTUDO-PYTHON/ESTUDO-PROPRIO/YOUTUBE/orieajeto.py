class Carro:
    def __init__(self, nome, marca, id):
        self.nome = nome
        self.marca = marca
        self.id = id
        
    def encher_pneu(self):
        print("Hora de calibrar os pneus!")

    def gasolina(self):
        print(veiculos.nome, veiculos.marca, veiculos.id)

veiculos = Carro('Uno', 'chevrolet','2025')
veiculos.encher_pneu()
veiculos.gasolina()