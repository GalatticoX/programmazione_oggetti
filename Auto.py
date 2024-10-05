class Auto:
    def __init__ (self, marca , modello):
        self.marca = marca
        self.modello = modello
        self.km = 0
    def modifica_km(self, km):
        self.km = km

    def modifica_marcaModello(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def toString(self):
        return "Marca: " + self.marca +  ", Modello: " + self.modello + ", Km = " + str(self.km)
mia_auto = Auto("Fiat" , "Panda")
print(mia_auto.toString())
mia_auto.modifica_km(5000)
mia_auto.modifica_marcaModello("Lancia", "Epsilon")
print(mia_auto.toString())