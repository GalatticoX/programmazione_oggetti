class Cane:
    def __init__(self,nome , razza):
        self.nome = nome
        self.razza = razza
    def abbaia(self):
        print("Woof!")

fido = Cane("Fido", "Corso")
fido.abbaia()
print("Il nome del cane è: " + fido.nome + "." "\n" + "La razza del cane è: " + fido.razza + ".")