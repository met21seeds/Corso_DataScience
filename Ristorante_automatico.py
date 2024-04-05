# liste di partenza + contatori vari
basi = ["Pasta frolla","Pan di spagna","Biscotto"]
prezzi_basi = [2,4,6]
farciture = ["crema","panna","cioccolata"]
prezzi_farc = [3,5,7]
toppings = ["canditi","zucchero a velo","praline"]
prezzi_toppings = [4,2,8]
count = 0 # contatore per i tavoli
#ricavi = 0 guadagno ristorante
tot_torte = 0
# Ciclo clienti
while True: 
    cliente = input ("Inserisci il nome :")
    count += 1
    tavolo = count + 1
    print ("Ciao", cliente ," il tuo tavolo è il numero", tavolo)

    # Che ingredienti vuoi per preparare la torta
    print ("Ecco gli ingredienti per la base della torta: \n" ,basi)
    scelta_base = input ("Scegli un ingrediente per la base della tua torta \n")
    # prezzo base:
    if scelta_base == 0 :
        prezzo_client = prezzi_basi[0] 
    elif scelta_base == 1 :
        prezzo_client = prezzi_basi[1]
    elif scelta_base == 2 :
        prezzo_client = prezzi_basi[2]

    # decisione_base= scelta_base
    tot_base = prezzo_client
  
    print ("Ecco gli ingredienti per la farcitura della torta: \n", farciture)
    scelta_farc = input("Scegli un ingrediente per farcirla? \n")
     # prezzo farciture:                   
    if scelta_farc == 0 :
        prezzo_client = prezzi_farc[0]
    elif scelta_farc == 1 :
        prezzo_client = prezzi_farc[1]
    elif scelta_farc == 2 :
        prezzo_client = prezzi_farc[2]
    
    # decisione_farc = scelta_farc
    tot_farc = prezzo_client
                   
    print ("Ecco la lista dei toppings disponibili : \n", toppings)
    scelta_top = input("Scegli un ingrediente : \n")
    # prezzo toppings:                   
    if scelta_top == 0 :
        prezzo_client = prezzi_toppings[0] 
    elif scelta_top == 1 :
        prezzo_client = prezzi_toppings[1]
    elif scelta_base == 2 :
        prezzo_client = prezzi_toppings[2]

    # decisione_top = scelta_top
    tot_top = prezzo_client

    tot_torta = tot_base + tot_farc + tot_top                 

#controllo tavoli disponibili
    if tavolo == 20 :
        print("Ristorante al completo. Attendi che si liberi un tavolo")
    break




# # Stampa riepilogo dell'ordine
# print("\n -- Riepilog ordine --")
# print("Cliente" : nome)
# print("tavolo": tavolo)
# print("base": basi[scelta_base] "- €" prezzi_basi[scelta_base])
# print("farcitura": farciture[scelta_farc] "- €" prezzi_farc[scelta_farc])
# print("topping":toppings[scelta_top] "- €" prezzi_top[scelta_top])

# # cacolo i ricavi del ristorante = ricavi + tot_cliente
# # torte vendute tot_torte = tot_torte + count

                      