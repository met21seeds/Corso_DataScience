# definizione della classe
class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self._nome = nome
        self._tipo_cucina = tipo_cucina
        self._aperto = False
        self._menu = {}
        self._descrizione_cucina = None

    # metodi della classe
    # descrivi ristorante
    def descrivi_ristorante(self):
        if self._descrizione_cucina:
            print(f"Il ristorante {self._nome} offre {self._tipo_cucina}. Descrizione della cucina: {self._descrizione_cucina}")
        else:
            print(f"Il ristorante {self._nome} offre {self._tipo_cucina}.")

    # apertura risto --> è aperto o chiuso??
    def stato_apertura(self):
        if self._aperto:
            print("Il ristorante è aperto.")
        else:
            print("Il ristorante è chiuso.")

    # ristorante aperto
    def apri_ristorante(self):
        self._aperto = True
        print(f"{self._nome} è ora aperto.")

    # risotante chiuso aperto = False
    def chiudi_ristorante(self):
        self._aperto = False
        print(f"{self._nome} è ora chiuso.")

    #aggiungi un piatto al menu
    def aggiungi_al_menu(self, piatto, prezzo):
        self._menu[piatto] = prezzo

    #togli un piatto dal menù
    def togli_dal_menu(self, piatto):
        if piatto in self._menu:
            del self._menu[piatto]

    # stampa menù
    def stampa_menu(self):
        for piatto, prezzo in self._menu.items():
            print(f"{piatto}: {prezzo}€")


#Creazione di un'istanza della classe Ristorante
ristorante = Ristorante("Da Mario", "Italiana")

# testare i metodi se funzionano o meno
ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.chiudi_ristorante()

