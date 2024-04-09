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

conocreato = 0
while conocreato <=3:
    quest = input("Vuoi creare un gelato?\n")
    if quest == "sì":
        gusto1 = input("scegli il primo gusto\n")
        gusto2 = input("scegli il secondo gusto\n")
        gusto3 = input("scegli il terzo gusto\n")
        conocreato += 1
        gelato1 = GelatoScelto(3, 2.5, gusto1, gusto2, gusto3)
        print(gelato1.stampaGelato())
    else:
        print("ci vediamo la prossima volta")
        break
