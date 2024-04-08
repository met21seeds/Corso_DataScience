# definizione della classe
class Ristorante:
    def __init__(self):
        self.nome = input("Inserisci nome risotrante: ")
        self.tipo_cucina = input("Inserisci tipo cucina: ")
        self.aperto = True
        self.menu = {}

    # metodi della classe

    # descrivi ristorante
    def descrivi_ristorante(self):
        return print(f"Il ristorante {self.nome} offre cucina {self.tipo_cucina}")
        

    # apertura risto --> è aperto o chiuso??
    def stato_apertura(self):
        if self.aperto == True :
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

    #aggiungi un piatto al menu
    def aggiungi_al_menu(self):
        aggiunta = input("Vuoi aggiungere un piatto al menù? \n sì \n no ")
        if aggiunta == "sì":
            piatto = input("Inserisci nome piatto: ")
            prezzo = input("Inserisci prezzo del piatto: ")
            self.menu[piatto] = prezzo
            print("Al menu è stato aggiunto", piatto, "con un prezzo di", prezzo)
        else:
            print("Ok, nessuna aggiunta per oggi")


    #togli un piatto dal menù
    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]

    # stampa menù
    def stampa_menu(self):
        for piatto, prezzo in self.menu.items():
            print(f"{piatto}: {prezzo}€")

#Creazione di un'istanza della classe Ristorante
ristorante = Ristorante()

# testare i metodi se funzionano o meno
ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.chiudi_ristorante()
ristorante.aggiungi_al_menu()
ristorante.stampa_menu()
