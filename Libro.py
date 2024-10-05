class Libro:
    def __init__(self, titolo, anno, autore):
        self._titolo = titolo
        self._anno = anno
        self._autore = autore

    def get_titolo(self):
        return self._titolo

    def set_titolo(self, titolo):
        self._titolo = titolo

    def get_anno(self):
        return self._anno

    def set_anno(self, anno):
        self._anno = anno

    def get_autore(self):
        return self._autore

    def set_autore (self, autore):
        self._autore = autore

    def toString(self):
        return "Titolo: " + self._titolo + "\n" "Anno: " + self._anno + "\n"  "Autore: " + self._autore

PromessiSposi = Libro("I promessi sposi", "1821", "Alessandro Manzoni \n ")
Infinito = Libro("L'infinito", "1819", "Giacomo Leopardi")
print(PromessiSposi.toString())
print(Infinito.toString())


