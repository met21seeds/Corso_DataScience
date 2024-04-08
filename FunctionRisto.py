# definizione della classe
class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}
        #self.descrizione_cucina = None  ---> + metodo per aggiungere la descrizione della propria cucina??


# metodi della classe

# def chiedi_descrizione_cucina(self):
#         risposta = input("Vuoi aggiungere una descrizione della tua cucina? (s/n) ")
#         if risposta.lower() == 's':
#             self.descrizione_cucina = input("Inserisci la descrizione della tua cucina: ")

# testare la classe
