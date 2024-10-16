class Mobili:
    def __init__(self, materiale,tipo,prezzo):
        self.materiale = materiale
        self.tipo = tipo
        self.prezzo = prezzo

    def get_materiale(self):
        return self.materiale

    def set_materiale(self, materiale):
        self.materiale = materiale

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo (self, prezzo):
        self.prezzo = prezzo

    def descrizione(self):
        return "Materiale: " + self.materiale + "\n" "Tipo: " + self.tipo + "\n"  "Prezzo: " + self.prezzo

sedia = Mobili("Legno" , "Sedia" , "20 Euro")
print(sedia.descrizione())