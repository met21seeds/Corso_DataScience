# definizione della classe
class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}
        self.descrizione_cucina = None  #---> + metodo per aggiungere la descrizione della propria cucina??


# metodi della classe
# descrivi ristorante
def descrivi_ristorante(self):
    if self.descrizione_cucina:
        print(f"Il ristorante {self.nome} offre {self.tipo_cucina}. Descrizione della cucina: {self.descrizione_cucina}")
    else:
        print(f"Il ristorante {self.nome} offre {self.tipo_cucina}.")

def chiedi_descrizione_cucina(self):
        risposta = input("Vuoi aggiungere una descrizione della tua cucina? (s/n) ")
        if risposta.lower() == 's':
            self.descrizione_cucina = input("Inserisci la descrizione della tua cucina: ")

# apertura risto --> è aperto o chiuso??
# chiudi risto come sopra aperto = False di coneguenza il risto è chiuso
#aggiungi un piatto al menu
#togli un piatto al meno
# stampa menù



# testare i metodi se funzionano o meno
