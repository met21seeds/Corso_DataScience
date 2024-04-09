class Gelato:
    cono_venduto = 0

    def __init__(self, palline, prezzo):
        self.palline = palline
        self.prezzo = prezzo
        Gelato.cono_venduto += 1

    def descrizione(self):
        return f"Questo gelato costa {self.prezzo} euro."

class GelatoScelto(Gelato):
    def __init__(self, palline, prezzo, gusto1, gusto2, gusto3):
        super().__init__(palline, prezzo)
        self.gusto1 = gusto1
        self.gusto2 = gusto2
        self.gusto3 = gusto3

    def stampaGelato(self):
        return f"Questo gelato costa {self.prezzo} euro e ha i gusti {self.gusto1}, {self.gusto2}, {self.gusto3}."

# Creazione di istanze della classe GelatoScelto
gelato1 = GelatoScelto(3, 2.5, "cioccolato", "vaniglia", "fragola")
gelato2 = GelatoScelto(2, 3.0, "nocciola", "pistacchio" , "crema")
gelato3 = GelatoScelto(3, 3.5, "mela", "pera", "banana")

# Stampa solo se sono stati venduti almeno 3 coni di gelato
if Gelato.palline == 3:
    print(gelato_scelto1.stampaGelato())
    print(gelato_scelto2.stampaGelato())
    print(gelato_scelto3.stampaGelato())
