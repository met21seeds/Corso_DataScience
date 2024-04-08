# definizione della classe
class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}
        self.descrizione_cucina = None

# metodi della classe
# descrivi ristorante
def descrivi_ristorante(self):
    if self.descrizione_cucina:
        print(f"Il ristorante {self.nome} offre {self.tipo_cucina}. Descrizione della cucina: {self.descrizione_cucina}")
    else:
        print(f"Il ristorante {self.nome} offre {self.tipo_cucina}.")

# def chiedi_descrizione_cucina(self):
#     risposta = input("Vuoi aggiungere una descrizione della tua cucina? (s/n) ")
#     if risposta.lower() == 's':
#         self.descrizione_cucina = input("Inserisci la descrizione della tua cucina: ")

# apertura risto --> è aperto o chiuso??
def stato_apertura(self):
    if self.aperto:
        print("Il ristorante è aperto.")
    else:
        print("Il ristorante è chiuso.")

# ristorante aperto
def apri_ristorante(self):
    self.aperto = True
    print(f"{self.nome} è ora aperto.")

# risotante chiuso aperto = False
def chiudi_ristorante(self):
    self.aperto = False
    print(f"{self.nome} è ora chiuso.")

#Creazione di un'istanza della classe Ristorante
ristorante = Ristorante("Da Mario", "Italiana")


#aggiungi un piatto al menu
def aggiungi_al_menu(self, piatto, prezzo):
    self.menu[piatto] = prezzo

#togli un piatto dal menù
#def togli_dal_menu(self, piatto):
 #       if piatto in self.menu:
  #          del self.menu[piatto]

# stampa menù
def stampa_menu(self):
    for piatto, prezzo in self.menu.items():
        print(f"{piatto}: {prezzo}€")



# testare i metodi se funzionano o meno
ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.chiudi_ristorante()

