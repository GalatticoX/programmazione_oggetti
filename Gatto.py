class Gatto:
    def __init__(self, nome, colore, eta):
        self.nome = nome
        self.colore = colore
        self.eta = eta

    def miagola(self):
        print("Meow")
    def modifica_nome(self,nuovoNome):
        self.nome = nuovoNome

fuffy = Gatto ("Fuffy", "Arancione", "6")
fuffy.miagola()
print (fuffy.nome + "\n" + fuffy.colore + "\n" + fuffy.eta)
fuffy.modifica_nome("Filippo")
print(fuffy.nome)
