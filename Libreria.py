# esercizio : Immagina di gestire una libreria. Crea due classi : Libro e Libreria
# 1 la classe libro dovrebbe avere gli attributi : titolo , autore , isbn (numero identificativo)

class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

# 2 Inoltre, dovrebbe avere un metodo descrizione() che restituisce una stringa che descrive il libro usando tutti e tre gli attributi.
    def descrizione(self):
        return f"Libro: {self.titolo} di {self.autore}, ISBN: {self.isbn}"

# 3 La classe Libreria dovrebbe avere l'attributo : catalogo (una lista che conterrà gli oggetti della classe Libro) --> devo salvare i libri dentro una lista
class Libreria:
    def __init__(self):
        self.catalogo = []


# 4 La classe Libreria dovrebbe avere i seguenti metodi :
# aggiungi_libro(libro) : che prende in input un oggetto della classe Libro e lo aggiunge al catalogo.
# rimuovi_libro(isbn) : che rimuove un libro dal catalogo in base al suo isbn.
# cerca_per_titolo(titolo): che restituisce una lista di libri che corrispondono al titolo dato.
# mostra_catalogo() : che stampa una descrizione di tutti i libri presenti nel catalogo


