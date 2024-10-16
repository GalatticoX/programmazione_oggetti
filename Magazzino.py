from Prodotto import Prodotto
class Magazzino:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

    def rimuovi_prodotto(self, nome_prodotto):
        for prodotto in self.prodotti:
            if prodotto.nome == nome_prodotto:
                self.prodotti.remove(prodotto)
                return
        print(f"Prodotto {nome_prodotto} non trovato nel magazzino.")

    def valore_totale(self):
        valore = 0
        for prodotto in self.prodotti:
            valore += prodotto.calcola_valore()
        return valore

    def salva_file(self, nome_file):
            file_csv = open(nome_file, "w")
            file_csv.write("Nome,Prezzo, Quantità \n")
            for prodotto in self.prodotti:
                file_csv.write(f'{prodotto.nome}, {prodotto.prezzo}, {prodotto.quantita}\n')
            file_csv.close()
            print(f"Inventario salvato in {nome_file}")

    def visualizza_magazzino(self):
        if not self.prodotti:
            print("Il magazzino è vuoto.")
        for prodotto in self.prodotti:
            print(f"Prodotto: {prodotto.nome}, Prezzo: {prodotto.prezzo}, Quantità: {prodotto.quantita}")

magazzino = Magazzino()
p1 = Prodotto("Maglietta", 15.99, 50)
p2 = Prodotto("Pantaloni", 29.99, 30)
magazzino.aggiungi_prodotto(p1)
magazzino.aggiungi_prodotto(p2)
magazzino.visualizza_magazzino()
magazzino.salva_file('inventario_magazzino.csv')