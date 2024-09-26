class Hefter:
    def __init__(self, initiale_blaetter):
        """
        Das Argument initiale_blaetter ist eine Liste von Strings
        und wird dem Instanzattribut blaetter zugewiesen.
        """
        self.blaetter = initiale_blaetter

    def blatt_hinzufuegen(self, blatt):
        """Fuegt ein Blatt der Liste von Blaettern am Ende hinzu."""
        self.blaetter.append(blatt)

    def blatt_entfernen(self):
        """Entfernt das letzte Blatt aus der Liste von Blaettern."""
        return blaetter.pop()

    def zeige_alle_blaetter(self):
        """
        Gibt nacheinander alle Blaetter aus der Liste von
        Blaettern aus.
        """
        for blatt in self.blaetter:
            print(blatt)

if __name__ == "__main__":
    blaetter = ["Blatt 1", "Blatt 2"]
    hefter = Hefter(blaetter)
    hefter.blatt_entfernen()
    hefter.blatt_hinzufuegen("Neues Blatt")
    hefter.zeige_alle_blaetter()
