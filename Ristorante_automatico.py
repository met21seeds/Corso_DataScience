# da rivedere variabili prezzo_client e ciclo , un po di confusione
# liste 
basi = ["pasta frolla","pan di spagna","biscotto"]
prezzi_basi = [2,4,6]
farciture = ["crema","panna","cioccolata"]
prezzi_farc = [3,5,7]
toppings = ["canditi","zucchero a velo","praline"]
prezzi_top = [4,2,8]
tavolo = 1
ricavi = 0 #guadagno ristorante
tot_torte = 0
# Ciclo clienti   
while True :
    cliente = input ("Può dirmi il suo nome? \n ")
    print ("Ciao", cliente ,"! il tuo tavolo è il numero", tavolo)
    tavolo = + 1
    # Che ingredienti vuoi per preparare la torta
    print ("Ecco gli ingredienti per la base della torta: \n" ,basi)
    scelta_base = input ("Scegli un ingrediente per la base della tua torta \n")

    # prezzo base:
    if scelta_base == "pasta frolla" :
        prezzo_client1 = prezzi_basi[0] 
    elif scelta_base == "pan di spagna":
        prezzo_client1 = prezzi_basi[1]
    else :
        prezzo_client1 = prezzi_basi[2]

    print("Hai scelto :", scelta_base, "prezzo: €",prezzo_client1)
    
    print ("Ecco gli ingredienti per la farcitura della torta: \n", farciture)
    scelta_farc = input("Scegli un ingrediente per farcirla? \n")
     # prezzo farciture:                   
    if scelta_farc == "crema" :
        prezzo_client2 = prezzi_farc[0]
    elif scelta_farc == "panna" :
        prezzo_client2 = prezzi_farc[1]
    elif scelta_farc == "cioccolata" :
        prezzo_client2 = prezzi_farc[2]

    print("Hai scelto :", scelta_farc, "prezzo: €",prezzo_client2)
                   
    print ("Ecco la lista dei toppings disponibili : \n", toppings)
    scelta_top = input("Scegli un ingrediente : \n")
    # prezzo toppings:                   
    if scelta_top == "canditi" :
        prezzo_client3 = prezzi_top[0] 
    elif scelta_top == "zucchero a velo" :
        prezzo_client3 = prezzi_top[1]
    else :
        prezzo_client3 = prezzi_top[2]

    print("Hai scelto :", scelta_top, "prezzo: €",prezzo_client3)

    tot_torta = prezzo_client1 + prezzo_client2 + prezzo_client3
    print("Lua torta è pronta costerà : €" , tot_torta)

    tot_torte += 1
    ricavi = tot_torta
    print("Torte vendute :",tot_torte)
    print("incasso: €", ricavi)                
 
    if tavolo == 20 :
        print("Ristorante al completo. Attendi che si liberi un tavolo")
    break


                      
