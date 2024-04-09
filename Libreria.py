# esercizio : Immagina di gestire una libreria. Crea due classi : Libro e Libreria
# 1 la classe libro dovrebbe avere gli attributi : titolo , autore , isbn (numero identificativo)

class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

        # 2 metodo descrizione() che restituisce una stringa che descrive il libro usando tutti e tre gli attributi.
    def descrizione(self):
        return f"Libro: {self.titolo} di {self.autore}, ISBN: {self.isbn}"

        # 3 La classe Libreria dovrebbe avere l'attributo : catalogo (una lista che conterrà gli oggetti della classe Libro) --> devo salvare i libri dentro una lista

class Libreria(Libro):
    def __init__(self, isbn, titolo, autore, catalogo):
        super().__init__(isbn, titolo, autore)
        self.catalogo = catalogo  # Lista o dizionario o dizionario dentro una lista ?
        catalogo = {}

 
        # Aggiunta del libro al catalogo prende in input un oggetto della classe Libro e lo aggiunge al catalogo.
    def aggiungi_libro(self, isbn, titolo, autore, catalogo):
        if self.titolo in catalogo:
            return "Errore: titolo già presente."
        else:
            nuovo_libro = Libro(isbn, titolo, autore)
            self.catalogo.append(nuovo_libro)
            return "Libro aggiunto con successo."

 
        # rimuovi_libro(isbn) : che rimuove un libro dal catalogo in base al suo isbn. --> forse serve dizionario per il catalogo
    def rimuovi_libro(self,catalogo) :
        if self.titolo in catalogo:
            del catalogo[self.titolo] 
            print(f"Hai rimosso il libro intitolato {self.titolo} di {self.autore}, ISBN: {self.isbn}")
        else: 
            print("libro non trovato")

        # cerca_per_titolo(titolo): che restituisce una lista di libri che corrispondono al titolo dato. --> ciclo per la ricerca del libro in catalogo , titolo è == all'input??
    #def cerca_per_titolo(self) : 




        # mostra_catalogo() : che stampa una descrizione di tutti i libri presenti nel catalogo
    def mostra_catalogo(self, catalogo):
        print("Catalogo" , catalogo)
        



# Creazione di un oggetto Libro
titolo = input("Inserisci il titolo del libro: ")
autore = input("Inserisci l'autore del libro: ")
isbn = input("Inserisci l'ISBN del libro: ")
nuovo_libro = Libro(titolo, autore, isbn)
