# Creo classe figlio denominata Giorno i cui attributi saranno giorno vendita e importo delle vendite di un determinato giorno
# definisco un metodo per sommare il totale di più giorni , un altro metodo media che andrà a calcolare la media nella lista registro vendite
# Creo una classe padre vendite e all'interno inserirò una lista vuota che rappresenta il totale delle vendite di un determinato giorno che è il reigistro vendite

class Vendite:
    def __init__(self):
        self.vendite_per_giorno = [] # Ottimizzabile con un dizionario

    def tot(self):
        return sum(self.vendite_per_giorno)

    def calcola_media(self):
        return self.tot() / len(self.vendite_per_giorno) if self.vendite_per_giorno else 0

    def giorno_vendite_max(self):
        if not self.vendite_per_giorno:
            return None
        max_vendite = max(self.vendite_per_giorno)
        giorno = self.vendite_per_giorno.index(max_vendite) + 1
        return giorno, max_vendite

    def sopra_media(self):
        media = self.calcola_media()
        return [i+1 for i, vendite in enumerate(self.vendite_per_giorno) if vendite > media]

class Giorno:
    def __init__(self, giorno, importo):
        self.giorno = giorno
        self.importo = importo

    def aggiungi_vendite(self, vendite):
        vendite.vendite_per_giorno.append(self.importo)

    def visualizza_giorno(self):
        print(f"Giorno {self.giorno}: {self.importo} vendite")

def inserimento_dati(vendite):
    while True:
        try:
            giorno = int(input("Inserisci il numero del giorno: "))
            importo = int(input("Inserisci l'importo delle vendite per il giorno: "))
            giorno = Giorno(giorno, importo)
            giorno.aggiungi_vendite(vendite)
            giorno.visualizza_giorno()
            if input("Vuoi inserire un altro giorno? (s/n) ").lower() != 's':
                break
        except ValueError:
            print("Errore: inserisci solo numeri.")

vendite = Vendite()
inserimento_dati(vendite)
print(f"Totale vendite: {vendite.tot()}")
print(f"Media vendite: {vendite.calcola_media()}")
if vendite.vendite_per_giorno:
    print(f"Giorno con vendite massime: {vendite.giorno_vendite_max()}")
    print(f"Giorni con vendite sopra la media: {vendite.sopra_media()}")
else:
    print("Non sono presenti dati di vendita.")

