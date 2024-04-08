# creo classse libro
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
#creo funzione descrizione
    def descrizione(self):
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha '{self.pagine}' pagine."

while True:
    titolo = input("Dimmi il titolo di un libro:\n")
    autore = input("Chi è l'autore del libro?\n")
    pagine = input("Quante pagine ha il libro?\n")

    libro = Libro(titolo, autore, pagine)
    print(libro.descrizione())

